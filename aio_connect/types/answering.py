from __future__ import annotations

from typing import TYPE_CHECKING, Any, List

from .base import ConnectObject

from ..types import UUID


class Answering(ConnectObject):
    """
    Название объекта: Answering
    Описание объекта: Ответ на вопрос
    """

    question: str
    """Текст вопроса, на который пытался дать варианты"""
    request_id: UUID
    """ID запроса"""
    answers: List
    """Массив с вариантами ответов. Отсортированы по уровню уверенности"""
    id: UUID
    """ID статьи базы знаний"""
    text: str
    """Текст ответа"""
    accuracy: float
    """Уровень уверенности(max. 1.0 - 100 %)"""
    answer_source: str
    """База знаний, из которой получен ответ:
        GREETINGS - приветствия
        GOODBYES - прощания
        OURS - любая из ваших
    """

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            question: str,
            request_id: UUID,
            answers: List,
            id: UUID,
            text: str,
            accuracy: float,
            answer_source: str,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                question=question,
                request_id=request_id,
                answers=answers,
                id=id,
                text=text,
                accuracy=accuracy,
                answer_source=answer_source,
                **__pydantic_kwargs,
            )
