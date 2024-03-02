from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject
from ..enums import ContentType

from datetime import datetime
from ..types import UUID, File, Call, Rda, ServiceRequest, Treatment, Data, PartnerNotification


class TypeLine(ConnectObject):
    """
    Дополнительные данные в сообщении:

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1357053953/4.2.2.2.2+line
    """

    message_id: UUID
    """ID сообщения"""
    message_type: int
    """Тип сообщения"""
    message_time: datetime
    """Время отправки сообщения"""
    treatment_id: Optional[UUID] = None
    """ID обращения
        Если это поле содержит неизвестный до текущего момента ID, то считается что начато новое обращение.
        Это справедливо для сообщений с любым типом.
    """
    author_id: Optional[UUID] = None
    """ID пользователя (может отсутствовать в случае инициации события автоматического закрытия обращения)"""
    line_id: UUID
    """ID линии поддержки"""
    user_id: UUID
    """ID пользователя"""
    text: Optional[str] = None
    """Текст сообщения"""
    file: Optional[File] = None
    """Данные файла"""
    call: Optional[Call] = None
    """Данные о звонке"""
    rda: Optional[Rda] = None
    """Данные о сеансе удаленного доступа"""
    service_request: Optional[ServiceRequest] = None
    """Данные заявки Service Desk"""
    treatment: Optional[Treatment] = None
    """Информация об обращении"""
    data: Optional[Data] = None
    """Дополнительные данные"""
    partner_notification: Optional[PartnerNotification] = None
    """Рассылка"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
                __pydantic__self__,
                *,
                message_id: UUID,
                message_type: int,
                message_time: datetime,
                treatment_id: Optional[UUID] = None,
                author_id: Optional[UUID] = None,
                line_id: UUID,
                user_id: UUID,
                text: Optional[str] = None,
                file: Optional[File] = None,
                call: Optional[Call] = None,
                rda: Optional[Rda] = None,
                service_request: Optional[ServiceRequest] = None,
                treatment: Optional[Treatment] = None,
                data: Optional[Data] = None,
                partner_notification: Optional[PartnerNotification] = None,
                **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                message_id=message_id,
                message_type=message_type,
                message_time=message_time,
                treatment_id=treatment_id,
                author_id=author_id,
                line_id=line_id,
                user_id=user_id,
                text=text,
                file=file,
                call=call,
                rda=rda,
                service_request=service_request,
                treatment=treatment,
                data=data,
                partner_notification=partner_notification,
                **__pydantic_kwargs,
            )

    @property
    def content_type(self) -> str:

        TypeMessage = {
            1: ContentType.TEXT,  # Текстовое сообщение
            2: ContentType.NOTIFY,  # Рассылка

            17: ContentType.QUALITY_WORK,  # Оценка работы специалиста

            20: ContentType.CALL_START_WITH_NSS,  # Начало звонка с открытием обращения
            21: ContentType.CALL_START_WITHOUT_NSS,  # Начало звонка без открытия обращения
            22: ContentType.CALL_END_GOOD,  # Удачное завершение звонка
            23: ContentType.CALL_BADCALL_CANCELED,  # Неудачное завершение звонка. Вызов отменен инициатором
            24: ContentType.CALL_BADCALL_EXCESS,  # Неудачное завершение звонка. Абонент не ответил
            25: ContentType.CALL_BADCALL_NONSS,  # Неудачное завершение звонка. Нет свободных специалистов
            26: ContentType.CALL_BADCALL_REJECTED,  # Неудачное завершение звонка. Вызов отклонен адресатом
            27: ContentType.CALL_REROUTING,  # Перевод звонка на специалиста
            28: ContentType.CALL_REROUTING_VENDOR,  # Перевод звонка в компанию вендора
            30: ContentType.CALL_REROUTING_WITHOUTEND,  # Перевод звонка без завершения(когда абонент не взял
            # трубку, а сразу перевел звонок)
            31: ContentType.CALL_REROUTING_VENDORFRAN_WE,  # Перевод звонка без завершения на вендора(когда абонент
            # не взял трубку, а сразу перевел звонок)

            32: ContentType.CALL_TECHNICAL_PROBLEM,  # Нет соединения с голосовым сервером
            36: ContentType.CALL_TECHNICAL_PROBLEM_NO_AUDIO,  # Неудачное завершение. У абонента нет аудио
            # устройства
            38: ContentType.LINE_CALLUNAVAIL,  # Недоступная линия по звонку (нерабочее время)

            50: ContentType.RDA_START_WITH_NSS,  # Начало сеанса удаленного доступа с сервисным специалистом
            51: ContentType.RDA_START_WITHOUT_NSS,  # Начало сеанса удаленного доступа без сервисного специалиста
            # (Специалист принудительно назначается пользователю сеансом удаленного доступа)
            52: ContentType.RDA_END_WITHT_RANSFER_FILES,  # Окончание сеанса удаленного доступа с передачей файлов
            53: ContentType.RDA_END_WITHTOUT_RANSFER_FILES,  # Окончание сеанса удаленного доступа без передачей
            # файлов
            54: ContentType.RDA_BAD_CANCELED,  # Неудачное завершение удаленного доступа. Сеанс отменен инициатором
            55: ContentType.RDA_BAD_REJECTED,  # Неудачное завершение удаленного доступа. Сеанс отклонен принимающим
            56: ContentType.RDA_BAD_EXCESS,  # Неудачное завершение удаленного доступа. Сеанс не состоялся по
            # таймауту
            57: ContentType.RDA_BAD,  # Неудачное завершение удаленного доступа
            59: ContentType.RDA_BAD_OLD_SERVICE,  # Неудачное завершение - устаревшая версия службы
            60: ContentType.RDA_BAD_NO_SERVICE,  # Неудачное завершение - служба не установлена
            61: ContentType.RDA_BAD_OLD_COMPONENT,  # Неудачное завершение - устаревшие версии компонентов
            62: ContentType.RDA_BAD_NO_FILES,  # Неудачное завершение - отсутствуют файлы компонентов УД

            70: ContentType.TRANSFERFILES,  # Передача файла через чат

            80: ContentType.LINE_USERINIT,  # Назначение специалиста системой. Инициатором был пользователь
            81: ContentType.LINE_SPECINIT,  # Специалист назначился. Инициатором был специалист
            82: ContentType.LINE_SPECDEL,  # Завершение работы специалиста (Закрытие обращения)
            83: ContentType.LINE_NONSS,  # Обращение поступило в очередь. Нет свободных специалистов

            84: ContentType.LINE_REROUTINGSPEC,  # Перевод обращения на специалиста

            85: ContentType.LINE_REROUTING_VENDOR,  # Перевод обращения в компанию вендора

            86: ContentType.LINE_SPECFOUND,  # Для обращения в очереди появился свободный специалист
            87: ContentType.LINE_CHATUNAVAIL,  # Недоступность линии (нерабочее время)
            88: ContentType.LINE_REROUTE_UNAVAIL,  # Недоступность линии по переводу. При переводе обращения в
            # компанию вендора попали в нерабочее время

            89: ContentType.LINE_REROUTING_OTHERSERVICE,  # Перевод в другую линию поддержки

            90: ContentType.LINE_CLOSED_NO_ACTIVITY,  # Обращение закрыто автоматически по отсутствию активности в
            # чате
            91: ContentType.LINE_CLOSED_REMOVE_SERVICE,  # Обращение закрыто автоматически, т.к.удалена линия
            # поддержки
            92: ContentType.LINE_CLOSED_REMOVE_SUBSCRIPTION,  # Обращение закрыто автоматически, т.к.удалена
            # подписка пользователя
            93: ContentType.LINE_CLOSED_REMOVE_USER,  # Обращение закрыто автоматически, т.к.удален пользователь

            121: ContentType.SERVICE_REQUEST_ADD,  # Создание заявки Service Desk
            122: ContentType,  # Изменение заявки Service Desk
            123: ContentType,  # Завершение заявки Service Desk
            124: ContentType,  # Отмена заявки Service Desk

            200: ContentType.LINE_REROUTING_TO_BOT,  # Перевод обращения специалистом на бота
        }

        if self.message_type:
            return TypeMessage[self.message_type]

        return ContentType.UNKNOWN
