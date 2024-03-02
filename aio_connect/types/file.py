from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from ..types import UUID


class File(ConnectObject):
    """
    Название объекта: File
    Описание объекта: Файл

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289388485/File
    """

    file_id: UUID
    """ID файла"""
    file_path: str
    """Адрес для скачивания"""
    file_name: str
    """Имя файла"""
    file_size: int
    """Размер файла, байт"""
    comment: Optional[str] = None
    """Сопроводительное сообщение к файлу"""
    preview_link: Optional[str] = None
    """Ссылка на превью для переданного изображения"""
    preview_link_hi: Optional[str] = None
    """Ссылка на превью в высоком качестве для переданного изображения"""
    preview_hi_sizes: Optional[str] = None
    """Размер превью (ширинаxвысота) в высоком качестве для переданного изображения"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            file_id: UUID,
            file_path: str,
            file_name: str,
            file_size: int,
            comment: Optional[str] = None,
            preview_link: Optional[str] = None,
            preview_link_hi: Optional[str] = None,
            preview_hi_sizes: Optional[str] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                file_id=file_id,
                file_path=file_path,
                file_name=file_name,
                file_size=file_size,
                comment=comment,
                preview_link=preview_link,
                preview_link_hi=preview_link_hi,
                preview_hi_sizes=preview_hi_sizes,
                **__pydantic_kwargs,
            )
