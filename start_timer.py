import asyncio

from time import localtime, time
from random import randint


class TimeState:
    PAUSE = 0
    START = 1


class TimerWork:
    state = None
    local_time = []
    num_timer = None
    until_timer_end = None

    hours_list = []
    minutes_list = []
    timer_1 = []
    timer_2 = []
    timer_3 = []
    random_start = 0
    random_stop = 0
    weekend = 0

    def __init__(self, timer_1: list, timer_2: list, timer_3: list, random_start: int, random_stop: int, weekend: int):
        self.state = TimeState.PAUSE

        self.timer_1 = timer_1
        self.timer_2 = timer_2
        self.timer_3 = timer_3

        if random_start != 0:
            self.random_start = randint(-random_start, random_start)
        else:
            self.random_start = random_start

        if random_stop != 0:
            self.random_stop = randint(-random_stop, random_stop)
        else:
            self.random_stop = random_stop

        self.weekend = weekend

        if self.random_start == 0:
            self.hours_list = [
                [self.timer_1[0], self.timer_1[2]],
                [self.timer_2[0], self.timer_2[2]],
                [self.timer_3[0], self.timer_3[2]]
            ]
            self.minutes_list = [
                [self.timer_1[1], self.timer_1[3]],
                [self.timer_2[1], self.timer_2[3]],
                [self.timer_3[1], self.timer_3[3]]
            ]
        elif self.random_start < 0:
            if self.timer_1[1] - self.random_start < 0:
                self.timer_1[0] -= 1
                self.timer_1[1] = 60 - self.timer_1[1] - self.random_start
            else:
                self.timer_1[1] += self.random_start
            if self.timer_2[1] - self.random_start < 0:
                self.timer_2[0] -= 1
                self.timer_2[1] = 60 - self.timer_2[1] - self.random_start
            else:
                self.timer_2[1] += self.random_start
            if self.timer_3[1] - self.random_start < 0:
                self.timer_3[0] -= 1
                self.timer_3[1] = 60 - self.timer_3[1] - self.random_start
            else:
                self.timer_3[1] += self.random_start
            self.hours_list = [
                [self.timer_1[0], self.timer_1[2]],
                [self.timer_2[0], self.timer_2[2]],
                [self.timer_3[0], self.timer_3[2]]
            ]
            self.minutes_list = [
                [self.timer_1[1], self.timer_1[3]],
                [self.timer_2[1], self.timer_2[3]],
                [self.timer_3[1], self.timer_3[3]]
            ]
        elif self.random_start > 0:
            if self.timer_1[1] + self.random_start > 59:
                self.timer_1[0] += 1
                self.timer_1[1] = self.timer_1[1] + self.random_start - 60
            else:
                self.timer_1[1] += self.random_start
            if self.timer_2[1] + self.random_start > 59:
                self.timer_2[0] += 1
                self.timer_2[1] = self.timer_2[1] + self.random_start - 60
            else:
                self.timer_2[1] += self.random_start
            if self.timer_3[1] + self.random_start > 59:
                self.timer_3[0] += 1
                self.timer_3[1] = self.timer_3[1] + self.random_start - 60
            else:
                self.timer_3[1] += self.random_start
            self.hours_list = [
                [self.timer_1[0], self.timer_1[2]],
                [self.timer_2[0], self.timer_2[2]],
                [self.timer_3[0], self.timer_3[2]]
            ]
            self.minutes_list = [
                [self.timer_1[1], self.timer_1[3]],
                [self.timer_2[1], self.timer_2[3]],
                [self.timer_3[1], self.timer_3[3]]
            ]

        if self.random_stop == 0:
            self.hours_list = [
                [self.timer_1[0], self.timer_1[2]],
                [self.timer_2[0], self.timer_2[2]],
                [self.timer_3[0], self.timer_3[2]]
            ]
            self.minutes_list = [
                [self.timer_1[1], self.timer_1[3]],
                [self.timer_2[1], self.timer_2[3]],
                [self.timer_3[1], self.timer_3[3]]
            ]
        elif self.random_stop < 0:
            if self.timer_1[3] - self.random_stop < 0:
                self.timer_1[2] -= 1
                self.timer_1[3] = 60 - self.timer_1[3] - self.random_stop
            else:
                self.timer_1[3] += self.random_stop
            if self.timer_2[3] - self.random_stop < 0:
                self.timer_2[2] -= 1
                self.timer_2[3] = 60 - self.timer_2[3] - self.random_stop
            else:
                self.timer_2[3] += self.random_stop
            if self.timer_3[3] - self.random_stop < 0:
                self.timer_3[2] -= 1
                self.timer_3[3] = 60 - self.timer_3[3] - self.random_stop
            else:
                self.timer_3[3] += self.random_stop
            self.hours_list = [
                [self.timer_1[0], self.timer_1[2]],
                [self.timer_2[0], self.timer_2[2]],
                [self.timer_3[0], self.timer_3[2]]
            ]
            self.minutes_list = [
                [self.timer_1[1], self.timer_1[3]],
                [self.timer_2[1], self.timer_2[3]],
                [self.timer_3[1], self.timer_3[3]]
            ]
        elif self.random_stop > 0:
            if self.timer_1[3] + self.random_stop > 59:
                self.timer_1[2] += 1
                self.timer_1[3] = self.timer_1[3] + self.random_stop - 60
            else:
                self.timer_1[3] += self.random_stop
            if self.timer_2[3] + self.random_stop > 59:
                self.timer_2[2] += 1
                self.timer_2[3] = self.timer_2[3] + self.random_stop - 60
            else:
                self.timer_2[3] += self.random_stop
            if self.timer_3[3] + self.random_stop > 59:
                self.timer_3[2] += 1
                self.timer_3[3] = self.timer_3[3] + self.random_stop - 60
            else:
                self.timer_3[3] += self.random_stop
            self.hours_list = [
                [self.timer_1[0], self.timer_1[2]],
                [self.timer_2[0], self.timer_2[2]],
                [self.timer_3[0], self.timer_3[2]]
            ]
            self.minutes_list = [
                [self.timer_1[1], self.timer_1[3]],
                [self.timer_2[1], self.timer_2[3]],
                [self.timer_3[1], self.timer_3[3]]
            ]

    async def main(self):  # , weekday: list
        while True:
            await asyncio.sleep(1)

            if self.weekend == localtime()[6]:
                continue

            if self.state == TimeState.PAUSE:
                while True:
                    self.local_time.clear()
                    self.local_time = [localtime()[_] for _ in range(9) if _ == 3 or _ == 4]

                    if self.hours_list[0][0] * 60 + self.minutes_list[0][0] <= \
                            self.local_time[0] * 60 + self.local_time[1] < \
                            self.hours_list[0][1] * 60 + self.minutes_list[0][1]:

                        self.state = TimeState.START
                        self.num_timer = 0
                        break

                    elif self.hours_list[1][0] * 60 + self.minutes_list[1][0] <= \
                            self.local_time[0] * 60 + self.local_time[1] < \
                            self.hours_list[1][1] * 60 + self.minutes_list[1][1]:

                        self.state = TimeState.START
                        self.num_timer = 1
                        break

                    elif self.hours_list[2][0] * 60 + self.minutes_list[2][0] <= \
                            self.local_time[0] * 60 + self.local_time[1] < \
                            self.hours_list[2][1] * 60 + self.minutes_list[2][1]:

                        self.state = TimeState.START
                        self.num_timer = 2
                        break

                    await asyncio.sleep(60)

            elif self.state == TimeState.START:
                timestamp = int(time())
                while True:
                    self.until_timer_end = (timestamp + ((self.hours_list[self.num_timer][1] * 60 +
                                            self.minutes_list[self.num_timer][1]) -
                                            (self.local_time[0] * 60 + self.local_time[1])) * 60) - int(time())

                    if timestamp + ((self.hours_list[self.num_timer][1] * 60 + self.minutes_list[self.num_timer][1]) -
                                    (self.local_time[0] * 60 + self.local_time[1])) * 60 > int(time()):
                        pass
                    else:
                        self.state = TimeState.PAUSE
                        self.num_timer = None
                        break

                    await asyncio.sleep(60)
