from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from ..types import UUID


class PartnerNotification(ConnectObject):
    """
    Название объекта: PartnerNotification
    Описание объекта: Рассылка

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2459074561/PartnerNotification
    """

    id: UUID
    """ID рассылки"""
    theme: str
    """Тема"""
    text: str
    """
    Текст рассылки с параметрами замены:
        <Фамилия>
        <Имя>
        <Отчество>
        <ДатаРождения>
        <Логин>
        <Должность>
        <Телефон>
        <EMail>
        <НазваниеКомпании>
        <ИННКомпании>
        <РегионКомпании>
    """
    description_hint: Optional[str] = None
    """Текст на кнопке"""
    description_url: Optional[str] = None
    """Ссылка, открываемая по кнопке. Так же как и text могут быть параметры."""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            id: UUID,
            theme: str,
            text: str,
            description_hint: Optional[str] = None,
            description_url: Optional[str] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                id=id,
                theme=theme,
                text=text,
                description_hint=description_hint,
                description_url=description_url,
                **__pydantic_kwargs,
            )
