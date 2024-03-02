from typing import Any, Awaitable, Callable, Dict, Optional

from aio_connect.dispatcher.middlewares.base import BaseMiddleware
from aio_connect.fsm.context import FSMContext
from aio_connect.fsm.storage.base import (
    DEFAULT_DESTINY,
    BaseEventIsolation,
    BaseStorage,
    StorageKey,
)
from aio_connect.types import ConnectObject, UUID


class FSMContextMiddleware(BaseMiddleware):
    def __init__(
        self,
        storage: BaseStorage,
        events_isolation: BaseEventIsolation,
    ) -> None:
        self.storage = storage
        self.events_isolation = events_isolation

    async def __call__(
        self,
        handler: Callable[[ConnectObject, Dict[str, Any]], Awaitable[Any]],
        event: ConnectObject,
        data: Dict[str, Any],
    ) -> Any:
        context = self.resolve_event_context(data)
        data["fsm_storage"] = self.storage
        if context:
            # Bugfix:
            # State should be loaded after lock is acquired
            async with self.events_isolation.lock(key=context.key):
                data.update({"state": context, "raw_state": await context.get_state()})
                return await handler(event, data)
        return await handler(event, data)

    def resolve_event_context(
        self,
        data: Dict[str, Any],
        destiny: str = DEFAULT_DESTINY,
    ) -> Optional[FSMContext]:
        line_id = data.get("event_line_id")
        user_id = data.get("event_user_id")
        author_id = data.get("event_author_id")
        action = data.get("event_action")
        return self.resolve_context(
            line_id=line_id,
            user_id=user_id,
            author_id=author_id,
            action=action,
            destiny=destiny,
        )

    def resolve_context(
        self,
        line_id: Optional[UUID] = None,
        user_id: Optional[UUID] = None,
        author_id: Optional[UUID] = None,
        action: Optional[str] = None,
        destiny: str = DEFAULT_DESTINY,
    ) -> Optional[FSMContext]:
        return self.get_context(
                line_id=line_id,
                user_id=user_id,
                author_id=author_id,
                action=action,
                destiny=destiny,
        )

    def get_context(
        self,
        line_id: Optional[UUID] = None,
        user_id: Optional[UUID] = None,
        author_id: Optional[UUID] = None,
        action: Optional[str] = None,
        destiny: str = DEFAULT_DESTINY,
    ) -> FSMContext:
        return FSMContext(
            storage=self.storage,
            key=StorageKey(
                line_id=line_id,
                user_id=user_id,
                author_id=author_id,
                action=action,
                destiny=destiny,
            ),
        )

    async def close(self) -> None:
        await self.storage.close()
        await self.events_isolation.close()
