from abc import ABC, abstractmethod
from typing import Any, Awaitable, Callable, Dict, TypeVar

from ...types import ConnectObject

T = TypeVar("T")


class BaseMiddleware(ABC):
    """
    Generic middleware class
    """

    @abstractmethod
    async def __call__(
        self,
        handler: Callable[[ConnectObject, Dict[str, Any]], Awaitable[Any]],
        event: ConnectObject,
        data: Dict[str, Any],
    ) -> Any:  # pragma: no cover
        """
        Execute middleware

        :param handler: Wrapped handler in middlewares chain
        :param event: Incoming event (Subclass of :class:`aio_connect.types.base.ConnectObject`)
        :param data: Contextual data. Will be mapped to handler arguments
        :return: :class:`Any`
        """
        pass
