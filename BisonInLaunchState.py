from pico2d import *
import os

class Bison:

    image = None

    SHIVERING, ATTACKING, HITTING, FLYING, FAILED, BOOSTERED, KNOCKOUT \
    = 1, 2, 3, 4, 4, 6, 5

    def __init__(self):
        self.x, self.y = (300, 150)
        self.frame = 0
        self.state = self.SHIVERING
        self.vibration = 2
        if Bison.image == None :
            self.image = load_image('./Images/LaunchingB_sprite.png')

    def update(self,frame_time):
        if self.state == self.SHIVERING:
            self.x = self.x + self.vibration
            self.vibration = -self.vibration

    def draw(self):
        self.image.clip_draw(self.frame * 250, self.state * 250,
                             250, 250, self.x, self.y)



