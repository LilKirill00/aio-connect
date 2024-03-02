from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, List, Dict, Union

from .base import ConnectMethod
from ..types import UUID, InputFile


class SendImageLine(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Отправка картинки
    Название: SendImageLine
    URL: /v1/line/send/image/

    Метод позволяет отправить картинку в чат.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1492091047/4.3.1.6.
    """

    __returning__ = bool

    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    author_id: Optional[UUID] = None
    """ID автора (специалиста, от имени которого отправляется файл)"""
    file_name: str
    """Имя файла"""
    comment: Optional[str] = None
    "Комментарий к файлу"
    bot_as_spec: Optional[bool] = None
    """Флаг, при наличии которого не требуется получения ответов от пользователя (отправка клавиатуры запрещена),
    и может отсутствовать подписка на события с типом bot.
    Специалист, от лица которого отправляется файл (поле author_id), должен быть в онлайне и в статусе отличном от
    "Нет на месте" и "Не беспокоить", во избежании лишних переназначений или постановок пользователя в очередь
    ожидания специалиста.
    """
    notification_only: Optional[bool] = None
    """Флаг, при наличии которого не требуется получения ответов от пользователя (отправка клавиатуры запрещена),
    и может отсутствовать подписка на события с типом bot.
    Используется для информирования пользователя о событиях.
    Специалист, от лица которого отправляется сообщение (поле author_id), не становится назначенным. При отсутствии
    открытого обращения, новое не будет открыто.
    """
    keyboard: Optional[List[List[Dict[Any, str]]]] = None
    """Клавиатура"""

    file: Union[InputFile, str]
    """Картинка в виде:
        URLInputFile(url="{url_ссылка_на_картинку}")
        FSInputFile(path="{./путь_к_файлу}")
        BufferedInputFile(file={содержимое}, filename="{название_файла}")
    """

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: UUID,
            user_id: UUID,
            author_id: Optional[UUID] = None,
            file_name: str,
            comment: Optional[str] = None,
            bot_as_spec: Optional[bool] = None,
            notification_only: Optional[bool] = None,
            keyboard: Optional[List[List[Dict[Any, str]]]] = None,
            file: Union[InputFile, str],
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                user_id=user_id,
                author_id=author_id,
                file_name=file_name,
                comment=comment,
                bot_as_spec=bot_as_spec,
                notification_only=notification_only,
                keyboard=keyboard,
                file=file,
                **__pydantic_kwargs,
            )
