from pico2d import *

import random

import KeepingBisonSpeed




class GreenJelly:

    image = None
    markimage = None

    PIXEL_PER_METER = 108
    RUNNING_SPEED_KMPH = 0
    RUNNING, EXPLODED = 0, 1
    FLYING_SPEED_KMPH = 0
    BISON_FLYING_SPEED_KMPH = 0

    def LOAD_BISON_SPEED (self):
        KeepingBisonSpeed.LoadBisonSpeed(self)

    def __init__(self):
        self.LOAD_BISON_SPEED()
        self.BISON_FLYING_SPEED_KMPH = self.FLYING_SPEED_KMPH

        self.canvas_width = get_canvas_width()

        self.RUNNING_SPEED_KMPH = -(random.randint( self.BISON_FLYING_SPEED_KMPH // 4,
                                                    ( self.BISON_FLYING_SPEED_KMPH // 4) * 2))

        if self.image == None :
            self.image = load_image('./Images/JellySprites.png')
        if self.markimage == None :
            self.markimage = load_image('./Images/GreenJellyMark.png')

        self.markimage.opacify(0)
        self.w = self.image.w
        self.h = self.image.h
        self.x = random.randint(self.canvas_width // 2, self.canvas_width + 500)
        self.y = 0

        self.frame = random.randint(-1,5)
        self.running_frame_count = 0
        self.popping_frame_count = 0
        self.state = self.RUNNING

    def update(self,bison, frame_time):

        self.y = 220 - bison.y

        if self.state == self.RUNNING :

            self.running_frame_count += frame_time
            if self.running_frame_count > 0.05:
                self.frame = (self.frame + 1) % 6
                self.running_frame_count = 0

            self.RUNNING_SPEED_MPM = (self.RUNNING_SPEED_KMPH * 1000) / 60
            self.RUNNING_SPEED_MPS = self.RUNNING_SPEED_MPM / 60
            self.RUNNING_SPEED_PPS = self.RUNNING_SPEED_MPS * self.PIXEL_PER_METER
            distance = self.RUNNING_SPEED_PPS * frame_time
            self.x += distance

            if self.x < -540:
                self.state = self.EXPLODED

            if self.x > 2160:
                self.state = self.EXPLODED


        elif self.state == self.EXPLODED :

            self.popping_frame_count += frame_time

            self.x -= bison.FLYING_SPEED_PPS * frame_time

            if self.popping_frame_count > 0.1 and self.frame < 5 :
                self.frame = (self.frame + 1) % 6
                self.popping_frame_count = 0

            elif self.frame == 5:
                self.x = random.randint(self.canvas_width + 300, self.canvas_width + 500)
                self.frame = 0
                self.state = self.RUNNING

            elif self.x < -540 and self.RUNNING_SPEED_KMPH < 0 :
                self.x = random.randint(self.canvas_width + 300, self.canvas_width + 500)
                self.state = self.RUNNING

            elif self.x > 2160 and self.RUNNING_SPEED_KMPH > 0 :
                self.x = random.randint(-500, -100)
                self.state = self.RUNNING

        if self.y < - 80 :
            self.markimage.opacify(10)
        else :
            self.markimage.opacify(0)


    def get_bb(self):
        r = 50
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r

    def draw(self):
        self.image.clip_draw(self.frame * 250, self.state * 250, 250, 250, self.x, self.y)
        self.markimage.draw(self.x, 80)


class MudJelly:

    image = None
    markimage = None

    PIXEL_PER_METER = 108
    RUNNING_SPEED_KMPH = 0
    RUNNING, EXPLODED = 0, 1
    FLYING_SPEED_KMPH = 0
    BISON_FLYING_SPEED_KMPH = 0

    def LOAD_BISON_SPEED (self):
        KeepingBisonSpeed.LoadBisonSpeed(self)

    def __init__(self):
        self.LOAD_BISON_SPEED()
        self.BISON_FLYING_SPEED_KMPH = self.FLYING_SPEED_KMPH

        self.canvas_width = get_canvas_width()

        self.RUNNING_SPEED_KMPH = -(random.randint( self.BISON_FLYING_SPEED_KMPH // 4,
                                                    ( self.BISON_FLYING_SPEED_KMPH // 3)))

        if self.image == None :
            self.image = load_image('./Images/MudJellySprites.png')
        if self.markimage == None :
            self.markimage = load_image('./Images/MudJellyMark.png')

        self.markimage.opacify(0)
        self.w = self.image.w
        self.h = self.image.h
        self.x = random.randint(self.canvas_width // 2, self.canvas_width + 500)
        self.y = 0

        self.frame = random.randint(-1,5)
        self.running_frame_count = 0
        self.popping_frame_count = 0
        self.state = self.RUNNING

    def update(self,bison, frame_time):

        self.y = 220 - bison.y

        if self.state == self.RUNNING :

            self.running_frame_count += frame_time
            if self.running_frame_count > 0.05:
                self.frame = (self.frame + 1) % 6
                self.running_frame_count = 0

            self.RUNNING_SPEED_MPM = (self.RUNNING_SPEED_KMPH * 1000) / 60
            self.RUNNING_SPEED_MPS = self.RUNNING_SPEED_MPM / 60
            self.RUNNING_SPEED_PPS = self.RUNNING_SPEED_MPS * self.PIXEL_PER_METER
            distance = self.RUNNING_SPEED_PPS * frame_time
            self.x += distance

            if self.x < -540:
                self.state = self.EXPLODED

            if self.x > 2160:
                self.state = self.EXPLODED


        elif self.state == self.EXPLODED :

            self.popping_frame_count += frame_time

            self.x -= bison.FLYING_SPEED_PPS * frame_time

            if self.popping_frame_count > 0.1 and self.frame < 5 :
                self.frame = (self.frame + 1) % 6
                self.popping_frame_count = 0

            elif self.frame == 5:
                self.x = random.randint(self.canvas_width + 300, self.canvas_width + 500)
                self.frame = 0
                self.state = self.RUNNING

            elif self.x < -540 and self.RUNNING_SPEED_KMPH < 0 :
                self.x = random.randint(self.canvas_width + 300, self.canvas_width + 500)
                self.state = self.RUNNING

            elif self.x > 2160 and self.RUNNING_SPEED_KMPH > 0 :
                self.x = random.randint(-500, -100)
                self.state = self.RUNNING

        if self.y < - 80 :
            self.markimage.opacify(10)
        else :
            self.markimage.opacify(0)


    def get_bb(self):
        r = 50
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r

    def draw(self):
        self.image.clip_draw(self.frame * 250, self.state * 250, 250, 250, self.x, self.y)
        self.markimage.draw(self.x, 80)

class PinkJelly:

    image = None
    markimage = None

    PIXEL_PER_METER = 108
    RUNNING_SPEED_KMPH = 0
    RUNNING, EXPLODED = 0, 1
    FLYING_SPEED_KMPH = 0
    BISON_FLYING_SPEED_KMPH = 0

    def LOAD_BISON_SPEED (self):
        KeepingBisonSpeed.LoadBisonSpeed(self)

    def __init__(self):
        self.LOAD_BISON_SPEED()
        self.BISON_FLYING_SPEED_KMPH = self.FLYING_SPEED_KMPH

        self.canvas_width = get_canvas_width()

        self.RUNNING_SPEED_KMPH = -(random.randint( self.BISON_FLYING_SPEED_KMPH // 4,
                                                    ( self.BISON_FLYING_SPEED_KMPH // 3)))

        if self.image == None :
            self.image = load_image('./Images/PinkJellySprites.png')
        if self.markimage == None :
            self.markimage = load_image('./Images/PinkJellyMark.png')

        self.markimage.opacify(0)
        self.w = self.image.w
        self.h = self.image.h
        self.x = random.randint(self.canvas_width // 2, self.canvas_width + 500)
        self.y = 0

        self.frame = random.randint(-1,5)
        self.running_frame_count = 0
        self.popping_frame_count = 0
        self.state = self.RUNNING

    def update(self,bison, frame_time):

        self.y = 220 - bison.y

        if self.state == self.RUNNING :

            self.running_frame_count += frame_time
            if self.running_frame_count > 0.05:
                self.frame = (self.frame + 1) % 6
                self.running_frame_count = 0

            self.RUNNING_SPEED_MPM = (self.RUNNING_SPEED_KMPH * 1000) / 60
            self.RUNNING_SPEED_MPS = self.RUNNING_SPEED_MPM / 60
            self.RUNNING_SPEED_PPS = self.RUNNING_SPEED_MPS * self.PIXEL_PER_METER
            distance = self.RUNNING_SPEED_PPS * frame_time
            self.x += distance

            if self.x < -540:
                self.state = self.EXPLODED

            if self.x > 2160:
                self.state = self.EXPLODED


        elif self.state == self.EXPLODED :

            self.popping_frame_count += frame_time

            self.x -= bison.FLYING_SPEED_PPS * frame_time

            if self.popping_frame_count > 0.1 and self.frame < 5 :
                self.frame = (self.frame + 1) % 6
                self.popping_frame_count = 0

            elif self.frame == 5:
                self.x = random.randint(self.canvas_width + 300, self.canvas_width + 500)
                self.frame = 0
                self.state = self.RUNNING

            elif self.x < -540 and self.RUNNING_SPEED_KMPH < 0 :
                self.x = random.randint(self.canvas_width + 300, self.canvas_width + 500)
                self.state = self.RUNNING

            elif self.x > 2160 and self.RUNNING_SPEED_KMPH > 0 :
                self.x = random.randint(-500, -100)
                self.state = self.RUNNING

        if self.y < - 80 :
            self.markimage.opacify(10)
        else :
            self.markimage.opacify(0)


    def get_bb(self):
        r = 50
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r

    def draw(self):
        self.image.clip_draw(self.frame * 250, self.state * 250, 250, 250, self.x, self.y)
        self.markimage.draw(self.x, 80)
