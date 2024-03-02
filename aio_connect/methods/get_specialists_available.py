from __future__ import annotations

from .base import ConnectMethod

from ..types import UUID
from typing import List


class GetSpecialistsAvailable(ConnectMethod[List[UUID]]):
    """
    Типы запросов: GET
    Описание: Получение специалистов в хорошем статусе по конкретной линии поддержки
    Название: GetSpecialistsAvailable
    URL: /v1/line/specialists/{line_id}/available/

    line_id: UUID = ID линии поддержки

    Метод возвращает id специалистов в статусе "Доступен" по конкретной линии поддержки
    Вызов метода позволяет узнать можно ли назначить специалиста на текущий момент методом
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2167472129/4.2.3.8.
    """

    __returning__ = List[UUID]
