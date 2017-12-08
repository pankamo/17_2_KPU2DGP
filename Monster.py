from pico2d import *

import math

class Monster:

    image = None

    IDLE, DRAGGING, LAUGHING, KNOCKED, CRUSHED = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = (800, 150)
        self.frame = 0
        self.state = self.IDLE
        if self.image == None :
            self.image = load_image('./Images/TempM.png')


    def update(self, frame_time):
        if self.state == self.IDLE :
            pass

        if self.state == self.DRAGGING :
            PIXEL_PER_METER = 108
            DRAG_SPEED_MPS = 0.4
            DRAG_SPEED_PPS = (DRAG_SPEED_MPS * PIXEL_PER_METER)
            distance = DRAG_SPEED_PPS * frame_time
            # 시속 1.44 Km / 초당 43.2 픽셀이동
            pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

    def get_bb(self):
        r = 70
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return ( x, y, r )