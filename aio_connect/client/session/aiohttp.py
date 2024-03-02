from __future__ import annotations

import asyncio
import json
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    Union,
    cast,
)

from aiohttp import BasicAuth, ClientError, ClientSession, FormData, TCPConnector
from aiohttp.hdrs import USER_AGENT
from aiohttp.http import SERVER_SOFTWARE

from aio_connect.methods import ConnectMethod

from ...exceptions import ConnectNetworkError
from ...methods.base import ConnectType
from ...types import InputFile
from .base import BaseSession

if TYPE_CHECKING:
    from ..bot import Bot

_ProxyBasic = Union[str, Tuple[str, BasicAuth]]
_ProxyChain = Iterable[_ProxyBasic]
_ProxyType = Union[_ProxyChain, _ProxyBasic]


def _retrieve_basic(basic: _ProxyBasic) -> Dict[str, Any]:
    from aiohttp_socks.utils import parse_proxy_url  # type: ignore

    proxy_auth: Optional[BasicAuth] = None

    if isinstance(basic, str):
        proxy_url = basic
    else:
        proxy_url, proxy_auth = basic

    proxy_type, host, port, username, password = parse_proxy_url(proxy_url)
    if isinstance(proxy_auth, BasicAuth):
        username = proxy_auth.login
        password = proxy_auth.password

    return {
        "proxy_type": proxy_type,
        "host": host,
        "port": port,
        "username": username,
        "password": password,
        "rdns": True,
    }


def _prepare_connector(chain_or_plain: _ProxyType) -> Tuple[Type["TCPConnector"], Dict[str, Any]]:
    from aiohttp_socks import ChainProxyConnector, ProxyConnector, ProxyInfo     # type: ignore

    # since tuple is Iterable(compatible with _ProxyChain) object, we assume that
    # user wants chained proxies if tuple is a pair of string(url) and BasicAuth
    if isinstance(chain_or_plain, str) or (
        isinstance(chain_or_plain, tuple) and len(chain_or_plain) == 2
    ):
        chain_or_plain = cast(_ProxyBasic, chain_or_plain)
        return ProxyConnector, _retrieve_basic(chain_or_plain)

    chain_or_plain = cast(_ProxyChain, chain_or_plain)
    infos: List[ProxyInfo] = []
    for basic in chain_or_plain:
        infos.append(ProxyInfo(**_retrieve_basic(basic)))

    return ChainProxyConnector, {"proxy_infos": infos}


class AiohttpSession(BaseSession):
    def __init__(self, proxy: Optional[_ProxyType] = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)

        self._session: Optional[ClientSession] = None
        self._connector_type: Type[TCPConnector] = TCPConnector
        self._should_reset_connector = True  # flag determines connector state
        self._proxy: Optional[_ProxyType] = None

        if proxy is not None:
            try:
                self._setup_proxy_connector(proxy)
            except ImportError as exc:  # pragma: no cover
                raise RuntimeError(
                    "In order to use aiohttp client for proxy requests, install "
                    "https://pypi.org/project/aiohttp-socks/"
                ) from exc

    def _setup_proxy_connector(self, proxy: _ProxyType) -> None:
        self._proxy = proxy

    @property
    def proxy(self) -> Optional[_ProxyType]:
        return self._proxy

    @proxy.setter
    def proxy(self, proxy: _ProxyType) -> None:
        self._setup_proxy_connector(proxy)
        self._should_reset_connector = True

    async def create_session(self) -> ClientSession:
        if self._should_reset_connector:
            await self.close()

        if self._session is None or self._session.closed:
            self._session = ClientSession(
                headers={
                    USER_AGENT: f"{SERVER_SOFTWARE}",
                },
            )
            self._should_reset_connector = False

        return self._session

    async def close(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()

            # Wait 250 ms for the underlying SSL connections to close
            # https://docs.aiohttp.org/en/stable/client_advanced.html#graceful-shutdown
            await asyncio.sleep(0.25)

    def build_form_data(self, bot: Bot, method: ConnectMethod[ConnectType]) -> FormData:
        form = FormData(quote_fields=False)
        files: Dict[str, InputFile] = {}

        new_json = {}
        for key, value in method.model_dump(warnings=False, exclude_none=True).items():
            value = self.prepare_value(value, bot=bot, files=files)
            new_json.update({key: value})
        form.add_field('meta', json.dumps(new_json), content_type='application/json')

        for key, value in files.items():
            form.add_field("file", value.read(bot), filename=value.filename or key)
        return form

    async def make_request(
        self, bot: Bot, method: ConnectMethod[ConnectType], type_request: str, path: str, timeout: Optional[int] = None
    ) -> ConnectType:
        session = await self.create_session()

        url = bot.base + path
        form = self.build_form_data(bot=bot, method=method)
        json_data = method.model_dump()

        try:
            if type_request == "POST-With-Attach":
                async with session.post(
                    auth=bot.auth, url=url, data=form,
                        timeout=self.timeout if timeout is None else timeout
                ) as resp:
                    raw_result = await resp.text()
            if type_request == "POST":
                async with session.post(
                    auth=bot.auth, url=url, json=json_data,
                        timeout=self.timeout if timeout is None else timeout
                ) as resp:
                    raw_result = await resp.text()
            elif type_request == "DELETE":
                async with session.delete(
                    auth=bot.auth, url=url, params=method.model_dump(exclude_none=True),
                        timeout=self.timeout if timeout is None else timeout
                ) as resp:
                    raw_result = await resp.text()
            elif type_request == "GET":
                async with session.get(
                    auth=bot.auth, url=url, params=method.model_dump(exclude_none=True),
                        timeout=self.timeout if timeout is None else timeout
                ) as resp:
                    raw_result = await resp.text()
            elif type_request == "PUT":
                async with session.put(
                    auth=bot.auth, url=url, json=json_data,
                        timeout=self.timeout if timeout is None else timeout
                ) as resp:
                    raw_result = await resp.text()
        except asyncio.TimeoutError:
            raise ConnectNetworkError(method=method, message="Request timeout error")
        except ClientError as e:
            raise ConnectNetworkError(method=method, message=f"{type(e).__name__}: {e}")
        response = self.check_response(
            bot=bot, method=method, status_code=resp.status, content=raw_result
        )
        return cast(ConnectType, response.result)

    async def stream_content(
        self,
        url: str,
        headers: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
        chunk_size: int = 65536,
        raise_for_status: bool = True,
    ) -> AsyncGenerator[bytes, None]:
        if headers is None:
            headers = {}

        session = await self.create_session()

        async with session.get(
            url, timeout=timeout, headers=headers, raise_for_status=raise_for_status
        ) as resp:
            async for chunk in resp.content.iter_chunked(chunk_size):
                yield chunk

    async def __aenter__(self) -> AiohttpSession:
        await self.create_session()
        return self
