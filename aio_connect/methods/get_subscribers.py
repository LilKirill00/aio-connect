from __future__ import annotations

from .base import ConnectMethod

from ..types import Users


class GetSubscribers(ConnectMethod[Users]):
    """
    Типы запросов: GET
    Описание: Получение информации о пользователях
    Название: GetSubscribers
    URL: /v1/line/subscribers/

    Метод возвращает информацию о пользователях
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2068938753/4.2.3.3.
    """

    __returning__ = Users
