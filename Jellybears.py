from pico2d import *

import random

class JellyBear:

    image = None
    PIXEL_PER_METER = 108

    def __init__(self):
        self.RUNNING_SPEED_KMPH = (random.randint(5, 25))
        self.RUNNING_SPEED_MPM = ( self.RUNNING_SPEED_KMPH * 1000 ) / 60
        self.RUNNING_SPEED_MPS = self.RUNNING_SPEED_MPM / 60
        self.RUNNING_SPEED_PPS = self.RUNNING_SPEED_MPS * self.PIXEL_PER_METER
        if self.image == None :
            self.image = load_image('./Images/TempBear.png')
        self.x = random.randint(0,1280)
        self.y = 100

    def set_background(self, background):
        self.background = background
        self.x = 0
        self.y = 0

    def update(self,frame_time):
        distance = self.RUNNING_SPEED_PPS * frame_time
        self.x += distance

    def get_bb(self):
        r = 50
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r

    def draw(self, background):
        self.image.draw(self.x - background.q3l,
                        self.y - background.q3b)

