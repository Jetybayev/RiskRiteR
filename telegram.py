import asyncio

import mss
import cv2 as cv
import numpy as np
import requests
import pyautogui as pag
import win32api
from random import uniform


class TelegramPause:
    ON = 0
    OFF = 1


# узнаём из json файла chat_id
# url = f"https://api.telegram.org/bot{token}/getUpdates"
# pprint(requests.get(url).json())


class IodineTelegram:

    state = None

    screenshot = None
    window_position = None
    border_pixels = 2
    titlebar_pixels = 30

    rectangles = []
    template = None
    temp_img_w = 0
    temp_img_h = 0

    url = 'https://api.telegram.org/bot'

    token = None
    chat_id = None
    name_char = None

    def __init__(self, token, chat_id, name_char):
        self.token = token
        self.chat_id = chat_id
        self.name_char = name_char
        self.template = cv.imread('templates/chat_activity_detection.png', cv.IMREAD_UNCHANGED)
        self.state = TelegramPause.OFF

    def update_pos_win(self, window_position):
        self.window_position = window_position

    async def pause_on_off(self):
        pag.keyDown('k')
        await asyncio.sleep(uniform(0.2, 0.4))
        pag.keyUp('k')
        await asyncio.sleep(uniform(0.3, 0.6))

    async def get_screenshot(self):
        with mss.mss() as stc:
            monitor = {
                'left': self.window_position[0] + self.border_pixels + 65,
                'top': self.window_position[1] + self.titlebar_pixels + 800,
                'width': 310,
                'height': 130
            }

        img = np.array(stc.grab(monitor))
        img = img[..., :3]
        img = np.ascontiguousarray(img)
        self.screenshot = img
        cv.imwrite('send_chat_activ.png', img)

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

    async def send_screen(self):
        chat_activ = {'photo': open('send_chat_activ.png', 'rb')}
        send_screen_url = f'{self.url}{self.token}/sendPhoto?chat_id={self.chat_id}'
        requests.get(send_screen_url, files=chat_activ)

        send_name_char_url = f'{self.url}{self.token}/sendMessage?chat_id={self.chat_id}&text={self.name_char}'
        requests.get(send_name_char_url)

    async def main(self):
        await asyncio.sleep(120)
        while True:
            await asyncio.sleep(10)

            k_press = win32api.GetKeyState(0x4B)
            if k_press == 0:
                self.state = TelegramPause.OFF
            elif k_press == 1:
                self.state = TelegramPause.ON
            else:
                pass

            if self.state == TelegramPause.OFF:
                if self.window_position is not None:
                    task_1 = asyncio.create_task(self.get_screenshot())
                    await task_1
                    task_2 = asyncio.create_task(self.find_img())
                    await task_2

                    if len(self.rectangles) == 0:
                        task_3 = asyncio.create_task(self.send_screen())
                        await task_3
                        task_4 = asyncio.create_task(self.pause_on_off())
                        await task_4
