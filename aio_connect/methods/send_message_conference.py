from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectMethod

from ..types import UUID


class SendMessageConference(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Отправить сообщение в группу
    Название: SendMessageConference
    URL: /v1/conference/send/message/

    Метод позволяет отправить сообщение в группу от имени участника этой группы.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1479704633/4.3.1.11.
    """

    __returning__ = bool

    conference_id: UUID
    """ID группы"""
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
            conference_id: UUID,
            author_id: UUID,
            text: str,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                conference_id=conference_id,
                author_id=author_id,
                text=text,
                **__pydantic_kwargs,
            )
