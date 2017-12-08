from pico2d import *

class Ground :

    image = None

    def __init__(self):
        self.x, self.y = ( 540, 50 )
        if self.image == None :
            self.image = load_image('./Images/TempGrass.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 540, self.y - 50, self.x + 540, self.y + 25



class Background :

    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/TempScene.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_main_object(self, bison):
        self.main_object = bison

    def update(self, frame_time):

        self.q3l = (int(self.main_object.x) - self.canvas_width // 4 ) % self.w
        self.q3b = clamp(0,
            int(self.main_object.y) - self.canvas_width // 2,
            self.h - self.canvas_height )
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)

        self.q4l = 0
        self.q4b = self.q3b
        self.q4w = self.canvas_width - self.q3w
        self.q4h = self.q3h

        #self.window_left = clamp(0,
            #int(self.main_object.x) - self.canvas_width // 4,
            #self.w - self.canvas_width )
        #self.window_bottom = clamp(0,
            #int(self.main_object.y) - self.canvas_width // 2,
            #self.h - self.canvas_height )
        pass

    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)
        self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)
        #self.image.clip_draw_to_origin(
            #self.window_left, self.window_bottom,
            #self.canvas_width, self.canvas_height,
            #0, 0)

        #self.image.clip_draw_to_origin(
            #self.window_left , self.window_bottom,
            #self.canvas_width, self.canvas_height,
            #self.canvas_width , 0)
        pass