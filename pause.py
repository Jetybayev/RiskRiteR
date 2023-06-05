import asyncio

import win32api

# key = 'k'


class LogicStatusPause:
    ON = 0
    OFF = 1


class Pause:
    state = None

    def __init__(self):
        self.state = LogicStatusPause.OFF

    async def main(self):
        while True:
            await asyncio.sleep(1)

            k_press = win32api.GetKeyState(0x4B)
            if k_press == 0:
                self.state = LogicStatusPause.OFF
            elif k_press == 1:
                self.state = LogicStatusPause.ON
            else:
                pass
