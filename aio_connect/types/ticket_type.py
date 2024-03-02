from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectObject

from ..types import UUID


class TicketType(ConnectObject):
    """
    Название объекта: TicketType
    Описание объекта: Типы заявок Service Desk

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492956693/TicketType
    """

    id: UUID
    """ID Типа заявок"""
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
