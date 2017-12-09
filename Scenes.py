from pico2d import *

import math

class Ground :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/TempGrass.png')
        self.x, self.y = ( 540, 50 )
        self.camera_width = get_canvas_width()
        self.camera_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def update(self, frame_time):
        self.q3l = ((int(self.main_object.x) - self.camera_width // 4 ) % self.w ) \
                    # + int((int(self.main_object.x) - self.camera_width // 4 ) // self.w) * self.w
        self.q3b = clamp(0,
                    int(self.main_object.y) - (self.camera_height // 5) * 4,
                    self.h - self.camera_height)
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)

        self.q4l = 0
        self.q4b = self.q3b
        self.q4w = self.camera_width - self.q3w
        self.q4h = self.q3h
        pass

    def set_main_object(self, bison):
        self.main_object = bison

    def set_jellybear(self, jellybear):
        self.jellybear = jellybear

    def set_background(self, background):
        self.background = background

    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)
        self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)

    def get_bb(self):
        return self.x - 540, self.y - 50, self.x + 540, self.y + 25



class Background :

    image = None
    SCROLLING_SPEED_PPS = 0

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/TempScene.png')
        self.speed = 0
        self.camera_width = get_canvas_width()
        self.camera_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x, self.y = 540, 300

    def GET_SCROLLING_SPEED(self, bison, background):
        self.SCROLLING_SPEED_PPS = bison.GET_BISON_FLYING_SPEED_PPS(background)
        return self.SCROLLING_SPEED_PPS

    def update(self, bison, background, frame_time):
        self.GET_SCROLLING_SPEED(bison, background)
        self.x -= int(self.SCROLLING_SPEED_PPS) * frame_time
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass