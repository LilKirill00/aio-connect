from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectObject


class TicketAdditionalFieldValue(ConnectObject):
    """
    Название объекта: TicketAdditionalFieldValue
    Описание объекта: Дополнительное поле заявки Service Desk

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492923923/TicketAdditionalFieldValue
    """

    id: str
    """Идентификатор поля:
        FIELD1 - Первое
        FIELD2 - Второе
        FIELD3 - Третье
        FIELD4 - Четвертое
    """
    value: str
    """Значение поля"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            id: str,
            value: str,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                id=id,
                value=value,
                **__pydantic_kwargs,
            )
