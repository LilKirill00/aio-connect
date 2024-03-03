from __future__ import annotations

import abc
import datetime
import json
import secrets
from enum import Enum
from http import HTTPStatus
from types import TracebackType
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Callable,
    Dict,
    Final,
    Optional,
    Type,
    cast,
)

from pydantic import ValidationError

from ...exceptions import (
    ClientDecodeError,
    RestartingConnect,
    ConnectAPIError,
    ConnectBadRequest,
    ConnectConflictError,
    ConnectEntityTooLarge,
    ConnectForbiddenError,
    ConnectNotFound,
    ConnectServerError,
    ConnectUnauthorizedError, UnprocessalbleEntity,
)

from .middlewares.manager import RequestMiddlewareManager
from ...methods import Response, ConnectMethod
from ...methods.base import ConnectType
from ...types import InputFile

if TYPE_CHECKING:
    from ..bot import Bot

_JsonLoads = Callable[..., Any]
_JsonDumps = Callable[..., str]

DEFAULT_TIMEOUT: Final[float] = 60.0


class BaseSession(abc.ABC):
    """
    This is base class for all HTTP sessions in aio-connect.

    If you want to create your own session, you must inherit from this class.
    """

    def __init__(
        self,
        json_loads: _JsonLoads = json.loads,
        json_dumps: _JsonDumps = json.dumps,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        """

        :param json_loads: JSON loader
        :param json_dumps: JSON dumper
        :param timeout: Session scope request timeout
        """
        self.json_loads = json_loads
        self.json_dumps = json_dumps
        self.timeout = timeout

        self.middleware = RequestMiddlewareManager()

    def check_response(
        self, bot: Bot, method: ConnectMethod[ConnectType], status_code: int, content: str
    ) -> Response[Any]:
        """
        Check response status
        """
        try:
            json_data = {'ok': False, 'result': False, 'error_code': None}
            if status_code == HTTPStatus.OK:
                json_data['ok'] = True
                json_data['result'] = True
            else:
                json_data['error_code'] = status_code
            if content:
                json_data['result'] = self.json_loads(content)
        except Exception as e:
            # Handled error type can't be classified as specific error
            # in due to decoder can be customized and raise any exception
            raise ClientDecodeError("Failed to decode object", e, content)

        try:
            response_type = Response[Any]  # type: ignore
            response = response_type.model_validate(json_data, context={"bot": bot})
        except ValidationError as e:
            raise ClientDecodeError("Failed to deserialize object", e, json_data)

        if HTTPStatus.OK <= status_code <= HTTPStatus.IM_USED and response.ok:
            return response

        result = cast(str, response.result)

        if status_code == HTTPStatus.BAD_REQUEST:
            raise ConnectBadRequest(method=method, message=result)
        if status_code == HTTPStatus.NOT_FOUND:
            raise ConnectNotFound(method=method, message=result)
        if status_code == HTTPStatus.CONFLICT:
            raise ConnectConflictError(method=method, message=result)
        if status_code == HTTPStatus.UNAUTHORIZED:
            raise ConnectUnauthorizedError(method=method, message=result)
        if status_code == HTTPStatus.FORBIDDEN:
            raise ConnectForbiddenError(method=method, message=result)
        if status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            raise UnprocessalbleEntity(method=method, message=result)
        if status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
            raise ConnectEntityTooLarge(method=method, message=result)
        if status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
            if "restart" in result:
                raise RestartingConnect(method=method, message=result)
            raise ConnectServerError(method=method, message=result)

        raise ConnectAPIError(
            method=method,
            message=result,
        )

    @abc.abstractmethod
    async def close(self) -> None:  # pragma: no cover
        """
        Close client session
        """
        pass

    @abc.abstractmethod
    async def make_request(
        self,
        bot: Bot,
        method: ConnectMethod[ConnectType],
        type_request: str,
        path: str,
        timeout: Optional[int] = None,
    ) -> ConnectType:  # pragma: no cover
        """
        Make request to Connect Bot API

        :param bot: Bot instance
        :param method: Method instance
        :param type_request: Тип запроса
        :param path: URL
        :param timeout: Request timeout
        :return:
        :raise ConnectApiError:
        """
        pass

    @abc.abstractmethod
    async def stream_content(
        self,
        url: str,
        headers: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
        chunk_size: int = 65536,
        raise_for_status: bool = True,
    ) -> AsyncGenerator[bytes, None]:  # pragma: no cover
        """
        Stream reader
        """
        yield b""

    def prepare_value(
        self,
        value: Any,
        bot: Bot,
        files: Dict[str, Any],
        _dumps_json: bool = True,
    ) -> Any:
        """
        Prepare value before send
        """
        if value is None:
            return None
        if isinstance(value, str):
            return value
        if isinstance(value, InputFile):
            key = secrets.token_urlsafe(10)
            files[key] = value
            return f"attach://{key}"
        if isinstance(value, dict):
            value = {
                key: prepared_item
                for key, item in value.items()
                if (
                    prepared_item := self.prepare_value(
                        item, bot=bot, files=files, _dumps_json=False
                    )
                )
                is not None
            }
            if _dumps_json:
                return self.json_dumps(value)
            return value
        if isinstance(value, list):
            value = [
                prepared_item
                for item in value
                if (
                    prepared_item := self.prepare_value(
                        item, bot=bot, files=files, _dumps_json=False
                    )
                )
                is not None
            ]
            if _dumps_json:
                return self.json_dumps(value)
            return value
        if isinstance(value, datetime.timedelta):
            now = datetime.datetime.now()
            return str(round((now + value).timestamp()))
        if isinstance(value, datetime.datetime):
            return str(round(value.timestamp()))
        if isinstance(value, Enum):
            return self.prepare_value(value.value, bot=bot, files=files)

        if _dumps_json:
            return self.json_dumps(value)
        return value

    async def __call__(
        self,
        bot: Bot,
        method: ConnectMethod[ConnectType],
        type_request: str,
        path: str,
        timeout: Optional[int] = None
    ) -> ConnectType:
        middleware = self.middleware.wrap_middlewares(self.make_request, timeout=timeout,
                                                      type_request=type_request, path=path)
        return cast(ConnectType, await middleware(bot, method))

    async def __aenter__(self) -> BaseSession:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.close()
