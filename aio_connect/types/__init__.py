from typing import List, Literal, Optional, Union

from .base import ConnectObject
from .input_file import BufferedInputFile, FSInputFile, InputFile, URLInputFile
from .bot_command import BotCommand
from .update import Update
from .uuid import UUID, is_valid_uuid
from .answering import Answering
from .hook_type import HookType
# 4.2.2.1. Объекты
from .competence import Competence, Competences
from .subscriptions import Subscriptions
from .user_service_line import UserServiceLine
from .user import User, Users
from .line import Line, LineShort, Lines
from .call import Call
from .file import File
from .rda import Rda
from .service_request import ServiceRequest
from .treatment import Treatment, Treatments
from .data import Data
from .partner_notification import PartnerNotification
from .ticket_channel import TicketChannel
from .ticket_status import TicketStatus
from .ticket_type import TicketType
from .service_kind import ServiceKind
from .ticket_additional_field_value import TicketAdditionalFieldValue
from .ticket_short import TicketShort
# 4.2.2.2. Структура событий
from .type_competence import TypeCompetence
from .type_line import TypeLine
from .type_subscriber import TypeSubscriber
from .type_subscription import TypeSubscription
from .type_support_line import TypeSupportLine
# 4.3.2. Структуры данных для ботов
from .button import Button

__all__ = (
    "ConnectObject",
    "BufferedInputFile", "FSInputFile", "InputFile", "URLInputFile",
    "BotCommand",
    "Update",
    "UUID", "is_valid_uuid",
    "Answering",
    "HookType",
    # 4.2.2.1. Объекты
    "Competence", "Competences",
    "Subscriptions",
    "UserServiceLine",
    "User", "Users",
    "Line", "LineShort", "Lines",
    "Call",
    "File",
    "Rda",
    "ServiceRequest",
    "Treatment", "Treatments",
    "Data",
    "PartnerNotification",
    "TicketChannel",
    "TicketStatus",
    "TicketType",
    "ServiceKind",
    "TicketAdditionalFieldValue",
    "TicketShort",
    # 4.2.2.2. Структура событий
    "TypeCompetence",
    "TypeLine",
    "TypeSubscriber",
    "TypeSubscription",
    "TypeSupportLine",
    # 4.3.2. Структуры данных для ботов
    "Button",
)


# Load typing forward refs for every ConnectObject
for _entity_name in __all__:
    _entity = globals()[_entity_name]
    if not hasattr(_entity, "model_rebuild"):
        continue
    _entity.model_rebuild(
        _types_namespace={
            "List": List,
            "Optional": Optional,
            "Union": Union,
            "Literal": Literal,
            **{k: v for k, v in globals().items() if k in __all__},
        }
    )

del _entity
del _entity_name
