from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectObject

from ..types import UUID


class TicketStatus(ConnectObject):
    """
    Название объекта: TicketStatus
    Описание объекта: Статусы заявок Service Desk

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492923906/TicketStatus
    """

    id: UUID
    """ID Статуса заявки"""
    name: str
    """Название"""
    type: str
    """Тип:
        NEW - Новая
        WORK - Выполняется
        VALIDATION - Валидация
        CONFIRMED - Подтверждена
        REJECTED - Отклонена
        SUSPENDED - Приостановлена
        FINISHED - Завершена
        CANCELLED - Отменена
    """

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            id: UUID,
            name: str,
            type: str,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                id=id,
                name=name,
                type=type,
                **__pydantic_kwargs,
            )
