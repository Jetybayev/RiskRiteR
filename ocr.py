import asyncio

import mss
import cv2 as cv
import numpy as np
import easyocr


class Ocr:
    window_position = None
    screen_ocr = None
    reader = None
    screenshot = None

    memory_targets = {}

    targets = []
    border_pixels = 2
    titlebar_pixels = 30

    def __init__(self):
        self.reader = easyocr.Reader(['ru'], gpu=False, verbose=False)

    def update_targets(self, targets):
        self.targets = targets
        return None

    def update_win_pos(self, window_position):
        self.window_position = window_position
        return None

    def memory_reset_ocr(self):
        self.memory_targets = {}
        return None

    async def get_screenshot(self, num_targets, left_shift, top_shift, width, height):
        with mss.mss() as stc:
            monitor = {
                'left': int(self.targets[num_targets][0]) + self.window_position[0] + self.border_pixels + left_shift,
                'top': int(self.targets[num_targets][1]) + self.window_position[1] + self.titlebar_pixels + top_shift,
                'width': width,
                'height': height
            }

        img = np.array(stc.grab(monitor))
        img = img[..., :3]
        img = np.ascontiguousarray(img)

        # cv.imwrite('12345.png', img)

        self.screenshot = img

    async def filter_ocr_distance_overview(self):
        image = self.screenshot
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image = cv.resize(image, None, fx=10, fy=10, interpolation=cv.INTER_CUBIC)

        kernel = np.ones((3, 3), np.uint8)
        image = cv.dilate(image, kernel, iterations=1)
        image = cv.erode(image, kernel, iterations=1)
        image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
        image = cv.medianBlur(image, 3)

        thresh, image = cv.threshold(image, 130, 255, cv.THRESH_BINARY)
        image = 255 - image
        image = cv.resize(image, (30, 40), interpolation=cv.INTER_AREA)

        # cv.imwrite('12345.png', image)

        text = self.reader.readtext(image, detail=0)
        if len(text) > 0:
            text = text[-1]
        else:
            text = ''
        return text

    async def main_ocr_asteroids_distance(self):
        dict_scan_position = {
            # left_shift, top_shift, width, height
            'm': [-23, 0, 8, 15],
            'k': [-29, 0, 6, 15],
            'units': [-36, 0, 7, 11],
            'tens': [-43, 0, 7, 11],
            'hundreds': [-50, 0, 7, 11],
            'thousands': [-61, 0, 7, 11],
            'units_km': [-43, 0, 8, 11],
            'tens_km': [-50, 0, 8, 11],
            'hundreds_km': [-61, 0, 8, 11]
        }

        if len(self.targets) > 6:
            self.targets = [self.targets[_] for _ in range(len(self.targets)) if 1 <= _ <= 5]

        for keys, values in dict_scan_position.items():
            for _, targets in enumerate(self.targets):

                task_1 = asyncio.create_task(self.get_screenshot(_, values[0], values[1], values[2], values[3]))
                await task_1
                task_2 = asyncio.create_task(self.filter_ocr_distance_overview())
                await task_2

                if task_2.result() != '':
                    self.memory_targets.setdefault(_, list())
                    if keys == 'm' or keys == 'k':
                        self.memory_targets[_].append(task_2.result())
                    elif keys == 'units' or keys == 'tens' or keys == 'hundreds' or keys == 'thousands':
                        if self.memory_targets[_].count('к') == 0 and self.memory_targets[_].count('К') == 0:
                            self.memory_targets[_].append(task_2.result())
                    elif keys == 'units_km' or keys == 'tens_km' or keys == 'hundreds_km':
                        if self.memory_targets[_].count('к') > 0 or self.memory_targets[_].count('К') > 0:
                            self.memory_targets[_].append(task_2.result())

        for _ in range(0, len(self.targets)):
            self.memory_targets[_].reverse()
            if self.memory_targets[_].count('к') == 0 and self.memory_targets[_].count('К') == 0:
                if len(self.memory_targets[_]) == 2:
                    self.memory_targets[_] = int(self.memory_targets[_][0])
                elif len(self.memory_targets[_]) == 3:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1])
                elif len(self.memory_targets[_]) == 4:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1] +
                                                 self.memory_targets[_][2])
                elif len(self.memory_targets[_]) == 5:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1] +
                                                 self.memory_targets[_][2] + self.memory_targets[_][3])
            elif self.memory_targets[_].count('к') > 0 or self.memory_targets[_].count('К') > 0:
                if len(self.memory_targets[_]) == 4:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1]) * 1000
                elif len(self.memory_targets[_]) == 5:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1] +
                                                 self.memory_targets[_][2]) * 1000

    async def main_ocr_npc_distance(self):
        dict_scan_position = {
            # left_shift, top_shift, width, height
            'm': [86, -3, 8, 15],
            'k': [80, -3, 7, 15],
            'units': [73, -3, 7, 11],
            'tens': [66, -3, 7, 11],
            'hundreds': [59, -3, 7, 11],
            'thousands': [48, -3, 7, 11],
            'units_km': [66, -3, 8, 11],
            'tens_km': [59, -3, 8, 11],
            'hundreds_km': [48, -3, 8, 11]
        }

        for keys, values in dict_scan_position.items():
            for _, targets in enumerate(self.targets):

                task_1 = asyncio.create_task(self.get_screenshot(_, values[0], values[1], values[2], values[3]))
                await task_1
                task_2 = asyncio.create_task(self.filter_ocr_distance_overview())
                await task_2

                if task_2.result() != '':
                    self.memory_targets.setdefault(_, list())
                    if keys == 'm' or keys == 'k':
                        self.memory_targets[_].append(task_2.result())
                    elif keys == 'units' or keys == 'tens' or keys == 'hundreds' or keys == 'thousands':
                        if self.memory_targets[_].count('к') == 0 and self.memory_targets[_].count('К') == 0:
                            self.memory_targets[_].append(task_2.result())
                    elif keys == 'units_km' or keys == 'tens_km' or keys == 'hundreds_km':
                        if self.memory_targets[_].count('к') > 0 or self.memory_targets[_].count('К') > 0:
                            self.memory_targets[_].append(task_2.result())

        for _ in range(0, len(self.targets)):
            self.memory_targets[_].reverse()
            if self.memory_targets[_].count('к') == 0 and self.memory_targets[_].count('К') == 0:
                if len(self.memory_targets[_]) == 2:
                    self.memory_targets[_] = int(self.memory_targets[_][0])
                elif len(self.memory_targets[_]) == 3:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1])
                elif len(self.memory_targets[_]) == 4:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1] +
                                                 self.memory_targets[_][2])
                elif len(self.memory_targets[_]) == 5:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1] +
                                                 self.memory_targets[_][2] + self.memory_targets[_][3])
            elif self.memory_targets[_].count('к') > 0 or self.memory_targets[_].count('К') > 0:
                if len(self.memory_targets[_]) == 4:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1]) * 1000
                elif len(self.memory_targets[_]) == 5:
                    self.memory_targets[_] = int(self.memory_targets[_][0] + self.memory_targets[_][1] +
                                                 self.memory_targets[_][2]) * 1000
