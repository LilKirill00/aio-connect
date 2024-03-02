from __future__ import annotations

from .base import ConnectMethod

from ..types import TicketShort


class GetTicketByNumber(ConnectMethod[TicketShort]):
    """
    Типы запросов: GET
    Описание: Получение заявки Service Desk со вложенными объектами по номеру
    Название: GetTicketByNumber
    URL: /v1/ticket/number/{number}/

    number: int = № заявки

    Метод возвращает заявку Service Desk со вложенными объектами по номеру
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492923976/4.2.3.10.+Service+Desk+ID
    """

    __returning__ = TicketShort
