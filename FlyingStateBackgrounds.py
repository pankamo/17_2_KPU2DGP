from pico2d import *

import math

class Ground :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/FlyingStateGrass.png')
        self.x, self.y = 0,0
        self.camera_width = get_canvas_width()
        self.camera_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

        self.ql = 0
        self.qb = 0

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.qb += bison.y
        self.qb = int(clamp(0, self.qb, 600 - self.camera_height))
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, self.qb,
                                        self.w - self.ql, self.h - self.qb,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , self.qb,
                                        self.ql, self.h - self.qb,
                                        self.w - self.ql, self.y)

    def get_bb(self):
        return 0, 0, 1080, 80


class UpperGround :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/FlyingStateGrassSecond.png')
        self.x, self.y = 0,0
        self.camera_width = get_canvas_width()
        self.camera_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

        self.ql = 0
        self.qb = 0

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS // 3

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.qb += bison.y
        self.qb = int(clamp(0, self.qb, 600 - self.camera_height))
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, self.qb,
                                        self.w - self.ql, self.h - self.qb,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , self.qb,
                                        self.ql, self.h - self.qb,
                                        self.w - self.ql, self.y)

class BackgroundFirst:

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/FlyingStateBackgroundFirst.png')
        self.x, self.y = 0,0
        self.camera_width = get_canvas_width()
        self.camera_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

        self.ql = 0
        self.qb = 0

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS // 5

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.qb += bison.y
        self.qb = int(clamp(0, self.qb, 600 - self.camera_height))
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, self.qb,
                                        self.w - self.ql, self.h - self.qb,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , self.qb,
                                        self.ql, self.h - self.qb,
                                        self.w - self.ql, self.y)
        pass


class BackgroundSecond :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/FlyingStateBackgroundSecond.png')
        self.x, self.y = 0,0
        self.camera_width = get_canvas_width()
        self.camera_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

        self.ql = 0
        self.qb = 0

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS // 10

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.qb += bison.y
        self.qb = int(clamp(0, self.qb, 600 - self.camera_height))
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, self.qb,
                                        self.w - self.ql, self.h - self.qb,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , self.qb,
                                        self.ql, self.h - self.qb,
                                        self.w - self.ql, self.y)
        pass





class BackgroundThird :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/FlyingStateBackgroundThird.png')
        self.x, self.y = 0,0
        self.camera_width = get_canvas_width()
        self.camera_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

        self.ql = 0
        self.qb = 0

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS // 20

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.qb += bison.y
        self.qb = int(clamp(0, self.qb, 600 - self.camera_height))
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, self.qb,
                                        self.w - self.ql, self.h - self.qb,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , self.qb,
                                        self.ql, self.h - self.qb,
                                        self.w - self.ql, self.y)
        pass