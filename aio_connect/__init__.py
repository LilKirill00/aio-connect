import asyncio as _asyncio
from contextlib import suppress

from . import enums, methods, types
from .client import session
from .client.bot import Bot
from .dispatcher.dispatcher import Dispatcher
from .dispatcher.middlewares.base import BaseMiddleware
from .dispatcher.router import Router
from .utils.magic_filter import MagicFilter

with suppress(ImportError):
    import uvloop as _uvloop

    _asyncio.set_event_loop_policy(_uvloop.EventLoopPolicy())


F = MagicFilter()

__all__ = (
    "types",
    "methods",
    "enums",
    "Bot",
    "session",
    "Dispatcher",
    "Router",
    "BaseMiddleware",
    "F",
)
