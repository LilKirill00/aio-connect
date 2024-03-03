# aio-connect

**aio-connect** — библиотека предназначается для создания ботов в среде 1С-Коннект.

За основу для написания библиотеки была заимствована библиотека [aiogram](https://github.com/aiogram/aiogram).

## Установка
Вы можете установить библиотеку с помощью pip:
```python
pip install aio-1c-connect
```

## Использование
Пример реализации бота с использованием данной библиотеки: [aio-connect-simple-bot](https://github.com/LilKirill00/aio-connect-simple-bot) 

Пример создания бота:
```python
import sys
import logging

from aiohttp import web

from config_reader import config
from aio_connect.types import HookType
from aio_connect import Bot, Dispatcher, Router, types, F
from aio_connect.webhook.aiohttp_server import SimpleRequestHandler, setup_application

SERVER_API = config.SERVER_API

# host
BASE_WEBHOOK_URL = config.BASE_WEBHOOK_URL
WEBHOOK_PATH = config.WEBHOOK_PATH

# listen
WEB_SERVER_HOST = config.WEB_SERVER_HOST
WEB_SERVER_PORT = config.WEB_SERVER_PORT

# line
LINE_ID = config.LINE_ID

bot = Bot(
    api_login=config.API_LOGIN.get_secret_value(),
    api_password=config.API_PASSSWORD.get_secret_value(),
    line_id=LINE_ID,
    base=SERVER_API
)


async def on_startup() -> None:
    await bot.set_hook(type=HookType.BOT, id=LINE_ID, url=BASE_WEBHOOK_URL + WEBHOOK_PATH + LINE_ID)


router = Router()


@router.line(F.text)
async def text_handler(line: types.TypeLine) -> None:
    if line.user_id == line.author_id:
        await bot.send_message_line(line_id=line.line_id, user_id=line.user_id, text=line.text)


def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)

    dp.startup.register(on_startup)

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH + LINE_ID)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
```

## Документация
Написание библиотеки основывалось на: [Документации для разработчиков](https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/975568915/4.).

## Лицензия
Библиотека распространяется под лицензией MIT. Подробности можно узнать в файле
[LICENSE](https://github.com/LilKirill00/aio-connect/blob/main/LICENSE).
