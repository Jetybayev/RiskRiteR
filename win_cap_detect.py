import asyncio

import mss
import cv2 as cv
import numpy as np
import win32gui
import ctypes
from ctypes.wintypes import HWND, DWORD, RECT


class WindowCapture:
    window_name = None
    window_handle = None
    window_rect = (0, 0, 0, 0)
    border_pixels = 2
    titlebar_pixels = 30

    dwmapi = ctypes.WinDLL("dwmapi")
    rect = RECT()
    DMWA_EXTENDED_FRAME_BOUNDS = 9

    screenshot = None
    template = None
    rectangles = []

    temp_img_w = 0
    temp_img_h = 0

    def __init__(self, window_name):
        self.window_name = window_name

        if window_name == 'Desktop':
            self.window_handle = win32gui.GetDesktopWindow()
            self.window_rect = win32gui.GetWindowRect(self.window_handle)

        else:
            self.window_handle = win32gui.FindWindow(None, window_name)
            self.dwmapi.DwmGetWindowAttribute(HWND(self.window_handle), DWORD(self.DMWA_EXTENDED_FRAME_BOUNDS),
                                              ctypes.byref(self.rect), ctypes.sizeof(self.rect))
            self.window_rect = (self.rect.left, self.rect.top, self.rect.right, self.rect.bottom)

    def update_position_window(self):
        self.window_handle = win32gui.FindWindow(None, self.window_name)
        self.dwmapi.DwmGetWindowAttribute(HWND(self.window_handle), DWORD(self.DMWA_EXTENDED_FRAME_BOUNDS),
                                          ctypes.byref(self.rect), ctypes.sizeof(self.rect))
        self.window_rect = (self.rect.left, self.rect.top, self.rect.right, self.rect.bottom)
        return self.window_rect

    def update_template(self, template):
        if template is not None:
            self.template = cv.imread(template, cv.IMREAD_UNCHANGED)
        else:
            self.template = None

    @staticmethod
    def list_window_names():
        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(win_enum_handler, None)

    async def get_screenshot(self):
        with mss.mss() as sct:
            monitor = {
                'left': self.window_rect[0] + self.border_pixels,
                'top': self.window_rect[1] + self.titlebar_pixels,
                'width': self.window_rect[2] - self.window_rect[0] - self.border_pixels,
                'height': self.window_rect[3] - self.window_rect[1] - self.titlebar_pixels - self.border_pixels
            }

        img = np.array(sct.grab(monitor))
        img = img[..., :3]
        img = np.ascontiguousarray(img)
        self.screenshot = img

    async def find_img(self, threshold=0.99, method=cv.TM_CCORR_NORMED):
        temp_img_w = self.template.shape[1]
        temp_img_h = self.template.shape[0]

        result = cv.matchTemplate(self.screenshot, self.template, method)
        # cv.imshow('SSS', result)
        # cv.waitKey(1)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), temp_img_w, temp_img_h]
            rectangles.append(rect)
            rectangles.append(rect)

        self.rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.1)

    async def main(self):
        task_1 = asyncio.create_task(self.get_screenshot())
        await task_1
        if self.template is not None:
            task_2 = asyncio.create_task(self.find_img())
            await task_2
