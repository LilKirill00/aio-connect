from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectMethod

from ..types import Competences, UUID


class GetCompetences(ConnectMethod[Competences]):
    """
    Типы запросов: GET
    Описание: Получение списка компетенций специалистов
    Название: GetCompetences
    URL: /v1/line/competences/

    Метод возвращает список компетенций специалистов, с возможностью отфильтровать по специалисту и линии.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2490302465/4.2.3.9.
    """

    __returning__ = Competences

    user_id: Optional[UUID] = None
    """ID пользователя (специалиста)"""
    line_id: Optional[UUID] = None
    """ID линии поддержки"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            user_id: Optional[UUID] = None,
            line_id: Optional[UUID] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                user_id=user_id,
                line_id=line_id,
                **__pydantic_kwargs,
            )
