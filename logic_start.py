import asyncio

import random
import pyautogui as pag
from mouse_user import MouseUtils


class LogicLogin:

    SCAN_START_LAUNCHER = 'SCAN_START_LAUNCHER'
    START_LAUNCHER = 'START_LAUNCHER'
    SCAN_START_GAME = 'SCAN_START_GAME'
    START_GAME = 'START_GAME'
    SCAN_LOCK_LAUNCHER = 'SCAN_LOCK_LAUNCHER'
    LOCK_LAUNCHER = 'LOCK_LAUNCHER'
    STOP_LAUNCH = 'STOP_LAUNCH'

    SCAN_DETECT_GIFT = 'SCAN_DETECT_GIFT'
    LOCK_GIFT = 'LOCK_GIFT'
    CHECK_FALSE_GIFT = 'CHECK_FALSE_GIFT'
    FINISH_LOCK_GIFT = 'FINISH_LOCK_GIFT'
    ESC_SETTINGS_GRAPHICS = 'ESC_SETTINGS_GRAPHICS'
    START_CHAR_MAIN = 'START_CHAR_MAIN'
    STOP = 'STOP'


class LoginPositioning:

    state = None
    timestamp = None
    window_position = None

    targets = []
    border_pixels = 2
    titlebar_pixels = 30

    def __init__(self):
        self.state = LogicLogin.SCAN_START_LAUNCHER

    def get_screen_position(self, pos):
        x = pos[0] + self.window_position[0] + self.border_pixels
        y = pos[1] + self.window_position[1] + self.titlebar_pixels
        return x, y

    def update_targets(self, targets):
        self.targets = targets

    def update_pos_win(self, window_position):
        self.window_position = window_position

    """ Специальные функции.========================================================================================"""
    async def start_launcher(self):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 5, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.145, 0.194))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.145, 0.194))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.145, 0.194))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.3, 0.6))

    async def start_game(self):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 25, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        await asyncio.sleep(random.uniform(15, 20))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.4, 0.7))
        pag.keyDown('tab')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('tab')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

    async def lock_launcher(self):
        MouseUtils.move_to(self.get_screen_position((self.targets[0][0] + 32, self.targets[0][1])), 0, 0)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.3, 0.6))

    async def success_gift(self, one_click=False):
        if one_click:
            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.3, 0.6))
        else:
            MouseUtils.move_to(self.get_screen_position((1340, 775)), 10, 5)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.3, 0.6))

    async def char_select_main(self):
        MouseUtils.move_to(self.get_screen_position((675, 500)), 100, 200)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.3, 0.6))

    async def removes_banner(self):
        MouseUtils.move_to(self.get_screen_position((1000, 140)), 300, 40)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def main(self):
        if self.state == LogicLogin.SCAN_START_LAUNCHER:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicLogin.START_LAUNCHER

        elif self.state == LogicLogin.START_LAUNCHER:
            task = asyncio.create_task(self.start_launcher())
            await task
            await asyncio.sleep(random.uniform(15, 20))
            self.state = LogicLogin.SCAN_START_GAME

        elif self.state == LogicLogin.SCAN_START_GAME:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicLogin.START_GAME

        elif self.state == LogicLogin.START_GAME:
            task = asyncio.create_task(self.start_game())
            await task
            self.state = LogicLogin.SCAN_LOCK_LAUNCHER

        elif self.state == LogicLogin.SCAN_LOCK_LAUNCHER:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicLogin.LOCK_LAUNCHER

        elif self.state == LogicLogin.LOCK_LAUNCHER:
            task = asyncio.create_task(self.lock_launcher())
            await task
            self.state = LogicLogin.STOP_LAUNCH

        # =============================================================================================================

        elif self.state == LogicLogin.STOP_LAUNCH:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicLogin.SCAN_DETECT_GIFT

        elif self.state == LogicLogin.SCAN_DETECT_GIFT:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.state = LogicLogin.LOCK_GIFT
            else:
                self.state = LogicLogin.START_CHAR_MAIN

        elif self.state == LogicLogin.LOCK_GIFT:
            task = asyncio.create_task(self.success_gift())
            await task
            await asyncio.sleep(random.uniform(3, 5))
            self.state = LogicLogin.CHECK_FALSE_GIFT

        elif self.state == LogicLogin.CHECK_FALSE_GIFT:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicLogin.FINISH_LOCK_GIFT

        elif self.state == LogicLogin.FINISH_LOCK_GIFT:
            if len(self.targets) > 0:
                task = asyncio.create_task(self.success_gift(one_click=True))
                await task
                self.state = LogicLogin.START_CHAR_MAIN
            else:
                self.state = LogicLogin.START_CHAR_MAIN

        elif self.state == LogicLogin.START_CHAR_MAIN:
            task_1 = asyncio.create_task(self.char_select_main())
            await task_1
            await asyncio.sleep(random.uniform(10, 15))
            task_2 = asyncio.create_task(self.removes_banner())
            await task_2
            await asyncio.sleep(random.uniform(3, 5))
            self.state = LogicLogin.STOP
