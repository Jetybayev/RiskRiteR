import asyncio

import os
from dotenv import load_dotenv, find_dotenv
import cv2 as cv
from ocr import Ocr
from vision import Vision
from win_cap_detect import WindowCapture
from modes import Modes, ProgramMode
from logic_start import LoginPositioning, LogicLogin
from logic_custom_win import LogicPositioning, LogicState
from pause import Pause, LogicStatusPause
from logic_extraction import LogicExtraction, ExtractionState
from start_timer import TimerWork, TimeState


class MainProgram:
    window_name = None
    windows = None
    win_detect = None

    START_MODE = True
    DEBUG = False

    def __init__(self, window_name):
        self.window_name = window_name
        self.windows = ['Desktop', 'EVE', f"EVE - {self.window_name}"]
        self.win_detect = WindowCapture(None)

    async def main_connecting_logic(self):
        await asyncio.sleep(5)
        while True:
            await asyncio.sleep(1)

            if timer.state == TimeState.PAUSE:
                continue

            if timer.until_timer_end is not None and timer.until_timer_end < 1500:
                continue

            if pause.state == LogicStatusPause.ON:
                continue
            else:

                if self.START_MODE:
                    self.win_detect = WindowCapture(self.windows[0])
                    start_mode.update_pos_win(self.win_detect.window_rect)

                    while True:
                        await asyncio.sleep(0.1)
                        if pause.state == LogicStatusPause.ON:
                            break

                        if start_mode.state == LogicLogin.SCAN_START_LAUNCHER:
                            self.win_detect.update_template('templates/start/start_launcher.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            start_mode.update_targets(targets)
                            task_2 = asyncio.create_task(start_mode.main())
                            await task_2

                        elif start_mode.state == LogicLogin.START_LAUNCHER:
                            task = asyncio.create_task(start_mode.main())
                            await task

                        elif start_mode.state == LogicLogin.SCAN_START_GAME:
                            self.win_detect.update_template('templates/start/start_game.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            start_mode.update_targets(targets)
                            task_2 = asyncio.create_task(start_mode.main())
                            await task_2

                        elif start_mode.state == LogicLogin.START_GAME:
                            task = asyncio.create_task(start_mode.main())
                            await task

                        elif start_mode.state == LogicLogin.SCAN_LOCK_LAUNCHER:
                            self.win_detect.update_template('templates/start/lock_launcher.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            start_mode.update_targets(targets)
                            task_2 = asyncio.create_task(start_mode.main())
                            await task_2

                        elif start_mode.state == LogicLogin.LOCK_LAUNCHER:
                            task = asyncio.create_task(start_mode.main())
                            await task

                        elif start_mode.state == LogicLogin.STOP_LAUNCH:
                            task = asyncio.create_task(start_mode.main())
                            await task
                            # window change____________________________________________________________________________
                            cv.destroyAllWindows()
                            self.win_detect = WindowCapture(self.windows[1])
                            start_mode.update_pos_win(self.win_detect.window_rect)

                        elif start_mode.state == LogicLogin.SCAN_DETECT_GIFT:
                            self.win_detect.update_template('templates/start/detect_gift.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            start_mode.update_targets(targets)
                            task_2 = asyncio.create_task(start_mode.main())
                            await task_2

                        elif start_mode.state == LogicLogin.LOCK_GIFT:
                            task = asyncio.create_task(start_mode.main())
                            await task

                        elif start_mode.state == LogicLogin.CHECK_FALSE_GIFT:
                            self.win_detect.update_template('templates/start/detect_gift.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            start_mode.update_targets(targets)
                            task_2 = asyncio.create_task(start_mode.main())
                            await task_2

                        elif start_mode.state == LogicLogin.FINISH_LOCK_GIFT:
                            task = asyncio.create_task(start_mode.main())
                            await task

                        elif start_mode.state == LogicLogin.START_CHAR_MAIN:
                            task = asyncio.create_task(start_mode.main())
                            await task

                        elif start_mode.state == LogicLogin.STOP:
                            cv.destroyAllWindows()
                            self.START_MODE = False
                            break

                        if self.win_detect.screenshot is None:
                            continue

                        if self.DEBUG:
                            debug_image = vision.draw_rectangles(self.win_detect.screenshot, self.win_detect.rectangles)
                            cv.imshow('DEBUG', debug_image)

                        key = cv.waitKey(1)
                        if key == ord('q'):
                            cv.destroyAllWindows()
                            break

                # Мод настройки позиций окон___________________________________________________________________________

                if MODE.state == Modes.CUSTOM_WINDOWS:
                    self.win_detect = WindowCapture(self.windows[2])
                    custom_win_mode.update_pos_win(self.win_detect.window_rect)

                    while True:
                        await asyncio.sleep(0.1)
                        if custom_win_mode.state == LogicState.START_CUSTOM_SETTINGS:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.KEYBOARD_SHORTCUTS:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.COMPLETION_CUSTOM_SETTINGS:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.CUSTOM_WINDOWS_STATION:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.SCAN_UNNECESSARY_MENU_DOCK:
                            self.win_detect.update_template('templates/unnecessary_menu.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            custom_win_mode.update_targets(targets)
                            task_2 = asyncio.create_task(custom_win_mode.main())
                            await task_2

                        elif custom_win_mode.state == LogicState.CLOSING_UNNECESSARY_MENU_DOCK:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.SCAN_UNNECESSARY_MENU_SPACE:
                            self.win_detect.update_template('templates/unnecessary_menu.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            custom_win_mode.update_targets(targets)
                            task_2 = asyncio.create_task(custom_win_mode.main())
                            await task_2

                        elif custom_win_mode.state == LogicState.CLOSING_UNNECESSARY_MENU_SPACE:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.CUSTOM_OVERVIEW:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.CUSTOM_WINDOWS_SPACE:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.SCAN_ADDITIONAL_UNNECESSARY_MENU_SPACE:
                            self.win_detect.update_template('templates/additional_unnecessary_menu.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            custom_win_mode.update_targets(targets)
                            task_2 = asyncio.create_task(custom_win_mode.main())
                            await task_2

                        elif custom_win_mode.state == LogicState.CLOSING_ADDITIONAL_UNNECESSARY_MENU_SPACE:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.SCAN_ADDITIONAL_UNNECESSARY_MENU_DOCK:
                            self.win_detect.update_template('templates/additional_unnecessary_menu.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            custom_win_mode.update_targets(targets)
                            task_2 = asyncio.create_task(custom_win_mode.main())
                            await task_2

                        elif custom_win_mode.state == LogicState.COMPLETION_CUSTOM_WINDOWS:
                            task = asyncio.create_task(custom_win_mode.main())
                            await task

                        elif custom_win_mode.state == LogicState.STOP:
                            cv.destroyAllWindows()
                            break

                        if self.win_detect.screenshot is None:
                            continue

                        if self.DEBUG:
                            debug_image = vision.draw_rectangles(self.win_detect.screenshot, self.win_detect.rectangles)
                            cv.imshow('DEBUG', debug_image)

                        key = cv.waitKey(1)
                        if key == ord('q'):
                            cv.destroyAllWindows()
                            break

                # Мод добычи астероидов на Venture в hi-sec____________________________________________________________

                elif MODE.state == Modes.MINING_PROJECT_GREEN:
                    self.win_detect = WindowCapture(self.windows[2])
                    extraction_mode.update_pos_win(self.win_detect.window_rect)
                    ocr_logic.update_win_pos(self.win_detect.window_rect)

                    while True:
                        await asyncio.sleep(0.1)
                        if pause.state == LogicStatusPause.ON:
                            break

                        if timer.state == TimeState.START:
                            if timer.until_timer_end is not None and timer.until_timer_end < 1500:
                                extraction_mode.work_time_finish = True

                        if extraction_mode.state == ExtractionState.START_INITIALIZING:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_STATION_OR_SPACE:
                            self.win_detect.update_template('templates/button_exit_station.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SHIP_IN_STATION:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_STORAGE_AT_STATION:
                            self.win_detect.update_template('templates/detection_storage.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_FULL_ORE_HOLD_AT_STATION:
                            self.win_detect.update_template('templates/extract/empty_ore_hold.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.UNDOCK:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SHIP_IN_SPACE:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_LOCATION_IN_SPACE:
                            ship_location = [
                                'templates/Overview/use_pve.png',
                                'templates/Overview/use_extract.png',
                                'templates/Overview/use_navigation.png'
                            ]
                            for _ in range(len(ship_location)):
                                scan_ship_location = ship_location.pop(0)
                                ship_location.append(scan_ship_location)

                                self.win_detect.update_template(scan_ship_location)
                                await asyncio.sleep(0.1)
                                task_1 = asyncio.create_task(self.win_detect.main())
                                await task_1
                                targets = vision.get_click_center(self.win_detect.rectangles)
                                extraction_mode.update_targets(targets)
                                task_2 = asyncio.create_task(extraction_mode.main())
                                await task_2
                                if len(extraction_mode.targets) > 0:
                                    break

                        elif extraction_mode.state == ExtractionState.DETERMINATION_LOCATION_SHIP:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_STORAGE_IN_SPACE:
                            self.win_detect.update_template('templates/detection_storage.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_FULL_ORE_HOLD_IN_SPACE:
                            self.win_detect.update_template('templates/extract/full_ore_hold.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_LOCAL_COORDINATES:
                            self.win_detect.update_template('templates/bookmarks/local_coordinates.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_BOOKMARKS_DOCK_TO_STATION:
                            self.win_detect.update_template('templates/bookmarks/DOCK.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.GO_TO_STATION:
                            self.win_detect.update_template('templates/warp/if_true_go_warp_to_station.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.DOCKING:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_BOOKMARKS_TO_ASTEROIDS:
                            self.win_detect.update_template('templates/bookmarks/asteroid.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.GO_TO_BOOKMARKS_TO_ASTEROIDS:
                            self.win_detect.update_template('templates/warp/if_true_go_warp_to_station.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.MENU_BELT_SYSTEM:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_BELT_SYSTEM:
                            self.win_detect.update_template('templates/extract/asteroid_belt.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SELECT_BELT:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.GO_TO_WARP_DRIVE:
                            self.win_detect.update_template('templates/warp/vector_warp_drive.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.WARP_DRIVE:
                            self.win_detect.update_template('templates/warp/warp_drive.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_ASTEROIDS:
                            self.win_detect.update_template('templates/extract/detection_asteroids.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            targets_to_ocr = vision.get_click_left_up_rectangle(self.win_detect.rectangles)
                            ocr_logic.update_targets(targets_to_ocr)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_DISTANCE_TO_ASTEROIDS:
                            task_1 = asyncio.create_task(ocr_logic.main_ocr_asteroids_distance())
                            await task_1
                            targets_from_ocr = ocr_logic.memory_targets
                            extraction_mode.update_targets_ocr(targets_from_ocr)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2
                            ocr_logic.memory_reset_ocr()

                        elif extraction_mode.state == ExtractionState.MOVEMENT_TO_ASTEROIDS:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.START_EXTRACT:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_EXTRACT:
                            self.win_detect.update_template('templates/extract/detection_extract.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_SHIELD_STATUS:
                            self.win_detect.update_template('templates/full_ship_shield.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.READINESS_SHIP:
                            self.win_detect.update_template('templates/drone_bay.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_ASTEROIDS_FOR_SAVE_BOOKMARKS:
                            self.win_detect.update_template('templates/extract/detection_asteroids.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SAVE_BOOKMARKS_ASTEROIDS:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_NPC_IN_OVERVIEW:
                            self.win_detect.update_template('templates/NPC/frigates'
                                                            '/not_selected_not_lock_npc_overview.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            targets_to_ocr = vision.get_click_left_up_rectangle(self.win_detect.rectangles)
                            ocr_logic.update_targets(targets_to_ocr)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_DISTANCE_NPC:
                            task_1 = asyncio.create_task(ocr_logic.main_ocr_npc_distance())
                            await task_1
                            targets_from_ocr = ocr_logic.memory_targets
                            extraction_mode.update_targets_ocr(targets_from_ocr)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2
                            ocr_logic.memory_reset_ocr()

                        elif extraction_mode.state == ExtractionState.LOCK_NPC:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_SHIP_PRIME_LOCK_AND_SELECTED:
                            self.win_detect.update_template('templates/NPC/frigates/prime_selected_lock_npc.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_SHIP_LOCK_AND_SELECTED:
                            self.win_detect.update_template('templates/NPC/frigates/selected_lock_npc.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.SCAN_SHIP_LOCK:
                            self.win_detect.update_template('templates/NPC/frigates/lock_npc.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.KILL_NPC:
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                        elif extraction_mode.state == ExtractionState.SCAN_KILL_NPC:
                            self.win_detect.update_template('templates/NPC/frigates/prime_selected_lock_npc.png')
                            await asyncio.sleep(0.1)
                            task_1 = asyncio.create_task(self.win_detect.main())
                            await task_1
                            targets = vision.get_click_center(self.win_detect.rectangles)
                            extraction_mode.update_targets(targets)
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        elif extraction_mode.state == ExtractionState.STOP:
                            cv.destroyAllWindows()
                            break

                        elif extraction_mode.state == ExtractionState.TIMER_PAUSE:
                            extraction_mode.num_timer = timer.num_timer
                            task = asyncio.create_task(extraction_mode.main())
                            await task

                            if timer.num_timer == 2:
                                start_mode.state = LogicLogin.SCAN_START_LAUNCHER
                                extraction_mode.state = ExtractionState.START_INITIALIZING
                                self.START_MODE = True
                                self.win_detect = WindowCapture(self.windows[0])
                                break
                            else:
                                if extraction_mode.on_off_general_win is True:
                                    start_mode.state = LogicLogin.SCAN_START_LAUNCHER
                                    extraction_mode.state = ExtractionState.START_INITIALIZING
                                    self.START_MODE = True
                                    self.win_detect = WindowCapture(self.windows[0])
                                else:
                                    extraction_mode.state = ExtractionState.START_INITIALIZING
                                break

                        if self.win_detect.screenshot is None:
                            continue

                        if self.DEBUG:
                            debug_image = vision.draw_rectangles(self.win_detect.screenshot, self.win_detect.rectangles)
                            cv.imshow('DEBUG', debug_image)

                        key = cv.waitKey(1)
                        if key == ord('q'):
                            cv.destroyAllWindows()
                            break

                        # connection_lost
                        self.win_detect.update_template('templates/connection_lost.png')
                        await asyncio.sleep(0.1)
                        task_1 = asyncio.create_task(self.win_detect.main())
                        await task_1
                        connection_lost_target = vision.get_click_center(self.win_detect.rectangles)
                        if len(connection_lost_target) > 0:
                            extraction_mode.connection_lost_target = connection_lost_target
                            extraction_mode.state = ExtractionState.CONNECTION_LOST
                            task_2 = asyncio.create_task(extraction_mode.main())
                            await task_2

                        # the window closed
                        self.win_detect.update_template('templates/detection_win_game.png')
                        await asyncio.sleep(0.1)
                        task_1 = asyncio.create_task(self.win_detect.main())
                        await task_1
                        target_reboot = vision.get_click_center(self.win_detect.rectangles)
                        if len(target_reboot) == 0:
                            start_mode.state = LogicLogin.SCAN_START_LAUNCHER
                            extraction_mode.state = ExtractionState.START_INITIALIZING
                            self.win_detect = WindowCapture(self.windows[0])
                            self.START_MODE = True
                            break

                        if self.win_detect.screenshot is None:
                            continue

                        if self.DEBUG:
                            debug_image = vision.draw_rectangles(self.win_detect.screenshot, self.win_detect.rectangles)
                            cv.imshow('DEBUG', debug_image)

                        key = cv.waitKey(1)
                        if key == ord('q'):
                            cv.destroyAllWindows()
                            break


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    main_con_log = MainProgram(os.getenv('name_char'))

    vision = Vision()
    ocr_logic = Ocr()
    pause = Pause()
    timer = TimerWork(
        list(map(int, os.getenv('timer_1').split(','))),
        list(map(int, os.getenv('timer_2').split(','))),
        list(map(int, os.getenv('timer_3').split(','))),
        int(os.getenv('random_start')),
        int(os.getenv('random_stop')),
        int(os.getenv('weekend'))
    )

    MODE = ProgramMode(int(os.getenv('activ_mode')))
    start_mode = LoginPositioning()
    custom_win_mode = LogicPositioning()
    extraction_mode = LogicExtraction()

    async def main():
        task_main = asyncio.create_task(main_con_log.main_connecting_logic())
        task_timer = asyncio.create_task(timer.main())
        task_pause = asyncio.create_task(pause.main())
        await task_main
        await task_timer
        await task_pause

    asyncio.run(main())
