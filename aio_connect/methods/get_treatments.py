from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectMethod

from ..types import UUID, Treatments


class GetTreatments(ConnectMethod[Treatments]):
    """
    Типы запросов: GET
    Описание: Получение открытых обращений
    Название: GetTreatments
    URL: /v1/line/treatment/

    Метод возвращает список открытых обращений.
    Принимает два необязательных параметра line_id и user_id.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355600/4.2.3.1.
    """

    __returning__ = Treatments

    line_id: Optional[UUID] = None
    """ID линии поддержки"""
    user_id: Optional[UUID] = None
    """ID пользователя"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: Optional[UUID] = None,
            user_id: Optional[UUID] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                user_id=user_id,
                **__pydantic_kwargs,
            )
