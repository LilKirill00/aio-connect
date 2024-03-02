from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectMethod

from ..types import UUID


class AppointSpec(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Попытаться назначить конкретного специалиста
    Название: AppointSpec
    URL: /v1/line/appoint/spec/

    Метод позволяет сделать попытку назначить конкретного специалиста.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1348632627/4.3.1.2.
    """

    __returning__ = bool

    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    spec_id: UUID
    """ID специалиста, на которого пытаемся назначить (должен быть в онлайне)"""
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
            spec_id: UUID,
            author_id: Optional[UUID] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                user_id=user_id,
                spec_id=spec_id,
                author_id=author_id,
                **__pydantic_kwargs,
            )
