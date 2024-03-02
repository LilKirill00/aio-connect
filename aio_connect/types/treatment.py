from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from datetime import datetime
from ..types import UUID


class Treatment(ConnectObject):
    """
    Название объекта: Treatment
    Описание объекта: Обращение

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289322810/Treatment
    """

    treatment_id: UUID
    """ID обращения"""
    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    initialized_at: datetime
    """Дата начала обращения"""
    treatment_duration: Optional[int] = None
    """Общая длительность обращения, сек. (при закрытии)"""
    current_specialist: Optional[UUID] = None
    """ID назначенного специалиста, null когда нет назначенного специалиста"""
    quality: Optional[int] = None
    """Оценка качества работы специалиста"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            treatment_id: UUID,
            line_id: UUID,
            user_id: UUID,
            initialized_at: datetime,
            treatment_duration: Optional[int] = None,
            current_specialist: Optional[UUID] = None,
            quality: Optional[int] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                treatment_id=treatment_id,
                line_id=line_id,
                user_id=user_id,
                initialized_at=initialized_at,
                treatment_duration=treatment_duration,
                current_specialist=current_specialist,
                quality=quality,
                **__pydantic_kwargs,
            )


class Treatments(ConnectObject):
    """
    Название объекта: Treatments
    Описание объекта: Обращения

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492923941/Treatments
    """

    treatment_id: UUID
    """ID обращения"""
    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    initialized_at: datetime
    """Дата начала обращения"""
    treatment_duration: Optional[int] = None
    """Общая длительность обращения, сек. (при закрытии)"""
    current_specialist: Optional[UUID] = None
    """ID назначенного специалиста, null когда нет назначенного специалиста"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            treatment_id: UUID,
            line_id: UUID,
            user_id: UUID,
            initialized_at: datetime,
            treatment_duration: Optional[int] = None,
            current_specialist: Optional[UUID] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                treatment_id=treatment_id,
                line_id=line_id,
                user_id=user_id,
                initialized_at=initialized_at,
                treatment_duration=treatment_duration,
                current_specialist=current_specialist,
                **__pydantic_kwargs,
            )
