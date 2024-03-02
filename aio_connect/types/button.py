from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import MutableConnectObject


class Button(MutableConnectObject):
    """
    Название объекта: Button
    Описание объекта: Структура описывающаю кнопку в бот-меню.

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1357119519/4.3.2.1.+Button
    """

    id: Optional[str] = None
    """Идентификатор команды"""
    text: str
    """Название команды"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            id: Optional[str] = None,
            text: str,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                id=id,
                text=text,
                **__pydantic_kwargs,
            )
