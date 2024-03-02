from __future__ import annotations

import asyncio
import warnings
from asyncio import Event, Lock
from typing import Any, Dict, Optional, Set

from .. import loggers
from ..client.bot import Bot
from ..exceptions import ConnectAPIError
from ..fsm.middleware import FSMContextMiddleware
from ..fsm.storage.base import BaseEventIsolation, BaseStorage
from ..fsm.storage.memory import DisabledEventIsolation, MemoryStorage
from ..methods import ConnectMethod
from ..types import Update
from ..types.update import UpdateTypeLookupError
from .event.bases import UNHANDLED, SkipHandler
from .event.connect import ConnectEventObserver
from .middlewares.error import ErrorsMiddleware
from .middlewares.user_context import UserContextMiddleware
from .router import Router


class Dispatcher(Router):
    """
    Root router
    """

    def __init__(
        self,
        *,  # * - Preventing to pass instance of Bot to the FSM storage
        storage: Optional[BaseStorage] = None,
        events_isolation: Optional[BaseEventIsolation] = None,
        disable_fsm: bool = False,
        name: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        Root router

        :param storage: Storage for FSM
        :param fsm_strategy: FSM strategy
        :param events_isolation: Events isolation
        :param disable_fsm: Disable FSM, note that if you disable FSM
            then you should not use storage and events isolation
        :param kwargs: Other arguments, will be passed as keyword arguments to handlers
        """
        super(Dispatcher, self).__init__(name=name)

        if storage and not isinstance(storage, BaseStorage):
            raise TypeError(
                f"FSM storage should be instance of 'BaseStorage' not {type(storage).__name__}"
            )

        # 1C-Connect API provides originally only one event type - Update
        # For making easily interactions with events here is registered handler which helps
        # to separate Update to different event types
        self.update = self.observers["update"] = ConnectEventObserver(
            router=self, event_name="update"
        )
        self.update.register(self._listen_update)

        # Error handlers should work is out of all other functions
        # and should be registered before all others middlewares
        self.update.outer_middleware(ErrorsMiddleware(self))

        # User context middleware makes small optimization for all other builtin
        # middlewares via caching the user and chat instances in the event context
        self.update.outer_middleware(UserContextMiddleware())

        # FSM middleware should always be registered after User context middleware
        # because here is used context from previous step
        self.fsm = FSMContextMiddleware(
            storage=storage or MemoryStorage(),
            events_isolation=events_isolation or DisabledEventIsolation(),
        )
        if not disable_fsm:
            # Note that when FSM middleware is disabled, the event isolation is also disabled
            # Because the isolation mechanism is a part of the FSM
            self.update.outer_middleware(self.fsm)
        self.shutdown.register(self.fsm.close)

        self.workflow_data: Dict[str, Any] = kwargs
        self._running_lock = Lock()
        self._stop_signal: Optional[Event] = None
        self._stopped_signal: Optional[Event] = None
        self._handle_update_tasks: Set[asyncio.Task[Any]] = set()

    def __getitem__(self, item: str) -> Any:
        return self.workflow_data[item]

    def __setitem__(self, key: str, value: Any) -> None:
        self.workflow_data[key] = value

    def __delitem__(self, key: str) -> None:
        del self.workflow_data[key]

    def get(self, key: str, /, default: Optional[Any] = None) -> Optional[Any]:
        return self.workflow_data.get(key, default)

    @property
    def storage(self) -> BaseStorage:
        return self.fsm.storage

    @property
    def parent_router(self) -> Optional[Router]:
        """
        Dispatcher has no parent router and can't be included to any other routers or dispatchers

        :return:
        """
        return None  # noqa: RET501

    @parent_router.setter
    def parent_router(self, value: Router) -> None:
        """
        Dispatcher is root Router then configuring parent router is not allowed

        :param value:
        :return:
        """
        raise RuntimeError("Dispatcher can not be attached to another Router.")

    async def feed_update(self, bot: Bot, update: Update, **kwargs: Any) -> Any:
        """
        Main entry point for incoming updates
        Response of this method can be used as Webhook response

        :param bot:
        :param update:
        """
        loop = asyncio.get_running_loop()
        handled = False
        start_time = loop.time()

        if update.bot != bot:
            # Re-mounting update to the current bot instance for making possible to
            # use it in shortcuts.
            # Here is update is re-created because we need to propagate context to
            # all nested objects and attributes of the Update, but it
            # is impossible without roundtrip to JSON :(
            # The preferred way is that pass already mounted Bot instance to this update
            # before call feed_update method
            update = Update.model_validate(update.model_dump(), context={"bot": bot})

        try:
            response = await self.update.wrap_outer_middleware(
                self.update.trigger,
                update,
                {
                    **self.workflow_data,
                    **kwargs,
                    "bot": bot,
                },
            )
            handled = response is not UNHANDLED
            return response
        finally:
            finish_time = loop.time()
            duration = (finish_time - start_time) * 1000
            loggers.event.info(
                "Update is %s. Duration %d ms",
                "handled" if handled else "not handled",
                duration
            )

    async def feed_raw_update(self, bot: Bot, update: Dict[str, Any], **kwargs: Any) -> Any:
        """
        Main entry point for incoming updates with automatic Dict->Update serializer

        :param bot:
        :param update:
        :param kwargs:
        """
        parsed_update = Update.model_validate(update, context={"bot": bot})
        return await self.feed_update(bot=bot, update=parsed_update, **kwargs)

    async def _listen_update(self, update: Update, **kwargs: Any) -> Any:
        """
        Main updates listener

        Workflow:
        - Detect content type and propagate to observers in current router
        - If no one filter is pass - propagate update to child routers as Update

        :param update:
        :param kwargs:
        :return:
        """
        try:
            update_type = update.event_type
            event = update.event
        except UpdateTypeLookupError as e:
            warnings.warn(
                "Detected unknown update type.\n"
                "Seems like Connect Bot API was updated and you have "
                "installed not latest version of aio_connect framework"
                f"\nUpdate: {update.model_dump_json(exclude_unset=True)}",
                RuntimeWarning,
            )
            raise SkipHandler() from e

        kwargs.update(event_update=update)

        return await self.propagate_event(update_type=update_type, event=event, **kwargs)

    @classmethod
    async def silent_call_request(cls, bot: Bot, result: ConnectMethod[Any]) -> None:
        """
        Simulate answer into WebHook

        :param bot:
        :param result:
        :return:
        """
        try:
            await bot(result)
        except ConnectAPIError as e:
            # In due to WebHook mechanism doesn't allow getting response for
            # requests called in answer to WebHook request.
            # Need to skip unsuccessful responses.
            # For debugging here is added logging.
            loggers.event.error("Failed to make answer: %s: %s", e.__class__.__name__, e)

    async def _feed_webhook_update(self, bot: Bot, update: Update, **kwargs: Any) -> Any:
        """
        The same with `Dispatcher.process_update()` but returns real response instead of bool
        """
        try:
            return await self.feed_update(bot, update, **kwargs)
        except Exception as e:
            loggers.event.exception(
                "Cause exception while process update \n%s: %s",
                e.__class__.__name__,
                e,
            )
            raise
