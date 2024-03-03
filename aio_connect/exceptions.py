from typing import Any, Optional

from .methods import ConnectMethod
from .methods.base import ConnectType


class AioconnectError(Exception):
    """
    Base exception for all Aio-connect errors.
    """


class DetailedAioconnectError(AioconnectError):
    """
    Base exception for all Aio-connect errors with detailed message.
    """

    url: Optional[str] = None

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        message = self.message
        if self.url:
            message += f"\n(background on this error at: {self.url})"
        return message

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self}')"


class UnsupportedKeywordArgument(DetailedAioconnectError):
    """
    Exception raised when a keyword argument is passed as filter.
    """


class ConnectAPIError(DetailedAioconnectError):
    """
    Base exception for all Connect API errors.
    """

    label: str = "Server says"

    def __init__(
        self,
        method: ConnectMethod[ConnectType],
        message: Optional[str]
    ) -> None:
        super().__init__(message=message)
        self.method = method

    def __str__(self) -> str:
        original_message = super().__str__()
        return f"{self.label} - {original_message}"


class ConnectNetworkError(ConnectAPIError):
    """
    Base exception for all Connect network errors.
    """

    label = "HTTP Client says"


class ConnectBadRequest(ConnectAPIError):
    """
    400 - Запрос содержит ошибку
    """


class ConnectUnauthorizedError(ConnectAPIError):
    """
    401 - Пользователь не авторизован
    """


class ConnectForbiddenError(ConnectAPIError):
    """
    403 - Недостаточно прав
    """


class ConnectNotFound(ConnectAPIError):
    """
    404 -
    """


class UnprocessalbleEntity(ConnectAPIError):
    """
    422 - Ошибка сервиса или запрос не прошел по требованиям
    """


class ConnectConflictError(ConnectAPIError):
    """
    409 -
    """


class ConnectServerError(ConnectAPIError):
    """
    Exception raised when Connect server returns 5xx error.
    """


class RestartingConnect(ConnectServerError):
    """
    Exception raised when Connect server is restarting.

    It seems like this error is not used by Connect anymore,
    but it's still here for backward compatibility.

    Currently, you should expect that Connect can raise RetryAfter (with timeout 5 seconds)
     error instead of this one.
    """


class ConnectEntityTooLarge(ConnectNetworkError):
    """
    Exception raised when you are trying to send a file that is too large.
    """


class ClientDecodeError(AioconnectError):
    """
    Exception raised when client can't decode response. (Malformed response, etc.)
    """

    def __init__(self, message: str, original: Exception, data: Any) -> None:
        self.message = message
        self.original = original
        self.data = data

    def __str__(self) -> str:
        original_type = type(self.original)
        return (
            f"{self.message}\n"
            f"Caused from error: "
            f"{original_type.__module__}.{original_type.__name__}: {self.original}\n"
            f"Content: {self.data}"
        )
