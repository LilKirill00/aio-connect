from enum import Enum


class UpdateType(str, Enum):
    """
    This object represents the complete list of allowed update types
    """
    COMPETENCE = "competence"
    LINE = "line"
    SUBSCRIBER = "subscriber"
    SUBSCRIPTION = "subscription"
    SUPPORT_LINE = "support_line"
