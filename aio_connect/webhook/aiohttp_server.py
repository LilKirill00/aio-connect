import asyncio
from abc import ABC, abstractmethod
from typing import Any, Dict, Set

from aiohttp import web
from aiohttp.abc import Application

from aio_connect import Bot, Dispatcher
from aio_connect.methods import ConnectMethod


def setup_application(app: Application, dispatcher: Dispatcher, /, **kwargs: Any) -> None:
    """
    This function helps to configure a startup-shutdown process

    :param app: aiohttp application
    :param dispatcher: aio-connect dispatcher
    :param kwargs: additional data
    :return:
    """
    workflow_data = {
        "app": app,
        "dispatcher": dispatcher,
        **dispatcher.workflow_data,
        **kwargs,
    }

    async def on_startup(*a: Any, **kw: Any) -> None:  # pragma: no cover
        await dispatcher.emit_startup(**workflow_data)

    async def on_shutdown(*a: Any, **kw: Any) -> None:  # pragma: no cover
        await dispatcher.emit_shutdown(**workflow_data)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)


class BaseRequestHandler(ABC):
    def __init__(
        self,
        dispatcher: Dispatcher,
        **data: Any,
    ) -> None:
        """
        Base handler that helps to handle incoming request from aiohttp
        and propagate it to the Dispatcher

        :param dispatcher: instance of :class:`aio_connect.dispatcher.dispatcher.Dispatcher`
        """
        self.dispatcher = dispatcher
        self.data = data
        self._background_feed_update_tasks: Set[asyncio.Task[Any]] = set()

    def register(self, app: Application, /, path: str, **kwargs: Any) -> None:
        """
        Register route and shutdown callback

        :param app: instance of aiohttp Application
        :param path: route path
        :param kwargs:
        """
        app.on_shutdown.append(self._handle_close)
        app.router.add_route("POST", path, self.handle, **kwargs)

    async def _handle_close(self, app: Application) -> None:
        await self.close()

    @abstractmethod
    async def close(self) -> None:
        pass

    @abstractmethod
    async def resolve_bot(self, request: web.Request) -> Bot:
        """
        This method should be implemented in subclasses of this class.

        Resolve Bot instance from request.

        :param request:
        :return: Bot instance
        """
        pass

    @abstractmethod
    def verify_bot(self, bot: Bot) -> bool:
        if bot.auth:
            return True

    async def _background_feed_update(self, bot: Bot, update: Dict[str, Any]) -> None:
        result = await self.dispatcher.feed_raw_update(bot=bot, update=update, **self.data)
        if isinstance(result, ConnectMethod):
            await self.dispatcher.silent_call_request(bot=bot, result=result)

    async def _handle_request_background(self, bot: Bot, request: web.Request) -> web.Response:
        update = await request.json(loads=bot.session.json_loads)
        new_update = {'event_type': update["event_type"], 'event_source': update["event_source"],
                      update["event_type"]: {obj: update[obj] for obj in update if
                                             obj not in ('event_type', 'event_source')}}
        print("------")  # Fixme: remove
        print(new_update)  # Fixme: remove
        feed_update_task = asyncio.create_task(
            self._background_feed_update(
                bot=bot, update=new_update
            )
        )
        self._background_feed_update_tasks.add(feed_update_task)
        feed_update_task.add_done_callback(self._background_feed_update_tasks.discard)
        return web.json_response({}, dumps=bot.session.json_dumps)

    async def handle(self, request: web.Request) -> web.Response:
        bot = await self.resolve_bot(request)
        if not self.verify_bot(bot):
            return web.Response(body="Unauthorized", status=401)
        return await self._handle_request_background(bot=bot, request=request)

    __call__ = handle


class SimpleRequestHandler(BaseRequestHandler):
    def __init__(
        self,
        dispatcher: Dispatcher,
        bot: Bot,
        **data: Any,
    ) -> None:
        """
        Handler for single Bot instance

        :param dispatcher: instance of :class:`aio_connect.dispatcher.dispatcher.Dispatcher`
        :param bot: instance of :class:`aio_connect.client.bot.Bot`
        """
        super().__init__(dispatcher=dispatcher, **data)
        self.bot = bot

    def verify_bot(self, bot: Bot) -> bool:
        if bot.auth:
            return True

    async def close(self) -> None:
        """
        Close bot session
        """
        await self.bot.session.close()

    async def resolve_bot(self, request: web.Request) -> Bot:
        return self.bot
