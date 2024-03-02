from __future__ import annotations

from typing import Optional, TYPE_CHECKING, Any

from .base import ConnectMethod

from ..types import Subscriptions, UUID


class GetSubscriptions(ConnectMethod[Subscriptions]):
    """
    Типы запросов: GET
    Описание: Получение списка линий, подключенных пользователям
    Название: GetSubscriptions
    URL: /v1/line/subscriptions/

    user_id: Optional[UUID] = ID пользователя
    client_id: Optional[UUID] = ID клинта
    line_id: Optional[UUID] = ID линии поддержки

    Метод возвращает информацию о получаемым линиям пользователями,
        с возможностью отфильтровать по пользователю, линии или клиенту.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2322923521/4.2.3.4.
    """

    __returning__ = Subscriptions

    user_id: Optional[UUID] = None
    """ID пользователя"""
    client_id: Optional[UUID] = None
    """ID клиента"""
    line_id: Optional[UUID] = None
    """ID линии поддержки"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
                __pydantic__self__,
                *,
                user_id: Optional[UUID] = None,
                client_id: Optional[UUID] = None,
                line_id: Optional[UUID] = None,
                **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                user_id=user_id,
                client_id=client_id,
                line_id=line_id,
                **__pydantic_kwargs,
            )
