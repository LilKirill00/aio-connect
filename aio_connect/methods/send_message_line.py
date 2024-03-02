from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, List

from .base import ConnectMethod

from ..types import UUID, Button


class SendMessageLine(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Отправить сообщение в чат
    Название: SendMessageLine
    URL: /v1/line/send/message/

    Метод позволяет отправить сообщение в чат.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355725/4.3.1.4.
    """

    __returning__ = bool

    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    author_id: Optional[UUID] = None
    """ID автора(специалиста, от имени которого отправляется сообщение)"""
    text: str
    """Текст сообщения"""
    bot_as_spec: Optional[bool] = None
    """ Флаг, при наличии которого не требуется получения ответов от пользователя (отправка клавиатуры запрещена),
    и может отсутствовать подписка на события с типом bot.
    Специалист, от лица которого отправляется сообщение (поле author_id),
    должен быть в онлайне и в статусе отличном от "Нет на месте" и "Не беспокоить",
    во избежании лишних переназначений или постановок пользователя в очередь ожидания специалиста.
    """
    notification_only: Optional[bool] = None
    """Флаг, при наличии которого не требуется получения ответов от пользователя (отправка клавиатуры запрещена),
    и может отсутствовать подписка на события с типом bot. Используется для информирования пользователя о событиях.
    Специалист, от лица которого отправляется сообщение (поле author_id), не становится назначенным.
    При отсутствии открытого обращения, новое не будет открыто.
    """
    keyboard: Optional[List[List[Button]]] = None
    """Клавиатура"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: UUID,
            user_id: UUID,
            author_id: Optional[UUID] = None,
            text: str,
            bot_as_spec: Optional[bool] = None,
            notification_only: Optional[bool] = None,
            keyboard: Optional[List[List[Button]]] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                user_id=user_id,
                author_id=author_id,
                text=text,
                bot_as_spec=bot_as_spec,
                notification_only=notification_only,
                keyboard=keyboard,
                **__pydantic_kwargs,
            )
