import asyncio

import random
import pyautogui as pag
from mouse_user import MouseUtils


class ExtractionState:
    START_INITIALIZING = 'START_INITIALIZING'
    SCAN_STATION_OR_SPACE = 'SCAN_STATION_OR_SPACE'

    SHIP_IN_STATION = 'SHIP_IN_STATION'
    SCAN_STORAGE_AT_STATION = 'SCAN_STORAGE_AT_STATION'
    SCAN_FULL_ORE_HOLD_AT_STATION = 'SCAN_FULL_ORE_HOLD_AT_STATION'
    UNDOCK = 'UNDOCK'

    SHIP_IN_SPACE = 'SHIP_IN_SPACE'
    SCAN_LOCATION_IN_SPACE = 'SCAN_LOCATION_IN_SPACE'
    DETERMINATION_LOCATION_SHIP = 'DETERMINATION_LOCATION_SHIP'

    SCAN_STORAGE_IN_SPACE = 'SCAN_STORAGE_IN_SPACE'
    SCAN_FULL_ORE_HOLD_IN_SPACE = 'SCAN_FULL_ORE_HOLD_IN_SPACE'
    SCAN_LOCAL_COORDINATES = 'SCAN_LOCAL_COORDINATES'

    SCAN_BOOKMARKS_DOCK_TO_STATION = 'SCAN_BOOKMARKS_DOCK_TO_STATION'
    GO_TO_STATION = 'GO_TO_STATION'
    DOCKING = 'DOCKING'

    SCAN_BOOKMARKS_TO_ASTEROIDS = 'SCAN_BOOKMARKS_TO_ASTEROIDS'
    GO_TO_BOOKMARKS_TO_ASTEROIDS = 'GO_TO_BOOKMARKS_TO_ASTEROIDS'

    MENU_BELT_SYSTEM = 'MENU_BELT_SYSTEM'
    SCAN_BELT_SYSTEM = 'SCAN_BELT_SYSTEM'
    SELECT_BELT = 'SELECT_BELT'

    GO_TO_WARP_DRIVE = 'GO_TO_WARP_DRIVE'
    WARP_DRIVE = 'WARP_DRIVE'

    SCAN_ASTEROIDS = 'SCAN_ASTEROIDS'
    SCAN_DISTANCE_TO_ASTEROIDS = 'SCAN_DISTANCE_TO_ASTEROIDS'
    MOVEMENT_TO_ASTEROIDS = 'MOVEMENT_TO_ASTEROIDS'
    START_EXTRACT = 'START_EXTRACT'
    SCAN_EXTRACT = 'SCAN_EXTRACT'
    SCAN_SHIELD_STATUS = 'SCAN_SHIELD_STATUS'
    READINESS_SHIP = 'READINESS_SHIP'

    SCAN_ASTEROIDS_FOR_SAVE_BOOKMARKS = 'SCAN_ASTEROIDS_FOR_SAVE_BOOKMARKS'
    SAVE_BOOKMARKS_ASTEROIDS = 'SAVE_BOOKMARKS_ASTEROIDS'

    SCAN_NPC_IN_OVERVIEW = 'SCAN_NPC_IN_OVERVIEW'
    SCAN_DISTANCE_NPC = 'SCAN_DISTANCE_NPC'
    LOCK_NPC = 'LOCK_NPC'
    SCAN_SHIP_PRIME_LOCK_AND_SELECTED = 'SCAN_SHIP_PRIME_LOCK_AND_SELECTED'
    SCAN_SHIP_LOCK_AND_SELECTED = 'SCAN_SHIP_LOCK_AND_SELECTED'
    SCAN_SHIP_LOCK = 'SCAN_SHIP_LOCK'
    KILL_NPC = 'KILL_NPC'
    SCAN_KILL_NPC = 'SCAN_KILL_NPC'

    TIMER_PAUSE = 'TIMER_PAUSE'
    CONNECTION_LOST = 'CONNECTION_LOST'
    STOP = 'STOP'


class LogicExtraction:
    new_akk = None

    connection_lost_target = []

    state = None
    window_position = None
    full_ore_hold = None
    not_asteroids_system = None

    attack_without_choice = False
    optional_mod = None
    select_ore_hold_at_station = True
    select_ore_hold_in_space = True
    ship_in_space = True
    go_to_station = False

    work_time_finish = False
    on_off_general_win = None
    num_timer = None

    memory_ship_location = []

    memory_targets_ocr = {}
    memory_scanned_targets = []

    memory_mining_belts = []
    active_belt = []

    quantity_work_module_extract = 0

    memory_mining_asteroids = []

    targets = []
    border_pixels = 2
    titlebar_pixels = 30

    def __init__(self, new_akk):
        self.state = ExtractionState.START_INITIALIZING
        if new_akk == "False":
            self.new_akk = False
        else:
            self.new_akk = True

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

    def update_targets_ocr(self, targets_ocr):
        self.memory_targets_ocr = targets_ocr
        return None

    """ Специальные функции.========================================================================================"""

    async def on_off_graphics(self):
        pag.keyDown('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('shift')
        await asyncio.sleep(random.uniform(0.5, 0.8))
        pag.keyDown('f9')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('f9')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('shift')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('ctrl')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def on_off_storage(self):
        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('c')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('c')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def select_corp_chat(self):

        if self.new_akk:
            MouseUtils.move_to(self.get_screen_position((205, 785)), 4, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.5, 0.8))

        MouseUtils.move_to(self.get_screen_position((448, 782)), 2, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

        MouseUtils.move_to(self.get_screen_position((550, 992)), 20, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def select_ore_hold(self, station=True):
        if station:
            MouseUtils.move_to(self.get_screen_position((160, 423)), 20, 3)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.5, 0.8))
        else:
            MouseUtils.move_to(self.get_screen_position((160, 301)), 20, )
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.5, 0.8))

    async def move_to_side_or_close_banner(self, click=False):
        MouseUtils.move_to(self.get_screen_position((1000, 140)), 300, 40)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        if click:
            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.5, 0.8))

    async def move_to_side_nearby_overview(self, click=False):
        MouseUtils.move_to(self.get_screen_position((1150, 550)), 150, 200)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        if click:
            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.5, 0.8))

    async def scroll_distance(self):
        for _ in range(random.randint(6, 8)):
            await asyncio.sleep(random.uniform(0.3, 0.6))
            for _ in range(random.randint(6, 8)):
                pag.scroll(100)
                await asyncio.sleep(random.uniform(0.02, 0.03))

    async def unloading_ore_hold(self):
        MouseUtils.move_to(self.get_screen_position((265, 395)), 10, 10)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.5, 0.8))

        MouseUtils.move_to((pag.position()[0] + 80, pag.position()[1] + 205), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

        MouseUtils.move_to(self.get_screen_position((265, 395)), 10, 10)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        MouseUtils.move_to(self.get_screen_position((160, 512)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def undock(self):
        pag.keyDown('space')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('space')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def shield_on_off(self):
        pag.keyDown('alt')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('f1')
        await asyncio.sleep(random.uniform(0.2, 0.4))
        pag.keyUp('f1')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyUp('alt')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def distance_calculation_npc(self):
        new_memory_npc = []
        for _ in range(len(self.memory_scanned_targets)):
            if self.memory_targets_ocr[_] < 16000:
                new_memory_npc.append(self.memory_scanned_targets[_])

        if len(new_memory_npc) == len(self.memory_scanned_targets):
            self.targets = new_memory_npc
            return True
        else:
            return False

    async def launch_drones(self):
        pag.keyDown('g')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('g')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def target_lock_npc(self):
        pag.keyDown('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        for _ in range(len(self.targets)):
            MouseUtils.move_to(self.get_screen_position((self.targets[_][0] + 150, self.targets[_][1])), 20, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.5))

        pag.keyUp('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))

    async def return_drones(self):
        pag.keyDown('r')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('r')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def kill_target_npc(self):
        if self.attack_without_choice:
            pag.keyDown('f')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.keyUp('f')
            await asyncio.sleep(random.uniform(0.5, 0.8))
        else:
            MouseUtils.move_to(self.get_screen_position((self.targets[0][0] + 150, self.targets[0][1])), 20, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.5))

            pag.keyDown('f')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.keyUp('f')
            await asyncio.sleep(random.uniform(0.5, 0.8))

    async def coordinates_on_off(self):
        pag.keyDown('l')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('l')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def extra_coordinate_menu(self):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def warp_bookmarks_to_0_km(self, warp_asteroid=False):
        MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1] + 20), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

        if warp_asteroid:
            MouseUtils.move_to((pag.position()[0] - 100, pag.position()[1] - 20), 2, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='right')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='right')
            await asyncio.sleep(random.uniform(0.2, 0.5))

            MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1] + 185), 2, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.5))

            pag.keyDown('enter')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.keyUp('enter')
            await asyncio.sleep(random.uniform(0.5, 0.8))

    async def docking(self):
        MouseUtils.move_to(self.get_screen_position((1600, 384)), 30, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.keyDown('d')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.5))

        pag.keyUp('d')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def select_overview_npc(self):
        MouseUtils.move_to(self.get_screen_position((1358, 331)), 3, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def select_overview_mining(self):
        MouseUtils.move_to(self.get_screen_position((1413, 331)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def select_overview_navigation(self):
        MouseUtils.move_to(self.get_screen_position((1723, 331)), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def select_menu_belt_system(self):
        MouseUtils.move_to(self.get_screen_position((89, 124)), 2, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.5))

        MouseUtils.move_to((pag.position()[0] + 260, pag.position()[1] + 96), 20, 2)
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def select_active_belt(self):
        self.active_belt.clear()
        self.active_belt.append(self.memory_mining_belts.pop(0))
        return None

    async def warp_to_activ_belt(self):
        MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1]), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position(self.active_belt[0]), 10, 2)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.5))

    async def distance_calculation_asteroids(self):
        new_memory_mining_asteroids = []
        for _ in range(len(self.memory_mining_asteroids)):
            if self.memory_targets_ocr[_] < 11000:
                new_memory_mining_asteroids.append(self.memory_mining_asteroids[_])

        if len(new_memory_mining_asteroids) >= 2:
            select_asteroid_1 = new_memory_mining_asteroids.pop(
                random.randint(0, len(new_memory_mining_asteroids) - 1)
            )
            select_asteroid_2 = new_memory_mining_asteroids.pop(
                random.randint(0, len(new_memory_mining_asteroids) - 1)
            )
            self.targets = [select_asteroid_1, select_asteroid_2]

        elif len(new_memory_mining_asteroids) == 1:
            select_asteroid_1 = new_memory_mining_asteroids.pop(
                random.randint(0, len(new_memory_mining_asteroids) - 1)
            )
            self.targets = [select_asteroid_1]

        if len(new_memory_mining_asteroids) > 0:
            return True
        else:
            return False

    async def movement_to_asteroid(self):
        MouseUtils.move_to(
            self.get_screen_position(
                self.memory_mining_asteroids[random.randint(0, len(self.memory_mining_asteroids) - 1)]
            ), 20, 2
        )
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.keyDown('q')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.5))

        pag.keyUp('q')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def afterburner_on_off(self):
        pag.keyDown('f4')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('f4')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def ship_stop(self):
        pag.keyDown('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))
        pag.keyDown('space')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('space')
        await asyncio.sleep(random.uniform(0.2, 0.5))
        pag.keyUp('ctrl')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def lock_asteroid(self):
        pag.keyDown('ctrl')
        await asyncio.sleep(random.uniform(0.3, 0.6))

        for _ in range(len(self.targets)):
            MouseUtils.move_to(self.get_screen_position(self.targets[_]), 10, 2)
            await asyncio.sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.175, 0.275))
            pag.mouseUp((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.2, 0.5))

        pag.keyUp('ctrl')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def extract_asteroids(self, all_module_extract_on=True):
        if all_module_extract_on:
            if len(self.targets) == 2:
                pag.keyDown('f1')
                await asyncio.sleep(random.uniform(0.175, 0.275))
                pag.keyUp('f1')
                await asyncio.sleep(random.uniform(0.2, 0.5))

                pag.keyDown('z')
                await asyncio.sleep(random.uniform(0.175, 0.275))
                pag.keyUp('z')
                await asyncio.sleep(random.uniform(0.2, 0.5))

                pag.keyDown('f2')
                await asyncio.sleep(random.uniform(0.175, 0.275))
                pag.keyUp('f2')
                await asyncio.sleep(random.uniform(0.5, 0.8))

            else:
                pag.keyDown('f1')
                await asyncio.sleep(random.uniform(0.175, 0.275))
                pag.keyUp('f1')
                await asyncio.sleep(random.uniform(0.2, 0.5))

                pag.keyDown('f2')
                await asyncio.sleep(random.uniform(0.175, 0.275))
                pag.keyUp('f2')
                await asyncio.sleep(random.uniform(0.5, 0.8))

        else:
            if self.quantity_work_module_extract == 1:
                random_f1_f2 = random.randint(1, 2)

                pag.keyDown(f'f{random_f1_f2}')
                await asyncio.sleep(random.uniform(0.175, 0.275))
                pag.keyUp(f'f{random_f1_f2}')
                await asyncio.sleep(random.uniform(0.5, 0.8))

            else:
                pag.keyDown('f1')
                await asyncio.sleep(random.uniform(0.175, 0.275))
                pag.keyUp('f1')
                await asyncio.sleep(random.uniform(0.2, 0.5))

                pag.keyDown('f2')
                await asyncio.sleep(random.uniform(0.175, 0.275))
                pag.keyUp('f2')
                await asyncio.sleep(random.uniform(0.5, 0.8))

    async def save_bookmarks_asteroid(self):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='right')
        await asyncio.sleep(random.uniform(0.2, 0.5))

        MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1] + 171), 10, 3)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.5))

        pag.keyDown('q')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('q')
        await asyncio.sleep(random.uniform(0.2, 0.5))
        pag.keyDown('w')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('w')
        await asyncio.sleep(random.uniform(0.2, 0.5))
        pag.keyDown('e')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('e')
        await asyncio.sleep(random.uniform(0.2, 0.5))

        pag.keyDown('enter')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.keyUp('enter')
        await asyncio.sleep(random.uniform(0.5, 0.8))

    async def connection_lost(self):
        MouseUtils.move_to(self.get_screen_position(self.connection_lost_target[0]), 50, 5)
        await asyncio.sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.175, 0.275))
        pag.mouseUp((pag.position()), button='left')
        await asyncio.sleep(random.uniform(0.2, 0.5))

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

    async def main(self):
        if self.state == ExtractionState.START_INITIALIZING:
            task_1 = asyncio.create_task(self.on_off_graphics())
            await task_1
            task_2 = asyncio.create_task(self.select_corp_chat())
            await task_2
            task_3 = asyncio.create_task(self.move_to_side_nearby_overview(click=True))
            await task_3
            self.state = ExtractionState.SCAN_STATION_OR_SPACE

        elif self.state == ExtractionState.SCAN_STATION_OR_SPACE:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.state = ExtractionState.SHIP_IN_STATION
            else:
                self.state = ExtractionState.SCAN_LOCATION_IN_SPACE

        elif self.state == ExtractionState.SHIP_IN_STATION:
            if self.work_time_finish is True:
                self.state = ExtractionState.TIMER_PAUSE
            else:
                if not self.not_asteroids_system is True:
                    self.state = ExtractionState.SCAN_STORAGE_AT_STATION
                else:
                    print('There are no asteroids in the system.')
                    self.state = ExtractionState.STOP

        elif self.state == ExtractionState.SCAN_STORAGE_AT_STATION:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) == 0:
                task_1 = asyncio.create_task(self.on_off_storage())
                await task_1
            if self.select_ore_hold_at_station:
                task_2 = asyncio.create_task(self.select_ore_hold())
                await task_2
                self.select_ore_hold_at_station = False
            self.state = ExtractionState.SCAN_FULL_ORE_HOLD_AT_STATION

        elif self.state == ExtractionState.SCAN_FULL_ORE_HOLD_AT_STATION:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) == 0:
                task_1 = asyncio.create_task(self.unloading_ore_hold())
                await task_1
            self.full_ore_hold = False
            self.state = ExtractionState.UNDOCK

        elif self.state == ExtractionState.UNDOCK:
            task_1 = asyncio.create_task(self.undock())
            await task_1
            task_2 = asyncio.create_task(self.move_to_side_nearby_overview())
            await task_2
            await asyncio.sleep(random.uniform(10, 15))
            self.state = ExtractionState.SHIP_IN_SPACE

        elif self.state == ExtractionState.SHIP_IN_SPACE:
            task_1 = asyncio.create_task(self.shield_on_off())
            await task_1
            if self.ship_in_space:
                task_2 = asyncio.create_task(self.scroll_distance())
                await task_2
                self.ship_in_space = False
            self.state = ExtractionState.SCAN_LOCATION_IN_SPACE

        elif self.state == ExtractionState.SCAN_LOCATION_IN_SPACE:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.memory_ship_location.append(self.targets)
            if len(self.targets) > 0:
                self.state = ExtractionState.DETERMINATION_LOCATION_SHIP

        elif self.state == ExtractionState.DETERMINATION_LOCATION_SHIP:
            if len(self.memory_ship_location) == 3:
                if self.go_to_station is False:
                    self.optional_mod = 'Navigation'
                    self.state = ExtractionState.SCAN_STORAGE_IN_SPACE
                else:
                    self.state = ExtractionState.DOCKING
            elif len(self.memory_ship_location) == 2:
                self.optional_mod = 'Extract'
                self.state = ExtractionState.SCAN_EXTRACT
            elif len(self.memory_ship_location) == 1:
                self.optional_mod = 'PVE'
                self.state = ExtractionState.SCAN_NPC_IN_OVERVIEW
            self.memory_ship_location = []

        elif self.state == ExtractionState.SCAN_STORAGE_IN_SPACE:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) == 0:
                task_1 = asyncio.create_task(self.on_off_storage())
                await task_1
            if self.select_ore_hold_in_space:
                task_2 = asyncio.create_task(self.select_ore_hold(station=False))
                await task_2
                task_3 = asyncio.create_task(self.move_to_side_nearby_overview())
                await task_3
                self.select_ore_hold_in_space = False
            self.state = ExtractionState.SCAN_FULL_ORE_HOLD_IN_SPACE

        elif self.state == ExtractionState.SCAN_FULL_ORE_HOLD_IN_SPACE:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if self.optional_mod == 'Navigation':
                if len(self.targets) == 0:
                    self.full_ore_hold = False
                else:
                    self.full_ore_hold = True
                self.state = ExtractionState.SCAN_LOCAL_COORDINATES
            elif self.optional_mod == 'Extract':
                if len(self.targets) == 0:
                    self.full_ore_hold = False
                    self.state = ExtractionState.SCAN_ASTEROIDS
                else:
                    self.full_ore_hold = True
                    self.state = ExtractionState.SCAN_ASTEROIDS_FOR_SAVE_BOOKMARKS

        elif self.state == ExtractionState.SCAN_LOCAL_COORDINATES:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) == 0:
                task = asyncio.create_task(self.coordinates_on_off())
                await task
            if self.full_ore_hold:
                self.state = ExtractionState.SCAN_BOOKMARKS_DOCK_TO_STATION
            else:
                self.state = ExtractionState.SCAN_BOOKMARKS_TO_ASTEROIDS

        elif self.state == ExtractionState.SCAN_BOOKMARKS_DOCK_TO_STATION:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            task_1 = asyncio.create_task(self.extra_coordinate_menu())
            await task_1
            self.state = ExtractionState.GO_TO_STATION

        elif self.state == ExtractionState.GO_TO_STATION:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                task = asyncio.create_task(self.warp_bookmarks_to_0_km())
                await task
                self.optional_mod = 'Navigation'
                task_1 = asyncio.create_task(self.select_overview_navigation())
                await task_1
                task_2 = asyncio.create_task(self.move_to_side_nearby_overview())
                await task_2
                self.go_to_station = True
                self.state = ExtractionState.GO_TO_WARP_DRIVE
                await asyncio.sleep(random.uniform(0.5, 0.8))

        elif self.state == ExtractionState.DOCKING:
            task = asyncio.create_task(self.docking())
            await task
            await asyncio.sleep(random.uniform(10, 15))
            self.go_to_station = False
            self.state = ExtractionState.SCAN_STATION_OR_SPACE

        elif self.state == ExtractionState.SCAN_BOOKMARKS_TO_ASTEROIDS:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                task_1 = asyncio.create_task(self.extra_coordinate_menu())
                await task_1
                self.state = ExtractionState.GO_TO_BOOKMARKS_TO_ASTEROIDS
            else:
                self.state = ExtractionState.MENU_BELT_SYSTEM

        elif self.state == ExtractionState.GO_TO_BOOKMARKS_TO_ASTEROIDS:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                task_1 = asyncio.create_task(self.warp_bookmarks_to_0_km(warp_asteroid=True))
                await task_1
                task_2 = asyncio.create_task(self.select_overview_npc())
                await task_2
                self.state = ExtractionState.GO_TO_WARP_DRIVE
                await asyncio.sleep(random.uniform(0.5, 0.8))
            else:
                task_3 = asyncio.create_task(self.select_overview_npc())
                await task_3
                self.state = ExtractionState.SCAN_LOCATION_IN_SPACE
            self.optional_mod = 'PVE'
            task_4 = asyncio.create_task(self.move_to_side_nearby_overview(click=True))
            await task_4

        elif self.state == ExtractionState.MENU_BELT_SYSTEM:
            task = asyncio.create_task(self.select_menu_belt_system())
            await task
            if len(self.active_belt) == 0:
                self.state = ExtractionState.SCAN_BELT_SYSTEM
            else:
                self.state = ExtractionState.SELECT_BELT

        elif self.state == ExtractionState.SCAN_BELT_SYSTEM:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.memory_mining_belts = self.targets
            self.state = ExtractionState.SELECT_BELT

        elif self.state == ExtractionState.SELECT_BELT:
            if len(self.memory_mining_belts) > 0:
                task_1 = asyncio.create_task(self.select_active_belt())
                await task_1
                task_2 = asyncio.create_task(self.warp_to_activ_belt())
                await task_2
                task_3 = asyncio.create_task(self.select_overview_npc())
                await task_3
                task_4 = asyncio.create_task(self.move_to_side_nearby_overview(click=True))
                await task_4
                self.optional_mod = 'PVE'
                self.state = ExtractionState.GO_TO_WARP_DRIVE
                await asyncio.sleep(random.uniform(0.5, 0.8))
            else:
                task_5 = asyncio.create_task(self.select_overview_navigation())
                await task_5
                task_6 = asyncio.create_task(self.move_to_side_nearby_overview())
                await task_6
                self.optional_mod = 'Navigation'
                self.not_asteroids_system = True
                self.full_ore_hold = True
                self.state = ExtractionState.SCAN_LOCATION_IN_SPACE

        elif self.state == ExtractionState.GO_TO_WARP_DRIVE:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.state = ExtractionState.GO_TO_WARP_DRIVE
            else:
                self.state = ExtractionState.WARP_DRIVE

        elif self.state == ExtractionState.WARP_DRIVE:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.state = ExtractionState.WARP_DRIVE
            else:
                self.state = ExtractionState.SCAN_LOCATION_IN_SPACE

        elif self.state == ExtractionState.SCAN_ASTEROIDS:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if self.quantity_work_module_extract != 0:
                self.state = ExtractionState.START_EXTRACT
            else:
                if 6 > len(self.targets) > 0:
                    self.memory_mining_asteroids = self.targets
                elif len(self.targets) > 6:
                    self.memory_mining_asteroids = [self.targets[_] for _ in range(len(self.targets)) if 1 <= _ <= 5]
                    self.state = ExtractionState.SCAN_DISTANCE_TO_ASTEROIDS
                else:
                    self.state = ExtractionState.SCAN_LOCAL_COORDINATES

        elif self.state == ExtractionState.SCAN_DISTANCE_TO_ASTEROIDS:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = ExtractionState.MOVEMENT_TO_ASTEROIDS

        elif self.state == ExtractionState.MOVEMENT_TO_ASTEROIDS:
            task_1 = asyncio.create_task(self.distance_calculation_asteroids())
            await task_1
            if task_1.result():
                self.state = ExtractionState.START_EXTRACT
            else:
                task_2 = asyncio.create_task(self.movement_to_asteroid())
                await task_2
                task_3 = asyncio.create_task(self.afterburner_on_off())
                await task_3
                task_4 = asyncio.create_task(self.move_to_side_nearby_overview(click=True))
                await task_4
                await asyncio.sleep(random.uniform(10, 12))
                task_5 = asyncio.create_task(self.afterburner_on_off())
                await task_5
                await asyncio.sleep(random.uniform(8, 12))
                task_6 = asyncio.create_task(self.ship_stop())
                await task_6
                self.state = ExtractionState.SCAN_DISTANCE_TO_ASTEROIDS

        elif self.state == ExtractionState.START_EXTRACT:
            if self.quantity_work_module_extract == 2:
                task_1 = asyncio.create_task(self.extract_asteroids(all_module_extract_on=False))
                await task_1
            if self.quantity_work_module_extract == 0:
                task_2 = asyncio.create_task(self.lock_asteroid())
                await task_2
                task_3 = asyncio.create_task(self.move_to_side_nearby_overview())
                await task_3
                await asyncio.sleep(random.uniform(3, 5))
                task_4 = asyncio.create_task(self.extract_asteroids())
                await task_4
            elif self.quantity_work_module_extract == 1:
                task_5 = asyncio.create_task(self.extract_asteroids(all_module_extract_on=False))
                await task_5
                self.quantity_work_module_extract = 2
            self.state = ExtractionState.SCAN_EXTRACT

        elif self.state == ExtractionState.SCAN_EXTRACT:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if self.quantity_work_module_extract == 2:
                if len(self.targets) == 2:
                    self.quantity_work_module_extract = 0
                    self.state = ExtractionState.SCAN_SHIELD_STATUS
                else:
                    self.quantity_work_module_extract = 2
                    self.state = ExtractionState.START_EXTRACT
            else:
                if len(self.targets) == 2:
                    self.state = ExtractionState.SCAN_SHIELD_STATUS
                else:
                    self.quantity_work_module_extract = len(self.targets)
                    self.state = ExtractionState.SCAN_STORAGE_IN_SPACE

        elif self.state == ExtractionState.SCAN_SHIELD_STATUS:
            if len(self.targets) == 0:
                task_1 = asyncio.create_task(self.select_overview_npc())
                await task_1
                task_2 = asyncio.create_task(self.move_to_side_nearby_overview())
                await task_2
                self.state = ExtractionState.SCAN_NPC_IN_OVERVIEW
            else:
                self.state = ExtractionState.READINESS_SHIP

        elif self.state == ExtractionState.READINESS_SHIP:
            if len(self.targets) > 0:
                self.state = ExtractionState.SCAN_EXTRACT
            else:
                task_1 = asyncio.create_task(self.select_overview_navigation())
                await task_1
                task_2 = asyncio.create_task(self.move_to_side_nearby_overview())
                await task_2
                self.optional_mod = 'Navigation'
                self.not_asteroids_system = True
                self.full_ore_hold = True
                self.state = ExtractionState.SCAN_LOCATION_IN_SPACE

        elif self.state == ExtractionState.SCAN_ASTEROIDS_FOR_SAVE_BOOKMARKS:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                if len(self.targets) > 6:
                    self.targets = [self.targets[_] for _ in range(len(self.targets)) if 1 <= _ <= 5]
                self.state = ExtractionState.SAVE_BOOKMARKS_ASTEROIDS
            else:
                self.state = ExtractionState.SCAN_BOOKMARKS_DOCK_TO_STATION

        elif self.state == ExtractionState.SAVE_BOOKMARKS_ASTEROIDS:
            task = asyncio.create_task(self.save_bookmarks_asteroid())
            await task
            self.state = ExtractionState.SCAN_LOCAL_COORDINATES

        elif self.state == ExtractionState.SCAN_NPC_IN_OVERVIEW:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.memory_scanned_targets = self.targets
                self.state = ExtractionState.SCAN_DISTANCE_NPC
            else:
                self.optional_mod = 'Extract'
                task_1 = asyncio.create_task(self.select_overview_mining())
                await task_1
                task_2 = asyncio.create_task(self.move_to_side_nearby_overview())
                await task_2
                self.state = ExtractionState.READINESS_SHIP

        elif self.state == ExtractionState.SCAN_DISTANCE_NPC:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            self.state = ExtractionState.LOCK_NPC

        elif self.state == ExtractionState.LOCK_NPC:
            task_1 = asyncio.create_task(self.distance_calculation_npc())
            await task_1
            await asyncio.sleep(random.uniform(1, 3))

            if task_1.result():
                task_2 = asyncio.create_task(self.launch_drones())
                await task_2
                task_3 = asyncio.create_task(self.target_lock_npc())
                await task_3
                task_4 = asyncio.create_task(self.move_to_side_nearby_overview())
                await task_4
                await asyncio.sleep(random.uniform(3, 5))
                self.state = ExtractionState.SCAN_SHIP_PRIME_LOCK_AND_SELECTED
            else:
                self.state = ExtractionState.SCAN_DISTANCE_NPC

        elif self.state == ExtractionState.SCAN_SHIP_PRIME_LOCK_AND_SELECTED:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.attack_without_choice = True
                self.state = ExtractionState.KILL_NPC
            else:
                self.state = ExtractionState.SCAN_SHIP_LOCK_AND_SELECTED

        elif self.state == ExtractionState.SCAN_SHIP_LOCK_AND_SELECTED:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.state = ExtractionState.KILL_NPC
            else:
                self.state = ExtractionState.SCAN_SHIP_LOCK

        elif self.state == ExtractionState.SCAN_SHIP_LOCK:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.state = ExtractionState.KILL_NPC
            else:
                task = asyncio.create_task(self.return_drones())
                await task
                self.state = ExtractionState.SCAN_NPC_IN_OVERVIEW

        elif self.state == ExtractionState.KILL_NPC:
            task_1 = asyncio.create_task(self.kill_target_npc())
            await task_1
            task_2 = asyncio.create_task(self.move_to_side_nearby_overview())
            await task_2
            self.attack_without_choice = False
            self.state = ExtractionState.SCAN_KILL_NPC

        elif self.state == ExtractionState.SCAN_KILL_NPC:
            await asyncio.sleep(random.uniform(0.5, 0.8))
            if len(self.targets) > 0:
                self.state = ExtractionState.SCAN_KILL_NPC
            else:
                self.state = ExtractionState.SCAN_SHIP_PRIME_LOCK_AND_SELECTED

        elif self.state == ExtractionState.TIMER_PAUSE:
            if self.num_timer == 2:
                task = asyncio.create_task(self.exit_program())
                await task
            else:
                self.on_off_general_win = random.choice([True, False])
                if self.on_off_general_win:
                    task = asyncio.create_task(self.exit_program())
                    await task

        elif self.state == ExtractionState.CONNECTION_LOST:
            task = asyncio.create_task(self.connection_lost())
            await task
