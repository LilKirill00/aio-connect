from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, cast

from ..utils.mypy_hacks import lru_cache
from .base import ConnectObject

if TYPE_CHECKING:
    from .type_competence import TypeCompetence
    from .type_line import TypeLine
    from .type_subscriber import TypeSubscriber
    from .type_subscription import TypeSubscription
    from .type_support_line import TypeSupportLine


class Update(ConnectObject):
    """
    This `object` represents an incoming update.

    At most **one** of the optional parameters can be present in any given update.
    """

    event_type: str
    """Тип события:
        line - событие по линии поддержки
        subscriber - изменения в профиле пользователя
        support_line - изменения линии поддержки
        competence - изменение компетенция
        subscription - изменения в подписках
    """
    event_source: str
    """Для подписки какого типа сгенерировано событие:
        line - событие на подписки с типом line
        bot - событие на подписки с типом bot
    """

    competence: Optional[TypeCompetence] = None
    line: Optional[TypeLine] = None
    subscriber: Optional[TypeSubscriber] = None
    subscription: Optional[TypeSubscription] = None
    support_line: Optional[TypeSupportLine] = None

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            event_type: str,
            event_source: str,

            competence: Optional[TypeCompetence] = None,
            line: Optional[TypeLine] = None,
            subscriber: Optional[TypeSubscriber] = None,
            subscription: Optional[TypeSubscription] = None,
            support_line: Optional[TypeSupportLine] = None,

            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                event_type=event_type,
                event_source=event_source,

                competence=competence,
                line=line,
                subscriber=subscriber,
                subscription=subscription,
                support_line=support_line,

                **__pydantic_kwargs,
            )

    @property
    @lru_cache()
    def get_event_type(self) -> str:
        """
        Detect update type
        If update type is unknown, raise UpdateTypeLookupError

        :return:
        """

        if self.competence:
            return "competence"
        if self.line:
            return "line"
        if self.subscriber:
            return "subscriber"
        if self.subscription:
            return "subscription"
        if self.support_line:
            return "support_line"

        raise UpdateTypeLookupError("Update does not contain any known event type.")

    @property
    def event(self) -> ConnectObject:
        return cast(ConnectObject, getattr(self, self.get_event_type))


class UpdateTypeLookupError(LookupError):
    """Update does not contain any known event type."""
