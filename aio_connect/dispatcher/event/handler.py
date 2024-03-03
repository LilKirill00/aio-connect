import asyncio
import contextvars
import inspect
import warnings
from dataclasses import dataclass, field
from functools import partial
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from magic_filter.magic import MagicFilter as OriginalMagicFilter

from ...filters.base import Filter
from ...handlers import BaseHandler
from ...utils.magic_filter import MagicFilter
from ...utils.warnings import Recommendation

CallbackType = Callable[..., Any]


@dataclass
class CallableObject:
    callback: CallbackType
    awaitable: bool = field(init=False)
    params: Set[str] = field(init=False)
    varkw: bool = field(init=False)

    def __post_init__(self) -> None:
        callback = inspect.unwrap(self.callback)
        self.awaitable = inspect.isawaitable(callback) or inspect.iscoroutinefunction(callback)
        spec = inspect.getfullargspec(callback)
        self.params = {*spec.args, *spec.kwonlyargs}
        self.varkw = spec.varkw is not None

    def _prepare_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        if self.varkw:
            return kwargs

        return {k: kwargs[k] for k in self.params if k in kwargs}

    async def call(self, *args: Any, **kwargs: Any) -> Any:
        wrapped = partial(self.callback, *args, **self._prepare_kwargs(kwargs))
        if self.awaitable:
            return await wrapped()

        loop = asyncio.get_event_loop()
        context = contextvars.copy_context()
        wrapped = partial(context.run, wrapped)
        return await loop.run_in_executor(None, wrapped)


@dataclass
class FilterObject(CallableObject):
    magic: Optional[MagicFilter] = None

    def __post_init__(self) -> None:
        if isinstance(self.callback, OriginalMagicFilter):
            # MagicFilter instance is callable but generates
            # only "CallOperation" instead of applying the filter
            self.magic = self.callback
            self.callback = self.callback.resolve
            if not isinstance(self.magic, MagicFilter):
                warnings.warn(
                    category=Recommendation,
                    message="You are using F provided by magic_filter package directly, "
                    "but it lacks `.as_()` extension."
                    "\n Please change the import statement: from `from magic_filter import F` "
                    "to `from aio_connect import F` to silence this warning.",
                    stacklevel=6,
                )

        super(FilterObject, self).__post_init__()

        if isinstance(self.callback, Filter):
            self.awaitable = True


@dataclass
class HandlerObject(CallableObject):
    filters: Optional[List[FilterObject]] = None

    def __post_init__(self) -> None:
        super(HandlerObject, self).__post_init__()
        callback = inspect.unwrap(self.callback)
        if inspect.isclass(callback) and issubclass(callback, BaseHandler):
            self.awaitable = True

    async def check(self, *args: Any, **kwargs: Any) -> Tuple[bool, Dict[str, Any]]:
        if not self.filters:
            return True, kwargs
        for event_filter in self.filters:
            check = await event_filter.call(*args, **kwargs)
            if not check:
                return False, kwargs
            if isinstance(check, dict):
                kwargs.update(check)
        return True, kwargs
