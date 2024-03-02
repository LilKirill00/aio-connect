from __future__ import annotations

from .base import ConnectMethod


class DelAllHook(ConnectMethod[bool]):
    """
    Типы запросов: DELETE
    Описание: Удаление адресов всех webhook (кроме bot)
    Название: DelAllHook
    URL: /v1/hook/

    Метод удаляет адреса всех webhook (кроме bot).
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355653/4.2.1.2.
    """

    __returning__ = bool
