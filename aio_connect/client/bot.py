from __future__ import annotations

import aiohttp

import pathlib
from contextlib import asynccontextmanager
from typing import (
    Any,
    AsyncIterator,
    List,
    Optional,
    TypeVar,
    Union,
    Dict,
    Literal
)

from ..methods import (
    ConnectMethod,
    # 4.2.1 Команды к механизму трансляции
    SetHook,
    DelAllHook,
    DelHook,
    # 4.2.3 Команды для уточнения информации
    GetTreatments,
    GetSubscriber,
    GetSubscribers,
    GetSubscriptions,
    GetLines,
    GetSpecialist,
    GetSpecialists,
    GetSpecialistsAvailable,
    GetCompetences,
    GetTicket,
    GetTicketByNumber,
    # 4.3.1. Команды внешних ботов
    AppointStart,
    AppointSpec,
    DropTreatment,
    SendMessageLine,
    SendFileLine,
    SendImageLine,
    DropKeyboard,
    SendMessageColleague,
    SendFileCollegue,
    SendImageColleague,
    SendMessageConference,
    SendFileConference,
    SendImageConference,
    QuestionAndAnswering, QuestionAndAnsweringSelected,
)
from ..types import (
    InputFile,
    UUID, is_valid_uuid,
    Answering,
    HookType,
    # 4.2.2.1. Объекты
    Competences,
    Subscriptions,
    User, Users,
    Lines,
    Treatments,
    TicketShort,
    # 4.3.2. Структуры данных для ботов
    Button,
)
from .session.aiohttp import AiohttpSession
from .session.base import BaseSession

T = TypeVar("T")


class Bot:
    def __init__(
        self,
        api_login: str,
        api_password: str,
        line_id: str,
        base: str,

        session: Optional[BaseSession] = None,
    ) -> None:
        """
        Bot class

        :param api_login:
        :param api_password:
        :param line_id:
        :param base: API server
        """

        if api_login and api_password:
            self.auth = aiohttp.BasicAuth(login=api_login, password=api_password)

        if session is None:
            session = AiohttpSession()

        self.api_login = api_login
        self.api_password = api_password
        self.line_id = line_id
        self.base = base
        self.session = session

    @asynccontextmanager
    async def context(self, auto_close: bool = True) -> AsyncIterator[Bot]:
        """
        Generate bot context

        :param auto_close: close session on exit
        :return:
        """
        try:
            yield self
        finally:
            if auto_close:
                await self.session.close()

    async def __call__(
        self,
        method: ConnectMethod[T],
        type_request: Literal["POST", "GET", "DELETE", "PUT", "POST-With-Attach"],
        path: str,
        request_timeout: Optional[int] = None
    ) -> T:
        """
        Call API method

        :param method:
        :param type_request: тип запроса
        :param path: URL после обращения к API
        :return:
        """
        return await self.session(self, method, timeout=request_timeout, type_request=type_request, path=path)

    async def download_file(
        self,
        file_path: str,
        destination: Union[pathlib.Path, str],
        timeout: int = 30,
    ) -> bool:
        """
        Download file by file_path to destination.

        :param file_path: Ссылка на скачивание
        :param destination: Путь и (или) имя файла
        :param timeout: Total timeout in seconds, defaults to 30
        """

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    auth=self.auth, url=file_path, timeout=timeout if timeout is None else timeout
            ) as resp:
                if resp.status == 200:
                    content = await resp.read()
                    with open(destination, 'wb') as file:
                        file.write(content)
                    return True
                else:
                    print(f'Ошибка скачивания файла. Код статуса: {resp.status}')
        return False

    """
    4.2.1 Команды к механизму трансляции

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1349812242/4.2.1.
    """

    async def set_hook(
        self,
        url: str,
        type: HookType,
        id: Optional[UUID] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод устанавливает webhook для получения событий.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289388306/4.2.1.1.

        :param url: URL WebHook. На этот адрес будут прилетать все события POST-запросами.
        :param type: Тип подписки: bot (на события для чат бота для указанной линии поддержки (обязателен id)),
            line (все события по линии(ям) поддержки)
        :param id: ID объекта, на который осуществляется подписка: ID линии поддержки,
            если type == line и не указан id, то подписка производится на все линии, к которым имеется доступ
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SetHook(
            url=url,
            type=type,
            id=is_valid_uuid(id),
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/hook/")

    async def del_all_hook(
        self,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод удаляет адреса всех webhook (кроме bot).

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355653/4.2.1.2.

        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = DelAllHook()
        return await self(call, request_timeout=request_timeout,
                          type_request="DELETE", path="/v1/hook/")

    async def del_hook(
        self,
        id: UUID,
        type: str,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод удаляет адрес конкретного webhook.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355682/4.2.1.3.

        :param id: ID объекта
        :param type: Тип WebHook: bot (на события для чат бота), line (все события по линии(ям) поддержки)
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = DelHook()
        return await self(call, request_timeout=request_timeout,
                          type_request="DELETE", path=f"/v1/hook/{type}/{is_valid_uuid(id)}/")

    """
    4.2.3 Команды для уточнения информации

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1349877812/4.2.3.
    """

    async def get_treatments(
        self,
        line_id: Optional[UUID] = None,
        user_id: Optional[UUID] = None,
        request_timeout: Optional[int] = None,
    ) -> Treatments:
        """
        Метод возвращает список открытых обращений.
        Принимает два необязательных параметра line_id и user_id.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355600/4.2.3.1.

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param request_timeout: Request timeout
        :return: Return :code:`Treatment`.
        """

        call = GetTreatments(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id)
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path="/v1/line/treatment/")

    async def get_subscriber(
        self,
        user_id: UUID,
        request_timeout: Optional[int] = None,
    ) -> User:
        """
        Метод возвращает информацию о пользователе

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289388228/4.2.3.2.

        :param user_id: ID пользователя, являющегося получателем любой линии поддержки
        :param request_timeout: Request timeout
        :return: Return :code:`User`.
        """

        call = GetSubscriber()
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path=f"/v1/line/subscriber/{is_valid_uuid(user_id)}/")

    async def get_subscribers(
        self,
        request_timeout: Optional[int] = None,
    ) -> Users:
        """
        Метод возвращает информацию о пользователях

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2068938753/4.2.3.3.

        :param request_timeout: Request timeout
        :return: Return :code:`Users`.
        """

        call = GetSubscribers()
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path="/v1/line/subscribers/")

    async def get_subscriptions(
        self,
        user_id: Optional[UUID] = None,
        client_id: Optional[UUID] = None,
        line_id: Optional[UUID] = None,
        request_timeout: Optional[int] = None,
    ) -> Subscriptions:
        """
        Метод возвращает информацию о получаемым линиям пользователями,
        с возможностью отфильтровать по пользователю, линии или клиенту.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2322923521/4.2.3.4.

        :param user_id: ID пользователя
        :param client_id: ID клиента
        :param line_id: ID линии поддержки
        :param request_timeout: Request timeout
        :return: Return :code:`Subscriptions`.
        """

        call = GetSubscriptions(
            user_id=is_valid_uuid(user_id),
            client_id=is_valid_uuid(client_id),
            line_id=is_valid_uuid(line_id)
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path="/v1/line/subscriptions/")

    async def get_lines(
        self,
        request_timeout: Optional[int] = None,
    ) -> Lines:
        """
        Метод возвращает список линий поддержки.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2156429313/4.2.3.5.

        :param request_timeout: Request timeout
        :return: Returns :code:`Lines`.
        """

        call = GetLines()
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path="/v1/line/")

    async def get_specialist(
        self,
        user_id: UUID,
        request_timeout: Optional[int] = None,
    ) -> User:
        """
        Метод возвращает информацию о специалисте

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289421100/4.2.3.6.

        :param user_id: ID пользователя, являющегося специалистом по любой линии поддержки
        :param request_timeout: Request timeout
        :return: Return :code:`User`.
        """

        call = GetSpecialist()
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path=f"/v1/line/specialist/{is_valid_uuid(user_id)}/")

    async def get_specialists(
        self,
        request_timeout: Optional[int] = None,
    ) -> Users:
        """
        Метод возвращает информацию о специалистах

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2167373825/4.2.3.7.

        :param request_timeout: Request timeout
        :return: Return :code:`Users`.
        """

        call = GetSpecialists()
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path="/v1/line/specialists/")

    async def get_specialists_available(
        self,
        line_id: UUID,
        request_timeout: Optional[int] = None,
    ) -> List[UUID]:
        """
        Метод возвращает id специалистов в статусе "Доступен" по конкретной линии поддержки
        Вызов метода позволяет узнать можно ли назначить специалиста на текущий момент методом

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2167472129/4.2.3.8.

        :param line_id: ID линии поддержки
        :param request_timeout: Request timeout
        :return: Return :code:`Array[UUID]`.
        """

        call = GetSpecialistsAvailable()
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path=f"/v1/line/specialists/{is_valid_uuid(line_id)}/available/")

    async def get_competences(
        self,
        user_id: Optional[UUID] = None,
        line_id: Optional[UUID] = None,
        request_timeout: Optional[int] = None,
    ) -> Competences:
        """
        Метод возвращает список компетенций специалистов, с возможностью отфильтровать по специалисту и линии.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2490302465/4.2.3.9.

        :param user_id: ID пользователя (специалиста)
        :param line_id: ID линии поддержки
        :param request_timeout: Request timeout
        :return: Return :code:`Treatment`.
        """

        call = GetCompetences(
            user_id=is_valid_uuid(user_id),
            line_id=is_valid_uuid(line_id),
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path="/v1/line/competences/")

    async def get_ticket(
        self,
        id: UUID,
        request_timeout: Optional[int] = None,
    ) -> TicketShort:
        """
        Метод возвращает заявку Service Desk со вложенными объектами по id

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492923976/4.2.3.10.+Service+Desk+ID

        :param id: ID заявки
        :param request_timeout: Request timeout
        :return: Return :code:`TicketShort`.
        """

        call = GetTicket()
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path=f"/v1/ticket/{is_valid_uuid(id)}/")

    async def get_ticket_by_number(
        self,
        number: int,
        request_timeout: Optional[int] = None,
    ) -> TicketShort:
        """
        Метод возвращает заявку Service Desk со вложенными объектами по номеру

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2492956727/4.2.3.11.+Service+Desk

        :param number: № заявки
        :param request_timeout: Request timeout
        :return: Return :code:`TicketShort`.
        """

        call = GetTicketByNumber()
        return await self(call, request_timeout=request_timeout,
                          type_request="GET", path=f"/v1/ticket/number/{number}/")

    """
    4.3.1. Команды внешних ботов

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1355841626/4.3.1.
    """

    async def appoint_start(
        self,
        line_id: UUID,
        user_id: UUID,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет назначить любого свободного специалиста.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1348632607/4.3.1.1.

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = AppointStart(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id),
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/line/appoint/start/")

    async def appoint_spec(
        self,
        line_id: UUID,
        user_id: UUID,
        spec_id: UUID,
        author_id: Optional[UUID] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет сделать попытку назначить конкретного специалиста.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1348632627/4.3.1.2.

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param spec_id: ID специалиста, на которого пытаемся назначить (должен быть в онлайне)
        :param author_id: ID автора (специалиста, от имени которого производится действие)
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = AppointSpec(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id),
            spec_id=is_valid_uuid(spec_id),
            author_id=is_valid_uuid(author_id),
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/line/appoint/spec/")

    async def drop_treatment(
        self,
        line_id: UUID,
        user_id: UUID,
        author_id: Optional[UUID] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет закрыть текущее обращение.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1347551359/4.3.1.3.

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param author_id: ID автора (специалиста, от имени которого производится действие)
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = DropTreatment(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id),
            author_id=is_valid_uuid(author_id),
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/line/drop/treatment/")

    async def send_message_line(
        self,
        line_id: UUID,
        user_id: UUID,
        text: str,
        author_id: Optional[UUID] = None,
        bot_as_spec: Optional[bool] = None,
        notification_only: Optional[bool] = None,
        keyboard: Optional[List[List[Button]]] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить сообщение в чат.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355725/4.3.1.4.

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param text: Текст сообщения
        :param author_id: ID автора (специалиста, от имени которого отправляется сообщение)
        :param bot_as_spec: Флаг, при наличии которого не требуется получения ответов от пользователя
        (отправка клавиатуры запрещена), и может отсутствовать подписка на события с типом bot.
        Специалист, от лица которого отправляется сообщение (поле author_id), должен быть в онлайне и в статусе
        отличном от "Нет на месте" и "Не беспокоить", во избежании лишних переназначений или постановок пользователя в
        очередь ожидания специалиста.
        :param notification_only: Флаг, при наличии которого не требуется получения ответов от пользователя
        (отправка клавиатуры запрещена), и может отсутствовать подписка на события с типом bot. Используется для
        информирования пользователя о событиях. Специалист, от лица которого отправляется сообщение (поле author_id),
        не становится назначенным. При отсутствии открытого обращения, новое не будет открыто.
        :param keyboard: Клавиатура
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendMessageLine(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id),
            author_id=is_valid_uuid(author_id),
            text=text,
            bot_as_spec=bot_as_spec,
            notification_only=notification_only,
            keyboard=keyboard
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/line/send/message/")

    async def send_file_line(
        self,
        line_id: UUID,
        user_id: UUID,
        file_name: str,
        file: Union[InputFile, str],
        author_id: Optional[UUID] = None,
        comment: Optional[str] = None,
        bot_as_spec: Optional[bool] = None,
        notification_only: Optional[bool] = None,
        keyboard: Optional[List[List[Dict[Any, str]]]] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить файл в чат.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289388419/4.3.1.5.

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param file_name: Имя файла
        :param comment: Комментарий к файлу
        :param author_id: ID автора (специалиста, от имени которого отправляется сообщение)
        :param bot_as_spec: Флаг, при наличии которого не требуется получения ответов от пользователя
        (отправка клавиатуры запрещена), и может отсутствовать подписка на события с типом bot.
        Специалист, от лица которого отправляется сообщение (поле author_id), должен быть в онлайне и в статусе
        отличном от "Нет на месте" и "Не беспокоить", во избежании лишних переназначений или постановок пользователя в
        очередь ожидания специалиста.
        :param notification_only: Флаг, при наличии которого не требуется получения ответов от пользователя
        (отправка клавиатуры запрещена), и может отсутствовать подписка на события с типом bot. Используется для
        информирования пользователя о событиях. Специалист, от лица которого отправляется сообщение (поле author_id),
        не становится назначенным. При отсутствии открытого обращения, новое не будет открыто.
        :param keyboard: Клавиатура
        :param file: Файл
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendFileLine(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id),
            author_id=is_valid_uuid(author_id),
            file_name=file_name,
            comment=comment,
            bot_as_spec=bot_as_spec,
            notification_only=notification_only,
            keyboard=keyboard,
            file=file
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST-With-Attach", path="/v1/line/send/file/")

    async def send_image_line(
        self,
        line_id: UUID,
        user_id: UUID,
        file_name: str,
        file: Union[InputFile, str],
        author_id: Optional[UUID] = None,
        comment: Optional[str] = None,
        bot_as_spec: Optional[bool] = None,
        notification_only: Optional[bool] = None,
        keyboard: Optional[List[List[Dict[Any, str]]]] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить картинку в чат.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1492091047/4.3.1.6.

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param file_name: Имя файла
        :param comment: Комментарий к файлу
        :param author_id: ID автора (специалиста, от имени которого отправляется сообщение)
        :param bot_as_spec: Флаг, при наличии которого не требуется получения ответов от пользователя
        (отправка клавиатуры запрещена), и может отсутствовать подписка на события с типом bot.
        Специалист, от лица которого отправляется сообщение (поле author_id), должен быть в онлайне и в статусе
        отличном от "Нет на месте" и "Не беспокоить", во избежании лишних переназначений или постановок пользователя в
        очередь ожидания специалиста.
        :param notification_only: Флаг, при наличии которого не требуется получения ответов от пользователя
        (отправка клавиатуры запрещена), и может отсутствовать подписка на события с типом bot. Используется для
        информирования пользователя о событиях. Специалист, от лица которого отправляется сообщение (поле author_id),
        не становится назначенным. При отсутствии открытого обращения, новое не будет открыто.
        :param keyboard: Клавиатура
        :param file: Файл
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendImageLine(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id),
            author_id=is_valid_uuid(author_id),
            file_name=file_name,
            comment=comment,
            bot_as_spec=bot_as_spec,
            notification_only=notification_only,
            keyboard=keyboard,
            file=file
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST-With-Attach", path="/v1/line/send/image/")

    async def drop_keyboard(
        self,
        line_id: UUID,
        user_id: UUID,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет убрать клавиатуру.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1347551311/4.3.1.7.+-

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = DropKeyboard(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id)
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/line/drop/keyboard/")

    async def send_message_colleague(
        self,
        recepient_id: UUID,
        author_id: UUID,
        text: str,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить сообщение в чат сотруднику от лица другого сотрудника.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1479737345/4.3.1.8.

        :param recepient_id: ID получателя
        :param author_id: ID автора (от чьего имени отправляется сообщение)
        :param text: Текст сообщения
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendMessageColleague(
            recepient_id=is_valid_uuid(recepient_id),
            author_id=is_valid_uuid(author_id),
            text=text,
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/colleague/send/message/")

    async def send_file_collegue(
        self,
        recepient_id: UUID,
        author_id: UUID,
        file_name: str,
        file: Union[InputFile, str],
        comment: Optional[str] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить файл в чат сотруднику от имени другого сотрудника.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1479442525/4.3.1.9.

        :param recepient_id: ID получателя
        :param author_id: ID автора (от чьего имени отправляется файл)
        :param file_name: Имя файла
        :param comment: Комментарий к файлу
        :param file: Файл
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendFileCollegue(
            recepient_id=is_valid_uuid(recepient_id),
            author_id=is_valid_uuid(author_id),
            file_name=file_name,
            comment=comment,
            file=file
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST-With-Attach", path="/v1/colleague/send/file/")

    async def send_image_collegue(
        self,
        recepient_id: UUID,
        author_id: UUID,
        file_name: str,
        file: Union[InputFile, str],
        comment: Optional[str] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить картинку в чат сотруднику от имени другого сотрудника.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1492091064/4.3.1.10.

        :param recepient_id: ID получателя
        :param author_id: ID автора (от чьего имени отправляется файл)
        :param file_name: Имя файла
        :param comment: Комментарий к файлу
        :param file: Картинка
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendImageColleague(
            recepient_id=is_valid_uuid(recepient_id),
            author_id=is_valid_uuid(author_id),
            file_name=file_name,
            comment=comment,
            file=file
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST-With-Attach", path="/v1/colleague/send/image/")

    async def send_message_conference(
        self,
        conference_id: UUID,
        author_id: UUID,
        text: str,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить сообщение в группу от имени участника этой группы.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1479704633/4.3.1.11.

        :param conference_id: ID группы
        :param author_id: ID автора (от чьего имени отправляется сообщение)
        :param text: Текст сообщения
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendMessageConference(
            conference_id=is_valid_uuid(conference_id),
            author_id=is_valid_uuid(author_id),
            text=text,
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/conference/send/message/")

    async def send_file_conference(
        self,
        conference_id: UUID,
        author_id: UUID,
        file_name: str,
        file: Union[InputFile, str],
        comment: Optional[str] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить файл в группу от имени участника этой группы.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1478099061/4.3.1.12.

        :param conference_id: ID группы
        :param author_id: ID автора (от чьего имени отправляется файл)
        :param file_name: Имя файла
        :param comment: Комментарий к файлу
        :param file: Файл
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendFileConference(
            conference_id=is_valid_uuid(conference_id),
            author_id=is_valid_uuid(author_id),
            file_name=file_name,
            comment=comment,
            file=file
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST-With-Attach", path="/v1/conference/send/file/")

    async def send_image_conference(
        self,
        conference_id: UUID,
        author_id: UUID,
        file_name: str,
        file: Union[InputFile, str],
        comment: Optional[str] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отправить картинку в группу от имени участника этой группы.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1492091105/4.3.1.13.

        :param conference_id: ID получателя
        :param author_id: ID автора (от чьего имени отправляется файл)
        :param file_name: Имя файла
        :param comment: Комментарий к файлу
        :param file: Картинка
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = SendImageConference(
            conference_id=is_valid_uuid(conference_id),
            author_id=is_valid_uuid(author_id),
            file_name=file_name,
            comment=comment,
            file=file
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST-With-Attach", path="/v1/conference/send/image/")

    async def question_and_answering(
        self,
        line_id: UUID,
        user_id: UUID,
        skip_greetings: bool,
        skip_goodbyes: bool,
        request_timeout: Optional[int] = None,
    ) -> Answering:
        """
        Метод позволяет получить варианты ответов на вопрос пользователя в базе знаний.

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1481932813/4.3.1.14.

        :param line_id: ID линии поддержки
        :param user_id: ID пользователя
        :param skip_greetings: Не использовать “Единая база приветствий и поддержки диалогов“
        :param skip_goodbyes: Не использовать “Единая база завершения диалогов“
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = QuestionAndAnswering(
            line_id=is_valid_uuid(line_id),
            user_id=is_valid_uuid(user_id),
            skip_greetings=skip_greetings,
            skip_goodbyes=skip_goodbyes,
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="POST", path="/v1/line/qna/")

    async def question_and_answering_selected(
        self,
        request_id: UUID,
        result_id: UUID,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Метод позволяет отметить конкретную подсказку выбранной

        Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2290024449

        :param request_id: ID запроса
        :param result_id: ID выбранной статьи
        :param request_timeout: Request timeout
        :return: Нет тела
        """

        call = QuestionAndAnsweringSelected(
            request_id=is_valid_uuid(request_id),
            result_id=is_valid_uuid(result_id),
        )
        return await self(call, request_timeout=request_timeout,
                          type_request="PUT", path="/v1/line/qna/selected/")
