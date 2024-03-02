from __future__ import annotations

from .base import ConnectMethod

from ..types import User


class GetSpecialist(ConnectMethod[User]):
    """
    Типы запросов: GET
    Описание: Получение информации о специалисте
    Название: GetSpecialist
    URL: /v1/line/specialist/{user_id}/

    user_id: UUID = ID пользователя, являющегося специалистом по любой линии поддержки

    Метод возвращает информацию о специалисте
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289421100/4.2.3.6.
    """

    __returning__ = User
