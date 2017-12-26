from pico2d import *

import math

class Monster:

    image = None
    taunting_sound = None

    IDLE, FAIL_DRAGGING, NORMAL_DRAGGING, SUCCESS_DRAGGING, TAUNTING, KNOCKED = 0, 1, 2, 3, 4, 5

    def __init__(self):
        self.x, self.y = (800, 250)
        self.state = self.IDLE
        self.frame = 0
        self.frame_count = 0
        self.time_count = 0
        if self.image == None :
            self.image = load_image('./Images/MonsterSprites.png')


    def update(self, frame_time):
        if self.state == self.IDLE :
            self.frame_count += frame_time
            if self.frame_count > 0.25 :
                self.frame = (self.frame + 1) % 6
                self.frame_count = 0
            pass

        if self.state == self.FAIL_DRAGGING :
            self.time_count += frame_time
            self.frame_count += frame_time

            if self.frame_count > 0.25 :
                self.frame = (self.frame + 1) % 6
                self.frame_count = 0

            if int(self.time_count) == 2 :
                self.time_count = 0
                self.state = self.TAUNTING
            pass


        if self.state == self.NORMAL_DRAGGING :
            self.time_count += frame_time
            self.frame_count += frame_time

            if self.frame_count > 0.25 :
                self.frame = (self.frame + 1) % 6
                self.frame_count = 0

            if int(self.time_count) == 2 :
                self.time_count = 0
                self.state = self.KNOCKED


        if self.state == self.SUCCESS_DRAGGING :
            self.time_count += frame_time
            self.frame_count += frame_time

            if self.frame_count > 0.25 :
                self.frame = (self.frame + 1) % 6
                self.frame_count = 0

            if int(self.time_count) == 2 :
                self.time_count = 0
                self.state = self.KNOCKED


        if self.state == self.KNOCKED :
            self.frame = 0
            pass


        if self.state == self.TAUNTING :
            self.frame_count += frame_time

            if self.frame_count > 0.25 :
                self.frame = (self.frame + 1) % 6
                self.frame_count = 0
            pass


    def draw(self):
        self.image.clip_draw(self.frame * 500, self.state * 500, 500, 500, self.x, self.y)
        pass

    def get_bb(self):
        r = 120
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return ( x, y, r )