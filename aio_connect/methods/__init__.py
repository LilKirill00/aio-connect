from .base import Request, Response, ConnectMethod
# 4.2.1 Команды к механизму трансляции
from .set_hook import SetHook
from .del_all_hook import DelAllHook
from .del_hook import DelHook
# 4.2.3 Команды для уточнения информации
from .get_treatments import GetTreatments
from .get_subscriber import GetSubscriber
from .get_subscribers import GetSubscribers
from .get_subscriptions import GetSubscriptions
from .get_lines import GetLines
from .get_specialist import GetSpecialist
from .get_specialists import GetSpecialists
from .get_specialists_available import GetSpecialistsAvailable
from .get_competences import GetCompetences
from .get_ticket import GetTicket
from .get_ticket_by_number import GetTicketByNumber
# 4.3.1. Команды внешних ботов
from .appoint_start import AppointStart
from .appoint_spec import AppointSpec
from .drop_treatment import DropTreatment
from .send_message_line import SendMessageLine
from .send_file_line import SendFileLine
from .send_image_line import SendImageLine
from .drop_keyboard import DropKeyboard
from .send_message_colleague import SendMessageColleague
from .send_file_collegue import SendFileCollegue
from .send_image_collegue import SendImageColleague
from .send_message_conference import SendMessageConference
from .send_file_conference import SendFileConference
from .send_image_conference import SendImageConference
from .question_and_answering import QuestionAndAnswering, QuestionAndAnsweringSelected

__all__ = (
    "Request", "Response", "ConnectMethod",
    # 4.2.1 Команды к механизму трансляции
    "SetHook",
    "DelAllHook",
    "DelHook",
    # 4.2.3 Команды для уточнения информации
    "GetTreatments",
    "GetSubscriber",
    "GetSubscribers",
    "GetSubscriptions",
    "GetLines",
    "GetSpecialist",
    "GetSpecialists",
    "GetSpecialistsAvailable",
    "GetCompetences",
    "GetTicket",
    "GetTicketByNumber",
    # 4.3.1. Команды внешних ботов
    "AppointStart",
    "AppointSpec",
    "DropTreatment",
    "SendMessageLine",
    "SendFileLine",
    "SendImageLine",
    "DropKeyboard",
    "SendMessageColleague",
    "SendFileCollegue",
    "SendImageColleague",
    "SendMessageConference",
    "SendFileConference",
    "SendImageConference",
    "QuestionAndAnswering", "QuestionAndAnsweringSelected"
)
