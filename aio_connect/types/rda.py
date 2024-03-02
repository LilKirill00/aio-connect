from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from ..types import UUID


class Rda(ConnectObject):
    """
    Название объекта: Rda
    Описание объекта: Сеанс удаленного доступа

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1304002561/Rda
    """

    src: UUID
    """ID инициатора"""
    dst: UUID
    """ID адресата"""
    duration: Optional[int] = None
    """Длительность сеанса, сек."""
    download_count: Optional[int] = None
    """Принятые файлы, шт."""
    upload_count: Optional[int] = None
    """Отправленные файлы, шт."""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            src: UUID,
            dst: UUID,
            duration: Optional[int] = None,
            download_count: Optional[int] = None,
            upload_count: Optional[int] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                src=src,
                dst=dst,
                duration=duration,
                download_count=download_count,
                upload_count=upload_count,
                **__pydantic_kwargs,
            )
