from __future__ import annotations

from .base import ConnectMethod

from ..types import User


class GetSubscriber(ConnectMethod[User]):
    """
    Типы запросов: GET
    Описание: Получение информации о пользователе
    Название: GetSubscriber
    URL: /v1/line/subscriber/{user_id}/

    user_id: UUID = ID пользователя, являющегося получателем любой линии поддержки

    Метод возвращает информацию о пользователе
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289388228/4.2.3.2.
    """

    __returning__ = User
