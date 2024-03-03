from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Protocol

from ....methods import Response, ConnectMethod
from ....methods.base import ConnectType

if TYPE_CHECKING:
    from ...bot import Bot


class NextRequestMiddlewareType(Protocol[ConnectType]):  # pragma: no cover
    async def __call__(
        self,
        bot: "Bot",
        method: ConnectMethod[ConnectType],
    ) -> Response[ConnectType]:
        pass


class RequestMiddlewareType(Protocol):  # pragma: no cover
    async def __call__(
        self,
        make_request: NextRequestMiddlewareType[ConnectType],
        bot: "Bot",
        method: ConnectMethod[ConnectType],
    ) -> Response[ConnectType]:
        pass


class BaseRequestMiddleware(ABC):
    """
    Generic middleware class
    """

    @abstractmethod
    async def __call__(
        self,
        make_request: NextRequestMiddlewareType[ConnectType],
        bot: "Bot",
        method: ConnectMethod[ConnectType],
    ) -> Response[ConnectType]:
        """
        Execute middleware

        :param make_request: Wrapped make_request in middlewares chain
        :param bot: bot for request making
        :param method: Request method (Subclass of :class:`aio_connect.methods.base.ConnectMethod`)

        :return: :class:`aio_connect.methods.Response`
        """
        pass
