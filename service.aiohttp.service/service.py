import asyncio
import xbmc
from aiohttp import web


async def hello(request):
    xbmc.log('AIOHTTP Application Request: !!!', xbmc.LOGDEBUG)
    return web.Response(text="Hello, world\n")


async def serve():
    xbmc.log('AIOHTTP Application Starting', xbmc.LOGDEBUG)
    app = web.Application()
    xbmc.log('AIOHTTP Adding route and handler "hello"', xbmc.LOGDEBUG)
    app.add_routes([web.get('/', hello)])
    xbmc.log('AIOHTTP Creating runner', xbmc.LOGDEBUG)
    runner = web.AppRunner(app)
    xbmc.log('AIOHTTP runner setup', xbmc.LOGDEBUG)
    await runner.setup()
    xbmc.log('AIOHTTP Creating site', xbmc.LOGDEBUG)
    site = web.TCPSite(runner, '192.168.0.175', 1080)
    xbmc.log('AIOHTTP Starting site', xbmc.LOGDEBUG)
    await site.start()
    try:
        while True:
            await asyncio.sleep(4)
    except Exception:
        xbmc.log('AIOHTTP Shutting down', xbmc.LOGDEBUG)
        await runner.cleanup()


def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        try:
            loop = asyncio.new_event_loop()
        except RuntimeError:
            loop = asyncio.get_running_loop()
    return loop


class Monitor(xbmc.Monitor):
    def run(self):
        xbmc.log('AIOHTTP getting event-loop', xbmc.LOGDEBUG)
        loop = event_loop()
        loop.create_task(serve())
        while not self.abortRequested():
            if self.waitForAbort(1):
                break


if __name__ == '__main__':
    xbmc.sleep(1000)
    Monitor().run()
