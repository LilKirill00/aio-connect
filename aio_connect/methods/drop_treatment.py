from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectMethod

from ..types import UUID


class DropTreatment(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Закрыть текущее обращение
    Название: DropTreatment
    URL: /v1/line/drop/treatment/

    Метод позволяет закрыть текущее обращение.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1347551359/4.3.1.3.
    """

    __returning__ = bool

    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    author_id: Optional[UUID] = None
    """ID автора (специалиста, от имени которого производится действие)"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: UUID,
            user_id: UUID,
            author_id: Optional[UUID] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                user_id=user_id,
                author_id=author_id,
                **__pydantic_kwargs,
            )
