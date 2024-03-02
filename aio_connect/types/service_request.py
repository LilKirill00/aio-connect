from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from datetime import datetime
from ..types import UUID


class ServiceRequest(ConnectObject):
    """
    Название объекта: ServiceRequest
    Описание объекта: Заявка Service Desk

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1302888526/ServiceRequest
    """

    request_id: UUID
    """ID Заявки"""
    number: str
    """Номер заявки"""
    created_at: datetime
    """Время создания UTC"""
    channel_id: UUID
    """ID Канала связи"""
    line_id: UUID
    """ID Линии поддержки"""
    initiator_id: UUID
    """ID Пользователя инициатора"""
    executor_id: UUID
    """ID Пользователя исполнителя"""
    status_id: UUID
    """ID Текущая стадия заявки"""
    kind_id: UUID
    """ID Вида услуг"""
    type_id: UUID
    """ID Типа заявок"""
    description: Optional[str] = None
    """Описание заявки"""
    result: Optional[str] = None
    """Описание решения"""
    transaction_id: UUID
    """ID транзакции"""
    updated_at: Optional[datetime] = None
    """Время обновления UTC"""
    duration: Optional[int] = None
    """Длительность работы, сек."""
    summary: Optional[str] = None
    """Тема"""
    priority: Optional[str] = None
    """
    Приоритет. Значения:
        LOW
        STANDARD
        HIGH
    """
    deadline: Optional[str] = None
    """Cрок исполнения"""
    field1: Optional[str] = None
    """Дополнительное настраиваемое поле"""
    field2: Optional[str] = None
    """Дополнительное настраиваемое поле"""
    field3: Optional[str] = None
    """Дополнительное настраиваемое поле"""
    field4: Optional[str] = None
    """Дополнительное настраиваемое поле"""
    field5: Optional[str] = None
    """Дополнительное настраиваемое поле"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            request_id: UUID,
            number: str,
            created_at: datetime,
            channel_id: UUID,
            line_id: UUID,
            initiator_id: UUID,
            executor_id: UUID,
            status_id: UUID,
            kind_id: UUID,
            type_id: UUID,
            description: Optional[str] = None,
            result: Optional[str] = None,
            transaction_id: UUID,
            updated_at: Optional[datetime] = None,
            duration: Optional[int] = None,
            summary: Optional[str] = None,
            priority: Optional[str] = None,
            deadline: Optional[str] = None,
            field1: Optional[str] = None,
            field2: Optional[str] = None,
            field3: Optional[str] = None,
            field4: Optional[str] = None,
            field5: Optional[str] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                request_id=request_id,
                number=number,
                created_at=created_at,
                channel_id=channel_id,
                line_id=line_id,
                initiator_id=initiator_id,
                executor_id=executor_id,
                status_id=status_id,
                kind_id=kind_id,
                type_id=type_id,
                description=description,
                result=result,
                transaction_id=transaction_id,
                updated_at=updated_at,
                duration=duration,
                summary=summary,
                priority=priority,
                deadline=deadline,
                field1=field1,
                field2=field2,
                field3=field3,
                field4=field4,
                field5=field5,
                **__pydantic_kwargs,
            )
