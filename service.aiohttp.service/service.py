import asyncio

import xbmc
from aiohttp import web, ClientSession

from lib.event_loop import get_running_loop


class Service:
    def __init__(self, host: str = 'localhost', port: int = 8080):
        self.host = host
        self.port = port

    @staticmethod
    async def hello(request):
        xbmc.log('AIOHTTP Application Request: !!!', xbmc.LOGDEBUG)

        async with ClientSession() as session:
            xbmc.log(f'AIOHTTP TEST running...', xbmc.LOGDEBUG)
            async with session.get('http://httpbin.org/get') as resp:
                await resp.text()

        text = f'Hello there! Wanna run a test? Ups ran it already...\nhttp://httpbin.org/get.resp={resp}'
        return web.Response(
            text=text)

    async def serve(self):
        xbmc.log(f'AIOHTTP Application Starting, http://{self.host}:{self.port}', xbmc.LOGDEBUG)
        app = web.Application()

        xbmc.log(f'AIOHTTP Adding route and handler "hello", http://{self.host}:{self.port}', xbmc.LOGDEBUG)
        app.add_routes([web.get('/', self.hello)])

        xbmc.log(f'AIOHTTP Creating runner, http://{self.host}:{self.port}', xbmc.LOGDEBUG)
        runner = web.AppRunner(app)

        xbmc.log(f'AIOHTTP Runner setup, http://{self.host}:{self.port}', xbmc.LOGDEBUG)
        await runner.setup()

        xbmc.log(f'AIOHTTP Creating site, http://{self.host}:{self.port}', xbmc.LOGDEBUG)
        site = web.TCPSite(runner, self.host, self.port)

        xbmc.log(f'AIOHTTP Starting site, http://{self.host}:{self.port}', xbmc.LOGDEBUG)
        await site.start()

        try:
            while True:
                await asyncio.sleep(4)
        except NameError:  # help, I'm gone!
            xbmc.log(f'AIOHTTP Shutting down, http://{self.host}:{self.port}', xbmc.LOGDEBUG)
            await runner.cleanup()


class Monitor(xbmc.Monitor):
    def run(self, host: str = 'localhost', port: int = 1081):
        xbmc.log(f'AIOHTTP getting event-loop, http://{host}:{port}', xbmc.LOGDEBUG)
        loop = get_running_loop()
        service = Service(host=host, port=port)
        loop.create_task(service.serve())
        while not self.abortRequested():
            if self.waitForAbort(1):
                break


xbmc.sleep(2500)
Monitor().run()
