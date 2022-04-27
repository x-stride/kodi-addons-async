import asyncio
import xbmc


class Monitor(xbmc.Monitor):
    def run(self):
        loop = None
        try:
            loop = asyncio.get_running_loop()
        except Exception as e:
            loop = asyncio.new_event_loop()
            xbmc.log('ASYNCIO: service.python.loop created asyncio loop', xbmc.LOGWARNING)
        loop.run_forever()
        while not self.abortRequested():
            if self.waitForAbort(60):
                break


if __name__ == '__main__':
    Monitor().run()
