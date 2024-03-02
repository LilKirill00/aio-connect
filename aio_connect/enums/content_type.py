from enum import Enum


class ContentType(str, Enum):
    """
    This object represents a type of content in message
    """

    UNKNOWN = "unknown"
    ANY = "any"

    CALL = "call"  # Тип line
    RDA = "rda"  # Тип line
    SERVICE_REQUEST = "service_request"  # Тип line
    TREATMENT = "treatment"  # Тип line
    DATA = "data"  # Тип line

    COMPETENCE = "competence"  # Тип competence
    USER = "user"  # Тип subscriber
    SUBSCRIPTION = "subscription"  # Тип subscription
    LINE = "line"  # Тип support_line

    ACTION = "action"  # Типы competence subscriber subscription support_line

    # Message type
    TEXT = "text"  # 1 - Текстовое сообщение
    NOTIFY = "notify"  # 2 - Рассылка
    REPORT = "report"  # 3 -
    BOT = "bot"  # 4 -

    RECORD = "record"  # 16 -

    QUALITY_WORK = "quality_work"  # 17 -

    CALL_START_WITH_NSS = "call_start_with_nss"  # 20 - Начало звонка с открытием обращения
    CALL_START_WITHOUT_NSS = "call_start_without_nss"  # 21 - Начало звонка без открытия обращения
    CALL_END_GOOD = "call_end_good"  # 22 - Удачное завершение звонка
    CALL_BADCALL_CANCELED = "call_badcall_canceled"  # 23 - Неудачное завершение звонка. Вызов отменен инициатором
    CALL_BADCALL_EXCESS = "call_badcall_excess"  # 24 - Неудачное завершение звонка. Абонент не ответил
    CALL_BADCALL_NONSS = "call_badcall_nonss"  # 25 - Неудачное завершение звонка. Нет свободных специалистов
    CALL_BADCALL_REJECTED = "call_badcall_rejected"  # 26 - Неудачное завершение звонка. Вызов отклонен адресатом
    CALL_REROUTING = "call_rerouting"  # 27 - Перевод звонка на специалиста
    CALL_REROUTING_VENDOR = "call_rerouting_vendor"  # 28 - Перевод звонка в компанию вендора
    CALL_REROUTING_COLL2COLL = "call_rerouting_coll2coll"  # 29 -
    CALL_REROUTING_WITHOUTEND = "call_rerouting_withoutend"  # 30 - Перевод звонка без завершения(когда абонент не взял
    # трубку, а сразу перевел звонок)
    CALL_REROUTING_VENDORFRAN_WE = "call_rerouting_vendorfran_we"  # 31 - Перевод звонка без завершения на вендора(когда
    # абонент не взял трубку, а сразу перевел звонок)

    CALL_TECHNICAL_PROBLEM = "call_technical_problem"  # 32 - Нет соединения с голосовым сервером
    CALL_TECHNICAL_PROBLEM_33 = "call_technical_problem_33"  # 33 -
    CALL_TECHNICAL_PROBLEM_34 = "call_technical_problem_34"  # 34 -
    CALL_TECHNICAL_PROBLEM_35 = "call_technical_problem_35"  # 35 -
    CALL_TECHNICAL_PROBLEM_NO_AUDIO = "call_technical_problem_no_audio"  # 36 - Неудачное завершение. У абонента нет
    # аудио устройства
    CALL_TECHNICAL_PROBLEM_37 = "call_technical_problem_37"  # 37 -
    LINE_CALLUNAVAIL = "line_callunavail"  # 38 - Недоступная линия по звонку (нерабочее время)

    CONFERENCE_STARTCALL = "conference_startcall"  # 40 -
    CONFERENCE_ENDCALL = "conference_endcall"  # 41 -
    CONFERENCE_BADCALL_CANCELED = "conference_badcall_canceled"  # 42 -
    CONFERENCE_BADCALL_EXCESS = "conference_badcall_excess"  # 43 -
    CONFERENCE_BADCALL_TECHNICALPROBLEM = "conference_badcall_technicalproblem"  # 44 -

    RDA_START_WITH_NSS = "rda_start_with_nss"  # 50 - Начало сеанса удаленного доступа с сервисным специалистом
    RDA_START_WITHOUT_NSS = "rda_start_without_nss"  # 51 - Начало сеанса удаленного доступа без сервисного специалиста
    # (Специалист принудительно назначается пользователю сеансом удаленного доступа)
    RDA_END_WITHT_RANSFER_FILES = "rda_end_witht_ransfer_files"  # 52 - Окончание сеанса удаленного доступа с передачей
    # файлов
    RDA_END_WITHTOUT_RANSFER_FILES = "rda_end_withtout_ransfer_files"  # 53 - Окончание сеанса удаленного доступа без
    # передачей файлов
    RDA_BAD_CANCELED = "rda_bad_canceled"  # 54 - Неудачное завершение удаленного доступа. Сеанс отменен инициатором
    RDA_BAD_REJECTED = "rda_bad_rejected"  # 55 - Неудачное завершение удаленного доступа. Сеанс отклонен принимающим
    RDA_BAD_EXCESS = "rda_bad_excess"  # 56 - Неудачное завершение удаленного доступа. Сеанс не состоялся по таймауту
    RDA_BAD = "rda_bad"  # 57 - Неудачное завершение удаленного доступа
    RDA_P2P = "rda_p2p"  # 58 -
    RDA_BAD_OLD_SERVICE = "rda_bad_old_service"  # 59 - Неудачное завершение - устаревшая версия службы
    RDA_BAD_NO_SERVICE = "rda_bad_no_service"  # 60 - Неудачное завершение - служба не установлена
    RDA_BAD_OLD_COMPONENT = "rda_bad_old_component"  # 61 - Неудачное завершение - устаревшие версии компонентов
    RDA_BAD_NO_FILES = "rda_bad_no_files"  # 62 - Неудачное завершение - отсутствуют файлы компонентов УД

    TRANSFERFILES = "transferfiles"  # 70 - Передача файла через чат

    LINE_USERINIT = "line_userinit"  # 80 - Назначение специалиста системой. Инициатором был пользователь
    LINE_SPECINIT = "line_specinit"  # 81 - Специалист назначился. Инициатором был специалист
    LINE_SPECDEL = "line_specdel"  # 82 - Завершение работы специалиста (Закрытие обращения)
    LINE_NONSS = "line_nonss"  # 83 - Обращение поступило в очередь. Нет свободных специалистов

    LINE_REROUTINGSPEC = "line_reroutingspec"  # 84 - Перевод обращения на специалиста

    LINE_REROUTING_VENDOR = "line_rerouting_vendor"  # 85 - Перевод обращения в компанию вендора

    LINE_SPECFOUND = "line_specfound"  # 86 - Для обращения в очереди появился свободный специалист
    LINE_CHATUNAVAIL = "line_chatunavail"  # 87 - Недоступность линии (нерабочее время)
    LINE_REROUTE_UNAVAIL = "line_reroute_unavail"  # 88 - Недоступность линии по переводу. При переводе обращения в
    # компанию вендора попали в нерабочее время

    LINE_REROUTING_OTHERSERVICE = "line_rerouting_otherservice"  # 89 - Перевод в другую линию поддержки

    LINE_CLOSED_NO_ACTIVITY = "line_closed_no_activity"  # 90 - Обращение закрыто автоматически по отсутствию активности
    # в чате
    LINE_CLOSED_REMOVE_SERVICE = "line_closed_remove_service"  # 91 - Обращение закрыто автоматически, т.к.удалена линия
    # поддержки
    LINE_CLOSED_REMOVE_SUBSCRIPTION = "line_closed_remove_subscription"  # 92 - Обращение закрыто автоматически, т.к.
    # удалена подписка пользователя
    LINE_CLOSED_REMOVE_USER = "line_closed_remove_user"  # 93 - Обращение закрыто автоматически, т.к.удален пользователь

    BUSSINES_CONTACT_ADD = "bussines_contact_add"  # 100 -
    BUSSINES_CONTACT_CANCEL = "bussines_contact_cancel"  # 101 -
    BUSSINES_CONTACT_HIDE = "bussines_contact_hide"  # 102 -
    BUSSINES_CONTACT_ACCEPT = "bussines_contact_accept"  # 103 -
    BUSSINES_CONTACT_REMOVE = "bussines_contact_remove"  # 104 -

    CONFERENCE_NEW = "conference_new"  # 110 -
    CONFERENCE_CHANGENAME = "conference_changename"  # 111 -
    CONFERENCE_NEWAVATAR = "conference_newavatar"  # 112 -
    CONFERENCE_ADD = "conference_add"  # 113 -
    CONFERENCE_DELETE = "conference_delete"  # 114 -
    CONFERENCE_LEAVE = "conference_leave"  # 115 -
    CONFERENCE_CLOSE = "conference_close"  # 116 -
    CONFERENCE_SETADMIN = "conference_setadmin"  # 117 -
    CONFERENCE_CALLCANCEL_BY_MEMBERS = "conference_callcancel_by_members"  # 118 -
    CONFERENCE_ADD_FROM_LINK = "conference_add_from_link"  # 119 -

    SERVICE_REQUEST_ADD = "service_request_add"  # 121 - Создание заявки Service Desk
    # 122 - Изменение заявки Service Desk
    # 123 - Завершение заявки Service Desk
    # 124 - Отмена заявки Service Desk

    LINE_REROUTING_TO_BOT = "line_rerouting_to_bot"  # 200 - Перевод обращения специалистом на бота
