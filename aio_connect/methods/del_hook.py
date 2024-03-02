from __future__ import annotations

from .base import ConnectMethod


class DelHook(ConnectMethod[bool]):
    """
    Типы запросов: DELETE
    Описание: Удаление адреса конкретного webhook
    Название: DelHook
    URL: /v1/hook/{type}/{id}/

    id: str = ID объекта
    type: str = Тип WebHook
                - bot - на события для чат бота
                - line - все события по линии(ям) поддержки

    Метод удаляет адрес конкретного webhook.
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355682/4.2.1.3.
    """

    __returning__ = bool
