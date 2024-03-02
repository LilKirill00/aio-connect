from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectObject

from ..types import UUID


class Competence(ConnectObject):
    """
    Название объекта: Competence
    Описание объекта: Компетенция

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289322615/Competence
    """

    line_id: UUID
    """ID линии поддержки"""
    specialist_id: UUID
    """ID пользователя"""
    pool_priority: int
    """
    Приоритет специалиста:
        0 - наблюдатель
        1 - высокий
        2 - средний
        3 - стандартный
    """
    is_franch_spec: bool
    """Является ли специалистом франа"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: UUID,
            specialist_id: UUID,
            pool_priority: int,
            is_franch_spec: bool,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                specialist_id=specialist_id,
                pool_priority=pool_priority,
                is_franch_spec=is_franch_spec,
                **__pydantic_kwargs,
            )


class Competences(Competence):
    """
    Название объекта: Competences
    Описание объекта: Компетенции

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2490695681/Competences

    Данные: Такие же как у Competence
    """
