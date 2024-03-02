from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from datetime import datetime
from ..types import UUID


class Subscriptions(ConnectObject):
    """
    Название объекта: Subscriptions
    Описание объекта: Линии, подключенные пользователям

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2322923533/Subscriptions
    """

    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    subscription_set: datetime
    """Дата начала подписки"""
    subscription_expire_at: Optional[datetime] = None
    """Дата окончания подписки, null когда бессрочная подписка"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: UUID,
            user_id: UUID,
            subscription_set: datetime,
            subscription_expire_at: Optional[datetime] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                user_id=user_id,
                subscription_set=subscription_set,
                subscription_expire_at=subscription_expire_at,
                **__pydantic_kwargs,
            )
