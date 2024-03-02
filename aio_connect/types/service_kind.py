from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from ..types import UUID


class ServiceKind(ConnectObject):
    """
    Название объекта: ServiceKind
    Описание объекта: Виды работ Service Desk

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492956710/ServiceKind
    """

    id: UUID
    """ID Вида работ"""
    name: str
    """Название"""
    description: Optional[str] = None
    """Описание"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            id: UUID,
            name: str,
            description: Optional[str] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                id=id,
                name=name,
                description=description,
                **__pydantic_kwargs,
            )
