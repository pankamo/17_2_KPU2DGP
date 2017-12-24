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

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.y = 120-(bison.y)
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, 0,
                                        self.w - self.ql, self.h,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , 0,
                                        self.ql, self.h,
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

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS // 3

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.y = 120 - bison.y
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, 0,
                                        self.w - self.ql, self.h,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , 0,
                                        self.ql, self.h,
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

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS // 10

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.y = 120 - bison.y
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, 0,
                                        self.w - self.ql, self.h,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , 0,
                                        self.ql, self.h,
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

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS // 10

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.y = 120 - bison.y
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, 0,
                                        self.w - self.ql, self.h,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , 0,
                                        self.ql, self.h,
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

    def update(self, bison, frame_time):
        bison.GET_BISON_FLYING_SPEED_PPS()
        self.speed = bison.FLYING_SPEED_PPS // 100

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)
        self.y = max (120 - bison.y, self.camera_height - self.h)
        pass

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, 0,
                                        self.w - self.ql, self.h,
                                        self.x + 1, self.y)
        self.image.clip_draw_to_origin( 0 , 0,
                                        self.ql, self.h,
                                        self.w - self.ql, self.y)
        pass