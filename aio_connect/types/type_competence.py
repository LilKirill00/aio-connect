from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectObject
from ..enums import ContentType

from ..types import Competence


class TypeCompetence(ConnectObject):
    """
    Дополнительные данные в сообщении:

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1357021196/4.2.2.2.1.+competence
    """

    action: str
    """Тип изменения объектов:
        add
        update
        delete
    """
    competence: Competence
    """Описание компетенции"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            action: str,
            competence: Competence,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                action=action,
                competence=competence,
                **__pydantic_kwargs,
            )

    @property
    def content_type(self) -> str:

        if self.action:
            return ContentType.ACTION
        if self.competence:
            return ContentType.COMPETENCE

        return ContentType.UNKNOWN
