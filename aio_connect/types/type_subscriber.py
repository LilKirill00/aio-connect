from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectObject
from ..enums import ContentType

from ..types import User


class TypeSubscriber(ConnectObject):
    """
    Дополнительные данные в сообщении:

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1357119489/4.2.2.2.3.+subscriber
    """

    action: str
    """Тип изменения объектов:
        add
        update
        delete
    """
    user: User
    """Описание пользователя"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            action: str,
            user: User,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                action=action,
                user=user,
                **__pydantic_kwargs,
            )

    @property
    def content_type(self) -> str:

        if self.action:
            return ContentType.ACTION
        if self.user:
            return ContentType.USER

        return ContentType.UNKNOWN
