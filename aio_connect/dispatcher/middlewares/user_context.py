from typing import Any, Awaitable, Callable, Dict, Optional, Tuple

from aio_connect.dispatcher.middlewares.base import BaseMiddleware
from aio_connect.types import ConnectObject, Update, Line, User

EVENT_LINE_ID = "event_line_id"
EVENT_USER_ID = "event_user_id"
EVENT_AUTHOR_ID = "event_author_id"
EVENT_ACTION = "event_action"


class UserContextMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[ConnectObject, Dict[str, Any]], Awaitable[Any]],
        event: ConnectObject,
        data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, Update):
            raise RuntimeError("UserContextMiddleware got an unexpected event type!")
        line_id, user_id, author_id, action = self.resolve_event_context(event=event)
        if line_id is not None:
            data[EVENT_LINE_ID] = line_id
        if user_id is not None:
            data[EVENT_USER_ID] = user_id
        if author_id is not None:
            data[EVENT_AUTHOR_ID] = author_id
        if action is not None:
            data[EVENT_ACTION] = action
        return await handler(event, data)

    @classmethod
    def resolve_event_context(
        cls, event: Update
    ) -> Tuple[Optional[Line], Optional[User], Optional[User], Optional[str]]:
        """
        Resolve chat and user instance from Update object
        """
        if event.event_type == "competence":
            return None, None, None, event.competence.action
        if event.event_type == "line":
            return event.line.line_id, event.line.user_id, event.line.author_id, None
        if event.event_type == "subscriber":
            return None, None, None, event.subscriber.action
        if event.event_type == "subscription":
            return None, None, None, event.subscription.action
        if event.event_type == "support_line":
            return None, None, None, event.support_line.action

        return None, None, None, None
