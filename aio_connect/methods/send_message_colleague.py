from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectMethod

from ..types import UUID


class SendMessageColleague(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Отправить сообщение в чат сотруднику
    Название: SendMessageColleague
    URL: /v1/colleague/send/message/

    Метод позволяет отправить сообщение в чат сотруднику от лица другого сотрудника.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1479737345/4.3.1.8.
    """

    __returning__ = bool

    recepient_id: UUID
    """ID получателя"""
    author_id: UUID
    """ID автора(от чьего имени отправляется сообщение)"""
    text: str
    """Текст сообщения"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            recepient_id: UUID,
            author_id: UUID,
            text: str,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                recepient_id=recepient_id,
                author_id=author_id,
                text=text,
                **__pydantic_kwargs,
            )
