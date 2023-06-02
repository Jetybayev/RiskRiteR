import asyncio

import random
import pyautogui as pag
from mouse_user import MouseUtils


class LogicState:

    START_CUSTOM_SETTINGS = 0
    KEYBOARD_SHORTCUTS = 1
    COMPLETION_CUSTOM_SETTINGS = 2
    CUSTOM_WINDOWS_STATION = 3
    SCAN_UNNECESSARY_MENU_DOCK = 4
    CLOSING_UNNECESSARY_MENU_DOCK = 5
    SCAN_UNNECESSARY_MENU_SPACE = 6
    CLOSING_UNNECESSARY_MENU_SPACE = 7
    CUSTOM_OVERVIEW = 8
    CUSTOM_WINDOWS_SPACE = 9
    SCAN_ADDITIONAL_UNNECESSARY_MENU_SPACE = 10
    CLOSING_ADDITIONAL_UNNECESSARY_MENU_SPACE = 11
    SCAN_ADDITIONAL_UNNECESSARY_MENU_DOCK = 12
    COMPLETION_CUSTOM_WINDOWS = 13
    STOP = 14


class LogicPositioning:
    state = None
    timestamp = None
    window_position = None

    targets = []
    border_pixels = 2
    titlebar_pixels = 30

    def __init__(self):
        self.state = LogicState.START_CUSTOM_SETTINGS

    def get_screen_position(self, pos):
        x = pos[0] + self.window_position[0] + self.border_pixels
        y = pos[1] + self.window_position[1] + self.titlebar_pixels
        return x, y

    def update_targets(self, targets):
        self.targets = targets
        return None

    def update_pos_win(self, window_position):
        self.window_position = window_position
        return None

    """ Специальные функции.========================================================================================"""

    async def basic_settings(self):
        pag.keyDown('esc')
        await asyncio.sleep(random.uniform(0.15, 0.35))
        pag.keyUp('esc')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((780, 179)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        for _ in range(382, 481, 98):
            MouseUtils.move_to(self.get_screen_position((1260, _)), 20, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1200, 420)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def reset_positions_windows(self):
        MouseUtils.move_to(self.get_screen_position((1180, 179)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1065, 245)), 5, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def left_column_menu_display_and_graphics(self):
        MouseUtils.move_to(self.get_screen_position((560, 179)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((560, 608)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((560, 631)), 10, 3)
        await asyncio.sleep(random.uniform(0.2, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((560, 703)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def middle_column_menu_display_and_graphics(self):
        for _ in range(245, 462, 24):
            MouseUtils.move_to(self.get_screen_position((870, _)), 5, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

        for _ in range(632, 663, 30):
            MouseUtils.move_to(self.get_screen_position((1025, _)), 5, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

    async def right_column_menu_display_and_graphics(self):
        MouseUtils.move_to(self.get_screen_position((1340, 323)), 15, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        for _ in range(359, 432, 36):
            MouseUtils.move_to(self.get_screen_position((1340, _)), 15, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1340, 467)), 15, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1265, 740)), 25, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def custom_menu_chats(self):
        MouseUtils.move_to(self.get_screen_position((650, 179)), 5, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((600, 269)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((570, 440)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((600, 489)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def custom_left_column_menu_sound(self):
        MouseUtils.move_to(self.get_screen_position((693, 179)), 5, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((600, 270)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((600, 332)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((722, 430)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((630, 430)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((750, 514)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((810, 514)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def custom_middle_column_menu_sound(self):
        MouseUtils.move_to(self.get_screen_position((900, 226)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1030, 248)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((940, 248)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1030, 360)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((940, 360)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def custom_right_column_menu_sound(self):
        MouseUtils.move_to(self.get_screen_position((1210, 225)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        for _ in range(287, 312, 24):
            MouseUtils.move_to(self.get_screen_position((1180, _)), 10, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

        for _ in range(420, 469, 48):
            MouseUtils.move_to(self.get_screen_position((1180, _)), 10, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

        for _ in range(564, 781, 24):
            MouseUtils.move_to(self.get_screen_position((1180, _)), 10, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

    async def window_management_keyboard(self):
        MouseUtils.move_to(self.get_screen_position((905, 180)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Список наблюдения: ALT + V"""

        MouseUtils.move_to(self.get_screen_position((700, 277)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('v')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('v')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((870, 602)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Прокрутка"""

        for _ in range(2):
            await asyncio.sleep(random.uniform(0.5, 0.9))
            for _ in range(7):
                pag.scroll(-100)
                await asyncio.sleep(random.uniform(0.015, 0.029))

        """Места: ALT + L"""

        MouseUtils.move_to(self.get_screen_position((700, 437)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('l')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('l')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Местные координаты: L"""

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('l')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('l')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Прокрутка"""

        for _ in range(3):
            await asyncio.sleep(random.uniform(0.5, 0.9))
            for _ in range(8):
                pag.scroll(-100)
                await asyncio.sleep(random.uniform(0.015, 0.029))

        """Схема кораблей: ALT + S"""

        MouseUtils.move_to(self.get_screen_position((700, 542)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('s')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('s')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((870, 602)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Штаб флота: ALT + Q"""

        MouseUtils.move_to(self.get_screen_position((700, 728)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('q')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('q')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

    async def common_keyboard(self):
        MouseUtils.move_to(self.get_screen_position((745, 219)), 3, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Покинуть станцию: SPACE"""

        MouseUtils.move_to(self.get_screen_position((700, 478)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('space')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('space')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((870, 602)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def ship_management_keyboard(self):
        MouseUtils.move_to(self.get_screen_position((850, 219)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Перейти к предыдущей цели: X"""

        MouseUtils.move_to(self.get_screen_position((700, 507)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        for _ in range(2):
            await asyncio.sleep(random.uniform(0.5, 0.9))
            for _ in range(6):
                pag.scroll(100)
                await asyncio.sleep(random.uniform(0.015, 0.029))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('x')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('x')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((870, 602)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Перейти к следующей цели: Z"""

        MouseUtils.move_to(self.get_screen_position((700, 529)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('z')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('z')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((870, 602)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def drone_control_keyboard(self):
        MouseUtils.move_to(self.get_screen_position((1135, 219)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Возврат дронов в отсек: R"""

        MouseUtils.move_to(self.get_screen_position((700, 319)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('r')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('r')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Запуск дронов: G"""

        MouseUtils.move_to(self.get_screen_position((700, 360)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('g')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('g')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def general_parameters(self):
        MouseUtils.move_to(self.get_screen_position((780, 179)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Задержка вывода подсказок"""

        MouseUtils.move_to(self.get_screen_position((663, 352)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((810, 352)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Прозрачность"""

        MouseUtils.move_to(self.get_screen_position((1407, 268)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1250, 269)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Прозрачность света"""

        MouseUtils.move_to(self.get_screen_position((1407, 313)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1250, 314)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('esc')
        await asyncio.sleep(random.uniform(0.15, 0.35))
        pag.keyUp('esc')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def custom_windows_station(self):
        MouseUtils.move_to(self.get_screen_position((1862, 35)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1735, 65)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Фиксируем панель неоком"""

        MouseUtils.move_to(self.get_screen_position((25, 740)), 0, 0)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 140, pag.position()[1] + 20), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна чатов"""

        MouseUtils.move_to(self.get_screen_position((300, 678)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((300, 767)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((472, 782)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((600, 705)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна склада"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('c')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('c')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((220, 297)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 16, pag.position()[1] + 37), 3, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((598, 331)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((750, 402)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна журнала"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('j')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('j')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1219, 500)), 2, 50)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1626, 500)), 2, 50)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1150, 651)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1150, 761)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((701, 358)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((662, 314)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((800, 742)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1558, 339)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('j')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('j')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Фиксируем окно Личное дело пилота"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('a')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('a')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1511, 148)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('a')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('a')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Фиксируем окно Кошелёк"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('w')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('w')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1269, 231)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('w')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('w')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Фиксируем окно Контакты"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('e')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('e')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1194, 281)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('e')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('e')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Настраиваем окно Торговая система"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('r')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('r')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((900, 123)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1000, 15)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((900, 886)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1000, 995)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1407, 500)), 2, 300)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1905, 500)), 2, 300)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((702, 800)), 1, 100)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((850, 700)), 2, 300)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((828, 103)), 3, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((900, 134)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1838, 35)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1720, 66)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((650, 495)), 50, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((650, 540)), 50, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((650, 565)), 50, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1050, 238)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1050, 639)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1630, 72)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна Заказы в торговой системе"""

        MouseUtils.move_to(self.get_screen_position((662, 500)), 2, 100)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((65, 500)), 2, 100)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((650, 752)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((680, 995)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((600, 258)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((700, 15)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1255, 500)), 2, 300)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1825, 500)), 2, 300)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1762, 44)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1750, 74)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1810, 43)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна Оптовая покупка"""

        MouseUtils.move_to(self.get_screen_position((1810, 70)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((950, 313)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((950, 15)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((950, 697)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((950, 995)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((704, 500)), 2, 300)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((510, 500)), 2, 300)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1154, 35)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1201, 35)), 3, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна Покупка товаров"""

        MouseUtils.move_to(self.get_screen_position((1070, 260)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 115, pag.position()[1] + 20), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1129, 459)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1177, 459)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('r')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('r')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Настройка окна Оснащение кораблей"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('f')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('f')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1854, 193)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1720, 223)), 30, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        for _ in range(400, 303, -24):
            MouseUtils.move_to(self.get_screen_position((1750, _)), 20, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('f')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('f')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Фиксируем окно База личного имущества"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('t')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('t')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1169, 307)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('t')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('t')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Фиксируем окно Выдача предметов"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('y')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('y')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1274, 204)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('y')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('y')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Фиксируем окно Почта"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('i')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('i')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1294, 231)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('i')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('i')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Фиксируем окно Места"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('l')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('l')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1119, 307)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 70), 30, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('l')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('l')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

    async def on_off_graphics(self):
        pag.keyDown('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.5))
        pag.keyDown('shift')
        await asyncio.sleep(random.uniform(0.8, 1.2))
        pag.keyDown('f9')
        await asyncio.sleep(random.uniform(0.2, 0.3))
        pag.keyUp('f9')
        await asyncio.sleep(random.uniform(0.3, 0.5))
        pag.keyUp('shift')
        await asyncio.sleep(random.uniform(0.3, 0.5))
        pag.keyUp('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))

    async def closing_unnecessary_menu(self, dock=True):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        if dock:
            pag.keyDown('space')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.keyUp('space')
            await asyncio.sleep(random.uniform(0.2, 0.4))

    async def move_to_side_up_monitor_and_click(self):
        MouseUtils.move_to(self.get_screen_position((1000, 140)), 300, 40)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def custom_overview(self):
        pag.keyDown('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('space')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('space')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Импортируем настройки из Документов из EVE/Overview"""

        MouseUtils.move_to(self.get_screen_position((1862, 209)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1700, 419)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1154, 224)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1040, 297)), 5, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((840, 780)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((900, 509)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1160, 504)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1185, 665)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1202, 223)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка позиции окна выбора и взаимодействия с целью"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('j')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('j')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1900, 100)), 2, 20)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1675, 100)), 2, 20)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1500, 100)), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 335, pag.position()[1] + 174), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1170, 362)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1170, 314)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1296, 210)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 70), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка позиции окна overview"""

        MouseUtils.move_to(self.get_screen_position((1610, 194)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1610, 314)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('j')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('j')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('j')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('j')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1862, 332)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] - 150, pag.position()[1] + 70), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Фиксируем окно дронов"""

        MouseUtils.move_to(self.get_screen_position((1862, 854)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] - 250, pag.position()[1] - 87), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def custom_overview_tab_mining(self):
        MouseUtils.move_to(self.get_screen_position((1413, 331)), 5, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1647, 363)), 0, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1605, 363)), 0, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1717, 363)), 0, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1900, 363)), 5, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1358, 331)), 5, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def custom_windows_space(self, custom_fleet=True):

        """Настройка позиции окна склада"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('c')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('c')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((220, 297)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 15, pag.position()[1] - 265), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((360, 20)), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0], pag.position()[1] + 173), 50, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((598, 210)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 70), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(1.1, 1.4))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

        """Настройка позиции окна местных координат"""

        pag.keyDown('l')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('l')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((860, 459)), 5, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 767, pag.position()[1] + 197), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((190, 638)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0], pag.position()[1] - 173), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((254, 485)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 70), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка позиции окна пеленгатора"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('d')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('d')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1857, 51)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('f9')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('f9')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((875, 345)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 182, pag.position()[1] - 17), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((940, 490)), 2, 20)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 286, pag.position()[1]), 2, 20)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1272, 331)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 70), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройки окна пеленгатора"""

        MouseUtils.move_to(self.get_screen_position((1170, 331)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 0, pag.position()[1] + 70), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Прокрутка"""

        for _ in range(2):
            await asyncio.sleep(random.uniform(0.5, 0.9))
            for _ in range(6):
                pag.scroll(-100)
                await asyncio.sleep(random.uniform(0.015, 0.029))

        await asyncio.sleep(random.uniform(0.5, 0.8))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1221, 650)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 50, pag.position()[1]), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1223, 359)), 0, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 85, pag.position()[1]), 2, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка позиции окна разведывательных зондов"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('p')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('p')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1857, 51)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('f9')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('f9')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((830, 320)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 578, pag.position()[1] - 291), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1540, 414)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0], pag.position()[1] - 100), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1734, 160)), 2, 20)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 168, pag.position()[1]), 2, 20)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1838, 36)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] - 130, pag.position()[1] + 70), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна разведывательных зондов"""

        MouseUtils.move_to(self.get_screen_position((1492, 59)), 0, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 20, pag.position()[1]), 0, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1612, 59)), 0, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 300, pag.position()[1]), 10, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна флота"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('q')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('q')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((950, 320)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 169, pag.position()[1] + 8), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((785, 710)), 30, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0], pag.position()[1] - 50), 30, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('d')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('d')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((538, 500)), 0, 10)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 37, pag.position()[1]), 0, 10)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((971, 340)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 70), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка флота"""

        if custom_fleet:
            MouseUtils.move_to(self.get_screen_position((641, 639)), 20, 5)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            for _ in range(1):
                MouseUtils.move_to(self.get_screen_position((800, 412)), 30, 5)
                await asyncio.sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='right')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='right')
                await asyncio.sleep(random.uniform(0.2, 0.4))

                MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1] + 143), 20, 3)
                await asyncio.sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='left')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='left')
                await asyncio.sleep(random.uniform(0.2, 0.4))

            counter_wings = 1
            for _ in range(448, 506, 57):
                MouseUtils.move_to(self.get_screen_position((800, _)), 20, 5)
                await asyncio.sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='right')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='right')
                await asyncio.sleep(random.uniform(0.2, 0.4))

                MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 40), 7, 2)
                await asyncio.sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='left')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='left')
                await asyncio.sleep(random.uniform(0.2, 0.4))

                pag.keyDown('W')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.keyUp('W')
                await asyncio.sleep(random.uniform(0.3, 0.6))
                pag.keyDown('i')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.keyUp('i')
                await asyncio.sleep(random.uniform(0.3, 0.6))
                pag.keyDown('n')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.keyUp('n')
                await asyncio.sleep(random.uniform(0.3, 0.6))
                pag.keyDown('g')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.keyUp('g')
                await asyncio.sleep(random.uniform(0.3, 0.6))
                pag.keyDown('_')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.keyUp('_')
                await asyncio.sleep(random.uniform(0.3, 0.6))
                pag.keyDown(f'{counter_wings}')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.keyUp(f'{counter_wings}')
                await asyncio.sleep(random.uniform(0.3, 0.6))
                pag.keyDown('enter')
                await asyncio.sleep(random.uniform(0.2, 0.4))
                pag.keyUp('enter')
                await asyncio.sleep(random.uniform(0.3, 0.6))

                counter_wings += 1

            for _ in range(505, 447, -57):
                for __ in range(1):
                    MouseUtils.move_to(self.get_screen_position((800, _)), 20, 5)
                    await asyncio.sleep(random.uniform(0.3, 0.6))

                    pag.mouseDown((pag.position()), button='right')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.mouseUp((pag.position()), button='right')
                    await asyncio.sleep(random.uniform(0.2, 0.4))

                    MouseUtils.move_to((pag.position()[0] + 80, pag.position()[1] + 60), 7, 2)
                    await asyncio.sleep(random.uniform(0.3, 0.6))

                    pag.mouseDown((pag.position()), button='left')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.mouseUp((pag.position()), button='left')
                    await asyncio.sleep(random.uniform(0.2, 0.4))

            counter_squad = 4
            for _ in range(577, 498, -78):
                for __ in range(_, _ - 21, -20):
                    MouseUtils.move_to(self.get_screen_position((720, __)), 20, 3)
                    await asyncio.sleep(random.uniform(0.3, 0.6))

                    pag.mouseDown((pag.position()), button='right')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.mouseUp((pag.position()), button='right')
                    await asyncio.sleep(random.uniform(0.2, 0.4))

                    MouseUtils.move_to((pag.position()[0] + 80, pag.position()[1] + 20), 7, 2)
                    await asyncio.sleep(random.uniform(0.3, 0.6))

                    pag.mouseDown((pag.position()), button='left')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.mouseUp((pag.position()), button='left')
                    await asyncio.sleep(random.uniform(0.2, 0.4))

                    pag.keyDown('s')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.keyUp('s')
                    await asyncio.sleep(random.uniform(0.3, 0.6))
                    pag.keyDown('q')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.keyUp('q')
                    await asyncio.sleep(random.uniform(0.3, 0.6))
                    pag.keyDown('u')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.keyUp('u')
                    await asyncio.sleep(random.uniform(0.3, 0.6))
                    pag.keyDown('a')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.keyUp('a')
                    await asyncio.sleep(random.uniform(0.3, 0.6))
                    pag.keyDown('d')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.keyUp('d')
                    await asyncio.sleep(random.uniform(0.3, 0.6))
                    pag.keyDown('_')
                    await asyncio.sleep(random.uniform(0.2, 0.4))
                    pag.keyUp('_')
                    await asyncio.sleep(random.uniform(0.3, 0.6))
                    if counter_squad < 10:
                        pag.keyDown(f'{counter_squad}')
                        await asyncio.sleep(random.uniform(0.2, 0.4))
                        pag.keyUp(f'{counter_squad}')
                        await asyncio.sleep(random.uniform(0.3, 0.6))
                        pag.keyDown('enter')
                        await asyncio.sleep(random.uniform(0.2, 0.4))
                        pag.keyUp('enter')
                        await asyncio.sleep(random.uniform(0.3, 0.6))
                    else:
                        pag.keyDown(f'{counter_squad // 10}')
                        await asyncio.sleep(random.uniform(0.2, 0.4))
                        pag.keyUp(f'{counter_squad // 10}')
                        await asyncio.sleep(random.uniform(0.3, 0.6))
                        pag.keyDown(f'{counter_squad % 10}')
                        await asyncio.sleep(random.uniform(0.2, 0.4))
                        pag.keyUp(f'{counter_squad % 10}')
                        await asyncio.sleep(random.uniform(0.3, 0.6))
                        pag.keyDown('enter')
                        await asyncio.sleep(random.uniform(0.2, 0.4))
                        pag.keyUp('enter')
                        await asyncio.sleep(random.uniform(0.3, 0.6))

                    counter_squad -= 1

            MouseUtils.move_to(self.get_screen_position((947, 339)), 2, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 375), 20, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to(self.get_screen_position((947, 339)), 2, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 279), 20, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            pag.keyDown('m')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.keyUp('m')
            await asyncio.sleep(random.uniform(0.3, 0.6))
            pag.keyDown('e')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.keyUp('e')
            await asyncio.sleep(random.uniform(0.3, 0.6))
            pag.keyDown('_')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.keyUp('_')
            await asyncio.sleep(random.uniform(0.3, 0.6))
            pag.keyDown('f')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.keyUp('f')
            await asyncio.sleep(random.uniform(0.3, 0.6))
            pag.keyDown('l')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.keyUp('l')
            await asyncio.sleep(random.uniform(0.3, 0.6))
            pag.keyDown('e')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.keyUp('e')
            await asyncio.sleep(random.uniform(0.3, 0.6))
            pag.keyDown('e')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.keyUp('e')
            await asyncio.sleep(random.uniform(0.3, 0.6))
            pag.keyDown('t')
            await asyncio.sleep(random.uniform(0.2, 0.4))
            pag.keyUp('t')
            await asyncio.sleep(random.uniform(0.3, 0.6))

            MouseUtils.move_to(self.get_screen_position((900, 546)), 20, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to(self.get_screen_position((915, 602)), 10, 5)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            """Настройка меню объявления флота"""

            MouseUtils.move_to(self.get_screen_position((947, 339)), 2, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 430), 20, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to(self.get_screen_position((1194, 459)), 2, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 20, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            """Левая колонка"""

            MouseUtils.move_to(self.get_screen_position((800, 714)), 20, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to(self.get_screen_position((800, 740)), 20, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            """Правая колонка"""

            MouseUtils.move_to(self.get_screen_position((1050, 502)), 20, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to(self.get_screen_position((1050, 633)), 20, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to(self.get_screen_position((1070, 695)), 20, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            MouseUtils.move_to(self.get_screen_position((910, 903)), 10, 5)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна списка наблюдения"""

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('v')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('v')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1000, 440)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 463, pag.position()[1] + 181), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((660, 685)), 2, 10)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 183, pag.position()[1]), 10, 10)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((450, 606)), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0], pag.position()[1] - 141), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((510, 485)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 70), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна карты системы"""

        pag.keyDown('f9')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('f9')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1127, 18)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to((pag.position()[0] + 20, pag.position()[1] + 40), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to((pag.position()[0] + 20, pag.position()[1] + 52), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1725, 600)), 2, 100)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((1037, 600)), 2, 100)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((520, 105)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((520, 15)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((196, 550)), 2, 100)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((319, 550)), 2, 100)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((670, 906)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((670, 661)), 100, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('f9')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('f9')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Настройка окна информации"""

        MouseUtils.move_to(self.get_screen_position((1600, 384)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.keyDown('t')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyUp('t')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((950, 219)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 391, pag.position()[1] - 40), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((754, 182)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Закрываем окна"""

        MouseUtils.move_to(self.get_screen_position((802, 182)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((557, 485)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('q')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('q')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('p')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('p')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('c')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('c')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        """Сохраняем координаты станции и фиксируем положение этого окна"""

        pag.keyDown('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('b')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('b')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.keyDown('*')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('*')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('*')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('*')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('space')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('space')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.keyDown('shift')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('d')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('d')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('o')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('o')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('c')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('c')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('k')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('k')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyUp('shift')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1064, 353)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 31), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((910, 650)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def steering_control(self):
        MouseUtils.move_to(self.get_screen_position((1030, 983)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1150, 638)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1150, 681)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1150, 764)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1150, 862)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1150, 959)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Режим перемещения сообщений"""

        MouseUtils.move_to(self.get_screen_position((817, 10)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 145, pag.position()[1]), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((770, 320)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] - 160, pag.position()[1] - 100), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1030, 983)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1150, 959)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        """Фиксируем список кораблей на прицеле"""

        MouseUtils.move_to(self.get_screen_position((1600, 384)), 20, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.keyDown('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.keyUp('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((984, 190)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to((pag.position()[0] + 350, pag.position()[1] - 180), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 150, pag.position()[1] + 20), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    async def closing_additional_unnecessary_menu(self, space=True, not_menu=False):
        if not_menu:
            pass
        else:
            MouseUtils.move_to(self.get_screen_position(self.targets[0]), 2, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

        if space:
            MouseUtils.move_to(self.get_screen_position((1600, 384)), 20, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.keyDown('d')
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.4))

            pag.keyUp('d')
            await asyncio.sleep(random.uniform(0.3, 0.6))

    async def exit_program(self):
        pag.keyDown('esc')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('esc')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1350, 820)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((900, 641)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((870, 677)), 20, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))

    """============================================================================================================="""
    async def main(self):
        if self.state == LogicState.START_CUSTOM_SETTINGS:
            task_1 = asyncio.create_task(self.basic_settings())
            await task_1
            task_2 = asyncio.create_task(self.reset_positions_windows())
            await task_2
            task_3 = asyncio.create_task(self.left_column_menu_display_and_graphics())
            await task_3
            task_4 = asyncio.create_task(self.middle_column_menu_display_and_graphics())
            await task_4
            task_5 = asyncio.create_task(self.right_column_menu_display_and_graphics())
            await task_5
            task_6 = asyncio.create_task(self.custom_menu_chats())
            await task_6
            task_7 = asyncio.create_task(self.custom_left_column_menu_sound())
            await task_7
            task_8 = asyncio.create_task(self.custom_middle_column_menu_sound())
            await task_8
            task_9 = asyncio.create_task(self.custom_right_column_menu_sound())
            await task_9
            self.state = LogicState.KEYBOARD_SHORTCUTS

        elif self.state == LogicState.KEYBOARD_SHORTCUTS:
            task_1 = asyncio.create_task(self.window_management_keyboard())
            await task_1
            task_2 = asyncio.create_task(self.common_keyboard())
            await task_2
            task_3 = asyncio.create_task(self.ship_management_keyboard())
            await task_3
            task_4 = asyncio.create_task(self.drone_control_keyboard())
            await task_4
            self.state = LogicState.COMPLETION_CUSTOM_SETTINGS

        elif self.state == LogicState.COMPLETION_CUSTOM_SETTINGS:
            task = asyncio.create_task(self.general_parameters())
            await task
            self.state = LogicState.CUSTOM_WINDOWS_STATION

        elif self.state == LogicState.CUSTOM_WINDOWS_STATION:
            task_1 = asyncio.create_task(self.custom_windows_station())
            await task_1
            task_2 = asyncio.create_task(self.on_off_graphics())
            await task_2
            self.state = LogicState.SCAN_UNNECESSARY_MENU_DOCK

        elif self.state == LogicState.SCAN_UNNECESSARY_MENU_DOCK:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicState.CLOSING_UNNECESSARY_MENU_DOCK

        elif self.state == LogicState.CLOSING_UNNECESSARY_MENU_DOCK:
            task_1 = asyncio.create_task(self.closing_unnecessary_menu())
            await task_1
            task_2 = asyncio.create_task(self.move_to_side_up_monitor_and_click())
            await task_2
            await asyncio.sleep(random.uniform(10, 15))
            self.state = LogicState.SCAN_UNNECESSARY_MENU_SPACE

        elif self.state == LogicState.SCAN_UNNECESSARY_MENU_SPACE:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicState.CLOSING_UNNECESSARY_MENU_SPACE

        elif self.state == LogicState.CLOSING_UNNECESSARY_MENU_SPACE:
            task = asyncio.create_task(self.closing_unnecessary_menu(dock=False))
            await task
            self.state = LogicState.CUSTOM_OVERVIEW

        elif self.state == LogicState.CUSTOM_OVERVIEW:
            task_1 = asyncio.create_task(self.custom_overview())
            await task_1
            task_2 = asyncio.create_task(self.custom_overview_tab_mining())
            await task_2
            self.state = LogicState.CUSTOM_WINDOWS_SPACE

        elif self.state == LogicState.CUSTOM_WINDOWS_SPACE:
            task_1 = asyncio.create_task(self.custom_windows_space())
            await task_1
            task_2 = asyncio.create_task(self.steering_control())
            await task_2
            self.state = LogicState.SCAN_ADDITIONAL_UNNECESSARY_MENU_SPACE

        elif self.state == LogicState.SCAN_ADDITIONAL_UNNECESSARY_MENU_SPACE:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicState.CLOSING_ADDITIONAL_UNNECESSARY_MENU_SPACE

        elif self.state == LogicState.CLOSING_ADDITIONAL_UNNECESSARY_MENU_SPACE:
            if len(self.targets) > 0:
                task_1 = asyncio.create_task(self.closing_additional_unnecessary_menu())
                await task_1
            else:
                task_2 = asyncio.create_task(self.closing_additional_unnecessary_menu(not_menu=True))
                await task_2
            await asyncio.sleep(random.uniform(10, 15))
            self.state = LogicState.SCAN_ADDITIONAL_UNNECESSARY_MENU_DOCK

        elif self.state == LogicState.SCAN_ADDITIONAL_UNNECESSARY_MENU_DOCK:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = LogicState.COMPLETION_CUSTOM_WINDOWS

        elif self.state == LogicState.COMPLETION_CUSTOM_WINDOWS:
            if len(self.targets) > 0:
                task = asyncio.create_task(self.closing_additional_unnecessary_menu(space=False))
                await task
                task_1 = asyncio.create_task(self.move_to_side_up_monitor_and_click())
                await task_1
            task_2 = asyncio.create_task(self.exit_program())
            await task_2
            self.state = LogicState.STOP
