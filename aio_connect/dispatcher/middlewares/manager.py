import functools
from typing import Any, Callable, Dict, List, Optional, Sequence, Union, overload

from aio_connect.dispatcher.event.bases import (
    MiddlewareEventType,
    MiddlewareType,
    NextMiddlewareType,
)
from aio_connect.dispatcher.event.handler import CallbackType
from aio_connect.types import ConnectObject


class MiddlewareManager(Sequence[MiddlewareType[ConnectObject]]):
    def __init__(self) -> None:
        self._middlewares: List[MiddlewareType[ConnectObject]] = []

    def register(
        self,
        middleware: MiddlewareType[ConnectObject],
    ) -> MiddlewareType[ConnectObject]:
        self._middlewares.append(middleware)
        return middleware

    def unregister(self, middleware: MiddlewareType[ConnectObject]) -> None:
        self._middlewares.remove(middleware)

    def __call__(
        self,
        middleware: Optional[MiddlewareType[ConnectObject]] = None,
    ) -> Union[
        Callable[[MiddlewareType[ConnectObject]], MiddlewareType[ConnectObject]],
        MiddlewareType[ConnectObject],
    ]:
        if middleware is None:
            return self.register
        return self.register(middleware)

    @overload
    def __getitem__(self, item: int) -> MiddlewareType[ConnectObject]:
        pass

    @overload
    def __getitem__(self, item: slice) -> Sequence[MiddlewareType[ConnectObject]]:
        pass

    def __getitem__(
        self, item: Union[int, slice]
    ) -> Union[MiddlewareType[ConnectObject], Sequence[MiddlewareType[ConnectObject]]]:
        return self._middlewares[item]

    def __len__(self) -> int:
        return len(self._middlewares)

    @staticmethod
    def wrap_middlewares(
        middlewares: Sequence[MiddlewareType[MiddlewareEventType]], handler: CallbackType
    ) -> NextMiddlewareType[MiddlewareEventType]:
        @functools.wraps(handler)
        def handler_wrapper(event: ConnectObject, kwargs: Dict[str, Any]) -> Any:
            return handler(event, **kwargs)

        middleware = handler_wrapper
        for m in reversed(middlewares):
            middleware = functools.partial(m, middleware)
        return middleware
