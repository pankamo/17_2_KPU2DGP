from pico2d import *

import random
import math

class Bison:

    font = None
    image = None

    DESCENT, RISING, ROTATING, KNOCKOUT = 1, 0, 2, 5

    PIXEL_PER_METER = 108
    FLYING_SPEED_KMPH = 20.0
    GRAVITIONAL_ACCELERATION = 9.81 #MPS
    ENERGY_LOSS = 9.81
    ELASTIC_ENERGY = 0

    def __init__(self):
        global frame_count
        global time_count
        global DESCENT_SPEED_MPS
        global RISING_SPEED_MPS
        frame_count = 0
        time_count = 0
        DESCENT_SPEED_MPS = 0
        RISING_SPEED_MPS = 0
        self.x, self.y = 0, 0
        self.frame = 0
        self.direction = -1
        self.state = self.DESCENT
        if self.image == None :
            self.image = load_image('./Images/FlyingB_sprite.png')
        if self.font == None :
            self.font = load_font('./Fonts/aMonster.TTF',20)
            pass

    def set_mainground(self, ground):
        self.ground = ground
        self.x = self.ground.w // 4
        self.y = self.ground.h * 6


    def update(self, frame_time):
        global frame_count
        global time_count
        global DESCENT_SPEED_MPS
        global RISING_SPEED_MPS

        self.FLYING_SPEED_MPM = ( self.FLYING_SPEED_KMPH * 1000 ) / 60
        self.FLYING_SPEED_MPS = self.FLYING_SPEED_MPM / 60
        self.FLYING_SPEED_PPS = self.FLYING_SPEED_MPS * self.PIXEL_PER_METER
        distance = self.FLYING_SPEED_PPS * frame_time

        self.x += distance

        if self.state == self.DESCENT :
            self.frame = 0
            self.direction = -1
            DESCENT_SPEED_MPS += self.GRAVITIONAL_ACCELERATION * frame_time
            RISING_SPEED_MPS = DESCENT_SPEED_MPS
            self.ELASTIC_ENERGY = DESCENT_SPEED_MPS
            DESCENT_SPEED_PPS = DESCENT_SPEED_MPS * self.PIXEL_PER_METER
            distance = DESCENT_SPEED_PPS * frame_time

            self.y += self.direction * distance

        elif self.state == self.RISING :
            if frame_count > 0.05:
                self.frame = (self.frame + 1) % 6
                frame_count = 0
            self.direction = 1
            RISING_SPEED_MPS -= ( self.ENERGY_LOSS ) * frame_time
            DESCENT_SPEED_MPS = RISING_SPEED_MPS
            RISING_SPEED_PPS = RISING_SPEED_MPS * self.PIXEL_PER_METER
            distance = RISING_SPEED_PPS * frame_time

            self.y += self.direction * distance

            if RISING_SPEED_MPS < 0:
                self.state = self.DESCENT

        elif self.state == self.ROTATING :
            frame_count += frame_time
            if frame_count > 0.05 :
                self.frame = ( self.frame + 1 ) % 6
                frame_count = 0
            self.direction = 1
            RISING_SPEED_MPS -= ( self.ENERGY_LOSS + 1.0) * frame_time
            DESCENT_SPEED_MPS = RISING_SPEED_MPS
            RISING_SPEED_PPS = RISING_SPEED_MPS * self.PIXEL_PER_METER
            distance = RISING_SPEED_PPS * frame_time

            self.y += self.direction * distance

            if RISING_SPEED_MPS < 0:
                self.state = self.DESCENT

        elif self.state == self.KNOCKOUT :
            self.image = load_image('./Images/LaunchingB_sprite.png')
            self.FLYING_SPEED_KMPH = 0
            self.frame = 0

    def GET_BISON_FLYING_SPEED_PPS(self, background):
        self.FLYING_SPEED_MPM = (self.FLYING_SPEED_KMPH * 1000) / 60
        self.FLYING_SPEED_MPS = self.FLYING_SPEED_MPM / 60
        self.FLYING_SPEED_PPS = self.FLYING_SPEED_MPS * self.PIXEL_PER_METER
        background.SCROLLING_SPEED_PPS = self.FLYING_SPEED_PPS
        return background.SCROLLING_SPEED_PPS

    def draw(self):
        self.font.draw((self.x - self.ground.q3l) - 80,
                       (self.y - self.ground.q3b) + 100,
                       'self.x : %f' % (self.x - self.ground.q3l), (255,255,0))
        self.font.draw((self.x - self.ground.q3l) - 80,
                       (self.y - self.ground.q3b) - 100,
                       'SPEED : %s KMPH' % (self.FLYING_SPEED_KMPH), (255,255,0))
        self.image.clip_draw(self.frame * 250, self.state * 250, 250, 250,
                             self.x - self.ground.q3l,
                             self.y - self.ground.q3b)

    def get_bb(self):
        r = 40
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r
