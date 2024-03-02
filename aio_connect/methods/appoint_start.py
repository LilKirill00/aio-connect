from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectMethod

from ..types import UUID


class AppointStart(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Назначить любого свободного специалиста
    Название: AppointStart
    URL: /v1/line/appoint/start/

    Метод Метод позволяет назначить любого свободного специалиста.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1348632607/4.3.1.1.
    """

    __returning__ = bool

    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: UUID,
            user_id: UUID,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                user_id=user_id,
                **__pydantic_kwargs,
            )
