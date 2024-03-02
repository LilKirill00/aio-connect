from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aio_connect.types.base import ConnectObject

if TYPE_CHECKING:
    from .update import Update


class ErrorEvent(ConnectObject):
    """
    Internal event, should be used to receive errors while processing Updates from Connect
    """

    update: Update
    """Received update"""
    exception: Exception
    """Exception"""

    if TYPE_CHECKING:

        def __init__(
            __pydantic_self__, *, update: Update, exception: Exception, **__pydantic_kwargs: Any
        ) -> None:
            super().__init__(update=update, exception=exception, **__pydantic_kwargs)
