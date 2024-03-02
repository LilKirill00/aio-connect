from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from ..types import UUID


class Line(ConnectObject):
    """
    Название объекта: Line
    Описание объекта: Линия поддержки

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289420955/Line
    """

    line_id: UUID
    """ID линии поддержки"""
    name: str
    """Название"""
    allow_bot: bool
    """Дано разрешение на использование цифрового меню"""
    hook_bot: Optional[str] = None
    """Адрес, на который выставлен hook с типом bot"""
    hook_line: Optional[str] = None
    """Адрес, на который выставлен hook с типом line"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: UUID,
            name: str,
            allow_bot: bool,
            hook_bot: Optional[str] = None,
            hook_line: Optional[str] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                name=name,
                allow_bot=allow_bot,
                hook_bot=hook_bot,
                hook_line=hook_line,
                **__pydantic_kwargs,
            )


class LineShort(ConnectObject):
    """
    Название объекта: LineShort
    Описание объекта: Линия поддержки (краткие сведения)

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2493218817/LineShort
    """

    id: UUID
    """ID линии поддержки"""
    name: str
    """Название"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            id: UUID,
            name: str,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                id=id,
                name=name,
                **__pydantic_kwargs,
            )


class Lines(Line):
    """
    Название объекта: Lines
    Описание объекта: Линии поддержки

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2156429325/Lines

    Данные: Такие же как у Line
    """
