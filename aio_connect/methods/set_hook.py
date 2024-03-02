from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectMethod

from ..types import UUID, HookType


class SetHook(ConnectMethod[bool]):
    """
    Типы запросов: POST
    Описание: Выставление адреса webhook
    Название: SetHook
    URL: /v1/hook/

    Метод устанавливает webhook для получения событий.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289388306/4.2.1.1.
    """

    __returning__ = bool

    url: str
    """URL WebHook. На этот адрес будут прилетать все события POST-запросами."""
    type: HookType
    """
    Тип подписки:
        - bot - на события для чат бота для указанной линии поддержки (обязателен id)
        - line - все события по линии(ям) поддержки
    """
    id: Optional[UUID] = None
    """
    ID объекта, на который осуществляется подписка:
        ID линии поддержки
        если type == line и не указан id, то подписка производится на все линии, к которым имеется доступ
    """

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            url: str,
            type: HookType,
            id: Optional[UUID] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                url=url,
                type=type,
                id=id,
                **__pydantic_kwargs,
            )
