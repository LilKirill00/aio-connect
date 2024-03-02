from __future__ import annotations

from .base import ConnectMethod

from ..types import Users


class GetSpecialists(ConnectMethod[Users]):
    """
    Типы запросов: GET
    Описание: Получение информации о специалистах
    Название: GetSpecialists
    URL: /v1/line/specialists/

    Метод возвращает информацию о специалистах
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2167373825/4.2.3.7.
    """

    __returning__ = Users
