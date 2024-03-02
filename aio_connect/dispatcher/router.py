from __future__ import annotations

from typing import Any, Dict, Final, Generator, List, Optional, Set

from ..types import ConnectObject
from .event.bases import REJECTED, UNHANDLED
from .event.event import EventObserver
from .event.connect import ConnectEventObserver

INTERNAL_UPDATE_TYPES: Final[frozenset[str]] = frozenset({"update", "error"})


class Router:
    """
    Router can route update, and it nested update types

    Event handlers can be registered in observer by two ways:

    - By observer method - :obj:`router.<event_type>.register(handler, <filters, ...>)`
    - By decorator - :obj:`@router.<event_type>(<filters, ...>)`
    """

    def __init__(self, *, name: Optional[str] = None) -> None:
        """
        :param name: Optional router name, can be useful for debugging
        """

        self.name = name or hex(id(self))

        self._parent_router: Optional[Router] = None
        self.sub_routers: List[Router] = []

        # Observers
        self.competence = ConnectEventObserver(router=self, event_name="competence")
        self.line = ConnectEventObserver(router=self, event_name="line")
        self.subscriber = ConnectEventObserver(router=self, event_name="subscriber")
        self.subscription = ConnectEventObserver(router=self, event_name="subscription")
        self.support_line = ConnectEventObserver(router=self, event_name="support_line")

        self.errors = self.error = ConnectEventObserver(router=self, event_name="error")

        self.startup = EventObserver()
        self.shutdown = EventObserver()

        self.observers: Dict[str, ConnectEventObserver] = {
            "competence": self.competence,
            "line": self.line,
            "subscriber": self.subscriber,
            "subscription": self.subscription,
            "support_line": self.support_line,

            "error": self.errors,
        }

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.name!r}"

    def __repr__(self) -> str:
        return f"<{self}>"

    def resolve_used_update_types(self, skip_events: Optional[Set[str]] = None) -> List[str]:
        """
        Resolve registered event names

        Is useful for getting updates only for registered event types.

        :param skip_events: skip specified event names
        :return: set of registered names
        """
        handlers_in_use: Set[str] = set()
        if skip_events is None:
            skip_events = set()
        skip_events = {*skip_events, *INTERNAL_UPDATE_TYPES}

        for router in self.chain_tail:
            for update_name, observer in router.observers.items():
                if observer.handlers and update_name not in skip_events:
                    handlers_in_use.add(update_name)

        return list(sorted(handlers_in_use))  # NOQA: C413

    async def propagate_event(self, update_type: str, event: ConnectObject, **kwargs: Any) -> Any:
        kwargs.update(event_router=self)
        observer = self.observers.get(update_type)

        async def _wrapped(connect_event: ConnectObject, **data: Any) -> Any:
            return await self._propagate_event(
                observer=observer, update_type=update_type, event=connect_event, **data
            )

        if observer:
            return await observer.wrap_outer_middleware(_wrapped, event=event, data=kwargs)
        return await _wrapped(event, **kwargs)

    async def _propagate_event(
        self,
        observer: Optional[ConnectEventObserver],
        update_type: str,
        event: ConnectObject,
        **kwargs: Any,
    ) -> Any:
        response = UNHANDLED
        if observer:
            # Check globally defined filters before any other handler will be checked.
            # This check is placed here instead of `trigger` method to add possibility
            # to pass context to handlers from global filters.
            result, data = await observer.check_root_filters(event, **kwargs)
            if not result:
                return UNHANDLED
            kwargs.update(data)
            response = await observer.trigger(event, **kwargs)
            if response is REJECTED:  # pragma: no cover
                # Possible only if some handler returns REJECTED
                return UNHANDLED
            if response is not UNHANDLED:
                return response

        for router in self.sub_routers:
            response = await router.propagate_event(update_type=update_type, event=event, **kwargs)
            if response is not UNHANDLED:
                break

        return response

    @property
    def chain_head(self) -> Generator[Router, None, None]:
        router: Optional[Router] = self
        while router:
            yield router
            router = router.parent_router

    @property
    def chain_tail(self) -> Generator[Router, None, None]:
        yield self
        for router in self.sub_routers:
            yield from router.chain_tail

    @property
    def parent_router(self) -> Optional[Router]:
        return self._parent_router

    @parent_router.setter
    def parent_router(self, router: Router) -> None:
        """
        Internal property setter of parent router fot this router.
        Do not use this method in own code.
        All routers should be included via `include_router` method.

        Self- and circular- referencing are not allowed here

        :param router:
        """
        if not isinstance(router, Router):
            raise ValueError(f"router should be instance of Router not {type(router).__name__!r}")
        if self._parent_router:
            raise RuntimeError(f"Router is already attached to {self._parent_router!r}")
        if self == router:
            raise RuntimeError("Self-referencing routers is not allowed")

        parent: Optional[Router] = router
        while parent is not None:
            if parent == self:
                raise RuntimeError("Circular referencing of Router is not allowed")

            parent = parent.parent_router

        self._parent_router = router
        router.sub_routers.append(self)

    def include_routers(self, *routers: Router) -> None:
        """
        Attach multiple routers.

        :param routers:
        :return:
        """
        if not routers:
            raise ValueError("At least one router must be provided")
        for router in routers:
            self.include_router(router)

    def include_router(self, router: Router) -> Router:
        """
        Attach another router.

        :param router:
        :return:
        """
        if not isinstance(router, Router):
            raise ValueError(
                f"router should be instance of Router not {type(router).__class__.__name__}"
            )
        router.parent_router = self
        return router

    async def emit_startup(self, *args: Any, **kwargs: Any) -> None:
        """
        Recursively call startup callbacks

        :param args:
        :param kwargs:
        :return:
        """
        kwargs.update(router=self)
        await self.startup.trigger(*args, **kwargs)
        for router in self.sub_routers:
            await router.emit_startup(*args, **kwargs)

    async def emit_shutdown(self, *args: Any, **kwargs: Any) -> None:
        """
        Recursively call shutdown callbacks to graceful shutdown

        :param args:
        :param kwargs:
        :return:
        """
        kwargs.update(router=self)
        await self.shutdown.trigger(*args, **kwargs)
        for router in self.sub_routers:
            await router.emit_shutdown(*args, **kwargs)
