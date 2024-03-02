from __future__ import annotations

from .base import ConnectMethod

from ..types import TicketShort


class GetTicket(ConnectMethod[TicketShort]):
    """
    Типы запросов: GET
    Описание: Получение заявки Service Desk со вложенными объектами по id
    Название: GetTicket
    URL: /v1/ticket/{id}/

    id: UUID = ID заявки

    Метод возвращает заявку Service Desk со вложенными объектами по id
    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492923976/4.2.3.10.+Service+Desk+ID
    """

    __returning__ = TicketShort
