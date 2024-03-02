from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from datetime import datetime
from ..types import UUID


class UserServiceLine(ConnectObject):
    """
    Название объекта: UserServiceLine
    Описание объекта: Линии, подключенные пользователям

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289322629/UserServiceLine
    """

    service_id: UUID
    """ID линии поддержки"""
    service_user_id: UUID
    """ID пользователя"""
    activate_date: datetime
    """Дата начала подписки"""
    expires_date: Optional[datetime] = None
    """Дата окончания подписки, null когда бессрочная подписка"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            service_id: UUID,
            service_user_id: UUID,
            activate_date: datetime,
            expires_date: Optional[datetime] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                service_id=service_id,
                service_user_id=service_user_id,
                activate_date=activate_date,
                expires_date=expires_date,
                **__pydantic_kwargs,
            )
