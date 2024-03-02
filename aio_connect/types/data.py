from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from ..types import UUID


class Data(ConnectObject):
    """
    Название объекта: Data
    Описание объекта: Дополнительные данные

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1487241255/Data
    """

    redirect: Optional[str] = None
    """Дополнительные данные перевода на бота"""
    direction: Optional[str] = None
    """Направления перевода обращения
        from - откуда
        to - куда
        to_fran - перевод в компанию франа
        to_vendor - перевод в компанию вендора
    """
    line_id: Optional[UUID] = None
    """ID линии поддержки при direction:
        from - ID исходной линии поддержки
        to - ID линии поддержки назначения
    """
    treatment_id: Optional[UUID] = None
    """ID обращения при direction:
        from - ID исходного обращения
        to - ID нового обращения
    """
    company_id: Optional[UUID] = None
    """ID компании при direction:
         to_fran - франа
         to_vendor - вендора
    """

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            redirect: Optional[str] = None,
            direction: Optional[str] = None,
            line_id: Optional[UUID] = None,
            treatment_id: Optional[UUID] = None,
            company_id: Optional[UUID] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                redirect=redirect,
                direction=direction,
                line_id=line_id,
                treatment_id=treatment_id,
                company_id=company_id,
                **__pydantic_kwargs,
            )
