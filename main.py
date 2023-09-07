import asyncio
import logging

import aiohttp
import requests
from aiohttp import web

logging.basicConfig(filename="output.log", filemode="w", level=logging.INFO)

ROUTE = "http://localhost:33337/"
LOGGER = logging.getLogger()


async def _create_and_start_webserver() -> web.TCPSite:
    app = web.Application(logger=LOGGER)

    async def _route(request: web.Request) -> web.Response:
        LOGGER.info("Received headers:-\n%s", request.headers)
        return web.Response(body=str(request.headers), status=201)

    app.add_routes([web.get("/", _route)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="localhost", port=33338)
    await site.start()

    return site


async def _async() -> None:
    async with aiohttp.ClientSession() as session, session.get(
        ROUTE, headers={"Authorization": "SomeAsyncAuthHere"}
    ) as resp:
        await resp.text()
        print("sent async request.")


def _sync() -> None:
    requests.get(ROUTE, headers={"Authorization": "SomeSyncAuthHere"})
    print("sent sync request.")


async def main() -> None:
    site = await _create_and_start_webserver()
    await _async()
    _sync()

    await site.stop()


asyncio.run(main())
