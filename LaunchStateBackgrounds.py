from pico2d import *

class Grass :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/LaunchStateGrass.png')
        self.x, self.y = 0,0

    def draw(self):
        self.image.draw_to_origin(self.x, self.y)

class Ground :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/LaunchStateGround.png')
        self.x, self.y = 0,0

    def draw(self):
        self.image.draw_to_origin(self.x, self.y)


class Background :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/MainTitleBackground.png')
        self.x, self.y = 0,0
        self.camera_width = get_canvas_width()
        self.camera_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

        self.ql = 0

    def update(self, frame_time):
        self.speed = 200

        self.ql = int((self.ql + (self.speed * frame_time)) % self.w)

    def draw(self):
        self.image.clip_draw_to_origin( self.ql, 0,
                                        self.w - self.ql, self.h,
                                        self.x, self.y)
        self.image.clip_draw_to_origin( 0 , 0,
                                        self.ql, self.h,
                                        self.w - self.ql, self.y)