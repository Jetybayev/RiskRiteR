import asyncio

import win32api

# key = 'k'


class LogicStatusPause:
    ON = 0
    OFF = 1


class Pause:
    state = None
    telegram_pause = None

    def __init__(self):
        self.state = LogicStatusPause.OFF

    async def main(self):
        while True:
            await asyncio.sleep(1)

            k_press = win32api.GetKeyState(0x4B)
            if k_press == 0:
                self.state = LogicStatusPause.OFF
                self.telegram_pause = False
            elif k_press == 1:
                self.state = LogicStatusPause.ON
                if self.telegram_pause is not True:
                    print('run user pause')
                    await asyncio.sleep(10)
                elif self.telegram_pause is True:
                    print('run TelegramPause')
                    await asyncio.sleep(10)
                else:
                    pass
            else:
                pass
