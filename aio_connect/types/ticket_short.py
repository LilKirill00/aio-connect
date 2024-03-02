from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from datetime import datetime
from ..types import (
    UUID,
    ServiceKind,
    LineShort,
    TicketType,
    TicketChannel,
    TicketStatus,
    User,
    TicketAdditionalFieldValue
)


class TicketShort(ConnectObject):
    """
    Название объекта: TicketShort
    Описание объекта: Заявка Service Desk (краткие сведения)

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492923959/TicketShort
    """

    id: UUID
    """ID Заявки"""
    transaction_id: UUID
    """ID Транзакции"""
    number: int
    """Номер заявки"""
    created_at: datetime
    """Время создания"""
    updated_at: datetime
    """Время изменения"""
    description: Optional[str] = None
    """Описание"""
    priority: str
    """Приоритет:
        LOW - низкий
        STANDARD - Стандартный
        HIGH - Высокий
    """
    duration: int
    """Длительность работы, сек (0 - не задано)"""
    result: Optional[str] = None
    """Описание решения"""
    summary: Optional[str] = None
    """Тема"""
    deadline: Optional[str] = None
    """Срок"""
    kind: ServiceKind
    """Вид работ"""
    line: LineShort
    """Линия поддержки"""
    type: TicketType
    """Тип заявки"""
    channel: TicketChannel
    """Канал связи"""
    status: TicketStatus
    """Статус заявоки"""
    initiator: User
    """Заказчик"""
    author: Optional[User] = None
    """Автор(отсутствует, если заявка создана в учетной системе)"""
    executor: Optional[User] = None
    """Исполнитель"""
    fields: Optional[TicketAdditionalFieldValue] = None
    """Значения дополнительных полей заявки"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            id: UUID,
            transaction_id: UUID,
            number: int,
            created_at: datetime,
            updated_at: datetime,
            description: Optional[str] = None,
            priority: str,
            duration: int,
            result: Optional[str] = None,
            summary: Optional[str] = None,
            deadline: Optional[str] = None,
            kind: ServiceKind,
            line: LineShort,
            type: TicketType,
            channel: TicketChannel,
            status: TicketStatus,
            initiator: User,
            author: Optional[User] = None,
            executor: Optional[User] = None,
            fields: Optional[TicketAdditionalFieldValue] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                id=id,
                transaction_id=transaction_id,
                number=number,
                created_at=created_at,
                updated_at=updated_at,
                description=description,
                priority=priority,
                duration=duration,
                result=result,
                summary=summary,
                deadline=deadline,
                kind=kind,
                line=line,
                type=type,
                channel=channel,
                status=status,
                initiator=initiator,
                author=author,
                executor=executor,
                fields=fields,
                **__pydantic_kwargs,
            )
