from pico2d import *

class Bison:

    image = None

    CHARGING = 6

    FLYING_SPEED_KMPH = 5
    PIXEL_PER_METER = 108


    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/LaunchingB_sprite.png')
        self.state = self.CHARGING
        self.frame = 0
        self.frame_count = 0
        self.width = 250
        self.height = 250
        self.x, self.y = 100, 400

        self.FLYING_SPEED_MPM = (self.FLYING_SPEED_KMPH * 1000) // 60
        self.FLYING_SPEED_MPS = (self.FLYING_SPEED_MPM // 60)
        self.FLYING_SPEED_PPS = self.FLYING_SPEED_MPS * self.PIXEL_PER_METER

    def update(self, frame_time):

        distance = self.FLYING_SPEED_PPS * frame_time

        if self.state == self.CHARGING :
            self.frame_count += frame_time
            if self.frame_count > 0.05:
                self.frame = (self.frame + 1) % 6
                self.frame_count = 0
            pass

            self.x += distance


    def draw(self):
        self.image.clip_draw(self.frame * 250, self.state * 250, self.width, self.height, self.x, self.y)
