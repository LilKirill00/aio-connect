from __future__ import annotations

from .base import ConnectMethod

from ..types import Lines


class GetLines(ConnectMethod[Lines]):
    """
    Типы запросов: GET
    Описание: Получение доступных линий поддержки
    Название: GetLines
    URL: /v1/line/

    Метод возвращает список линий поддержки.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2156429313/4.2.3.5.
    """

    __returning__ = Lines
