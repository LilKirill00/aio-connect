from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from .base import ConnectMethod
from ..types import UUID, InputFile


class SendImageColleague(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Отправка картинку
    Название: SendImageColleague
    URL: /v1/colleague/send/image/

    Метод позволяет отправить картинку в чат сотруднику от имени другого сотрудника.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1492091064/4.3.1.10.
    """

    __returning__ = bool

    recepient_id: UUID
    """ID получателя"""
    author_id: UUID
    """ID автора (от чьего имени отправляется файл)"""
    file_name: str
    """Имя файла"""
    comment: Optional[str] = None
    "Комментарий к файлу"

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
            recepient_id: UUID,
            author_id: UUID,
            file_name: str,
            comment: Optional[str] = None,
            file: Union[InputFile, str],
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                recepient_id=recepient_id,
                author_id=author_id,
                file_name=file_name,
                comment=comment,
                file=file,
                **__pydantic_kwargs,
            )
