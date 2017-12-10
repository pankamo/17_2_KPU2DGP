from pico2d import *

import random

import FlyingState

class JellyBear:

    image = None
    PIXEL_PER_METER = 108
    RUNNING_SPEED_KMPH = 0
    RUNNING, EXPLODED = 0, 1

    def __init__(self):

        self.canvas_width = get_canvas_width()

        self.RUNNING_SPEED_KMPH = -(random.randint(20,80))
        if self.image == None :
            self.image = load_image('./Images/TempBear.png')
        self.x = random.randint(self.canvas_width // 2, self.canvas_width + 500)
        self.y = 100
        self.state = self.RUNNING

    def update(self, frame_time):
        if self.state == self.RUNNING :
            self.RUNNING_SPEED_MPM = (self.RUNNING_SPEED_KMPH * 1000) / 60
            self.RUNNING_SPEED_MPS = self.RUNNING_SPEED_MPM / 60
            self.RUNNING_SPEED_PPS = self.RUNNING_SPEED_MPS * self.PIXEL_PER_METER
            distance = self.RUNNING_SPEED_PPS * frame_time
            self.x += distance

            if self.x < -540:
                self.state = self.EXPLODED

            if self.x > 1620:
                self.state = self.EXPLODED

        if self.state == self.EXPLODED :
            if self.x < -540 :
                self.x = random.randint(self.canvas_width + 100, self.canvas_width + 500)
            if self.x > 1620:
                self.x = random.randint(-500, -100)
            self.state = self.RUNNING

    def get_bb(self):
        r = 50
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r

    def draw(self):
        self.image.draw(self.x, self.y)

