from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .base import ConnectMethod

from ..types import UUID, Answering


class QuestionAndAnswering(ConnectMethod[Answering]):
    """
    Типы запросов: POST
    Описание: Получение подсказок
    Название: QuestionAndAnswering
    URL: /v1/line/qna/

    Метод позволяет получить варианты ответов на вопрос пользователя в базе знаний.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1481932813/4.3.1.14.
    """

    __returning__ = Answering

    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    skip_greetings: bool
    """Не использовать “Единая база приветствий и поддержки диалогов“"""
    skip_goodbyes: bool
    """Не использовать “Единая база завершения диалогов“"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            line_id: UUID,
            user_id: UUID,
            skip_greetings: bool,
            skip_goodbyes: bool,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                line_id=line_id,
                user_id=user_id,
                skip_greetings=skip_greetings,
                skip_goodbyes=skip_goodbyes,
                **__pydantic_kwargs,
            )


class QuestionAndAnsweringSelected(ConnectMethod[bool]):
    """
    Типы запросов: PUT
    Описание: Получение подсказок
    Название: QuestionAndAnsweringSelected
    URL: /v1/line/qna/selected/

    Метод позволяет отметить конкретную подсказку выбранной
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2290024449
    """

    __returning__ = bool

    request_id: UUID
    """ID запроса"""
    result_id: UUID
    """ID выбранной статьи"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            request_id: UUID,
            result_id: UUID,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                request_id=request_id,
                result_id=result_id,
                **__pydantic_kwargs,
            )
