from pico2d import *

import random
import math

class Bison:

    font = None
    image = None

    DESCENT, RISING, ROTATING, KNOCKOUT, ROCKETSLAM = 1, 0, 2, 3, 4

    PIXEL_PER_METER = 108
    FLYING_SPEED_KMPH = 0
    GRAVITIONAL_ACCELERATION = 9.81 #MP
    ELASTIC_ENERGY = 0

    def SET_ENEMY(self, jellybears):
        self.enemy = jellybears

    def __init__(self):
        global frame_count
        global time_count
        global DESCENT_SPEED_MPS
        global RISING_SPEED_MPS
        frame_count = 0
        time_count = 0
        DESCENT_SPEED_MPS = 0
        RISING_SPEED_MPS = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = 0
        self.direction = -1
        self.state = self.DESCENT
        self.x = self.canvas_width // 4
        self.y = self.canvas_height
        self.FLYING_SPEED_KMPH = 128
        self.ENERGY_LOSS = 0

        if self.image == None :
            self.image = load_image('./Images/FlyingB_sprite.png')
        if self.font == None :
            self.font = load_font('./Fonts/aMonster.TTF',30)
            pass

    def update(self, frame_time):
        global frame_count
        global time_count
        global DESCENT_SPEED_MPS
        global RISING_SPEED_MPS


        self.FLYING_SPEED_MPM = ( self.FLYING_SPEED_KMPH * 1000 ) / 60
        self.FLYING_SPEED_MPS = self.FLYING_SPEED_MPM / 60
        self.FLYING_SPEED_PPS = self.FLYING_SPEED_MPS * self.PIXEL_PER_METER

        self.x = clamp(0, self.canvas_width // 4, self.canvas_width)
        self.y = clamp(125, self.y, self.canvas_height)

        if self.state == self.KNOCKOUT :
            pass
        else :
            self.spend_time = get_time()

        if self.state == self.DESCENT :
            self.frame = 0
            self.direction = -1
            self.ENERGY_LOSS = 9.81
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

        elif self.state == self.ROCKETSLAM :
            self.frame = 0
            self.direction = -1
            self.ENERGY_LOSS = 9.81
            DESCENT_SPEED_MPS += self.GRAVITIONAL_ACCELERATION * frame_time
            RISING_SPEED_MPS = DESCENT_SPEED_MPS
            self.ELASTIC_ENERGY = DESCENT_SPEED_MPS
            DESCENT_SPEED_PPS = DESCENT_SPEED_MPS * self.PIXEL_PER_METER
            distance = DESCENT_SPEED_PPS * frame_time

            self.y += self.direction * (distance * 3)


        elif self.state == self.KNOCKOUT :
            self.FLYING_SPEED_KMPH = 0
            self.frame = 0

    def GET_BISON_FLYING_SPEED_PPS(self):
        self.FLYING_SPEED_MPM = (self.FLYING_SPEED_KMPH * 1000) / 60
        self.FLYING_SPEED_MPS = self.FLYING_SPEED_MPM / 60
        self.FLYING_SPEED_PPS = self.FLYING_SPEED_MPS * self.PIXEL_PER_METER
        return self.FLYING_SPEED_PPS

    def draw(self):
        #self.font.draw(self.x - 80, self.y + 100,
                       #'self.x : %f' % (self.x), (255,255,0))
        self.font.draw(20, 570,
                       '비행 속도 : %s KM/H' % (self.FLYING_SPEED_KMPH), (0,0,0))
        self.font.draw(20, 530,
                       '비행 시간 : %2.2f 초' % (self.spend_time),(0,0,0))
        self.image.clip_draw(self.frame * 250, self.state * 250, 250, 250,
                             self.x, self.y)

    def get_bb(self):
        r = 40
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE :
            self.state = self.ROCKETSLAM
