from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject
from ..types import UUID


class Call(ConnectObject):
    """
    Название объекта: Call
    Описание объекта: Звонок (голосовой вызов)

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1298628889/Call
    """

    src: UUID
    """ID инициатора"""
    dst: Optional[UUID] = None
    """ID адресата"""
    new_dst: Optional[UUID] = None
    """ID нового адресата (при перенаправлении вызова)"""
    billsec: Optional[int] = None
    """Длительность разговора, секунды"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            src: UUID,
            dst: Optional[UUID] = None,
            new_dst: Optional[UUID] = None,
            billsec: Optional[int] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                src=src,
                dst=dst,
                new_dst=new_dst,
                billsec=billsec,
                **__pydantic_kwargs,
            )
