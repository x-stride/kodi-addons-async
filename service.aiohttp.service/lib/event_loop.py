import asyncio


def get_running_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        try:
            loop = asyncio.new_event_loop()
        except RuntimeError:
            loop = asyncio.get_running_loop()
    return loop

