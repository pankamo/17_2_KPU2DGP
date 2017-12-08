from pico2d import *

import random
import math

class Bison:

    image = None

    SHIVERING, ATTACKING, FAILED, BOOSTERED, HITTING, REFLECTING, FLYING, KNOCKOUT \
    = 1, 2, 4, 6, 3, 3, 4, 5

    def __init__(self):
        global PIXEL_PER_METER
        global frame_count
        global time_count
        PIXEL_PER_METER = 108
        frame_count = 0
        time_count = 0
        self.x, self.y = (250, 150)
        self.frame = 0
        self.vibedirection = random.choice([-1,1])
        self.state = self.SHIVERING
        if self.image == None :
            self.image = load_image('./Images/LaunchingB_sprite.png')
            pass

    def update(self,frame_time):
        global frame_count
        global time_count
        if self.state == self.SHIVERING:
            VIBE_SPEED_PPS = 100
            distance = VIBE_SPEED_PPS * frame_time
            if self.vibedirection :
                self.x = clamp(248, self.x + (self.vibedirection * distance), 252)
                if self.x == 248 or self.x == 252:
                    self.vibedirection = -(self.vibedirection)

        elif self.state == self.ATTACKING :
            ATTACK_SPEED_MPS = 8
            ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)
            distance = ATTACK_SPEED_PPS * frame_time
            # 시속 약 30 Km / 초당 864 픽셀이동

            frame_count += frame_time
            if frame_count > 0.025 :
                self.frame = ( self.frame + 1 ) % 6
                frame_count = 0
            self.x += distance
            pass

        elif self.state == self.BOOSTERED :
            ATTACK_SPEED_MPS = 10
            ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)
            distance = ATTACK_SPEED_PPS * frame_time
            # 시속 약 36 Km / 초당 1080 픽셀이동

            frame_count += frame_time
            if frame_count > 0.05 :
                self.frame = ( self.frame + 1 ) % 6
                frame_count = 0
            self.x += distance

        elif self.state == self.FAILED :
            ATTACK_SPEED_MPS = 6
            ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)
            distance = ATTACK_SPEED_PPS * frame_time
            # 시속 약 22 Km / 초당 648 픽셀이동

            frame_count += frame_time
            if frame_count > 0.05 :
                self.frame = ( self.frame + 1 ) % 6
                frame_count = 0
            self.x += distance

        elif self.state == self.HITTING :
            self.frame = 0
            self.x = self.x + 0.4
            self.y = self.y + 0.5
            time_count += frame_time

            if int(time_count) == 1 :
                time_count = 0
                self.state = self.FLYING

        elif self.state == self.FLYING :
            self.x = self.x + 4
            self.y = self.y + 5
            frame_count += frame_time
            if frame_count > 0.05:
                self.frame = (self.frame + 1) % 6
                frame_count = 0
            pass

        elif self.state == self.REFLECTING :
            self.x = self.x - 0.4
            self.y = self.y - 0.5

    def draw(self):
        self.image.clip_draw(self.frame * 250, self.state * 250,
                             250, 250, self.x, self.y)

    def handle_event(self, event) :
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state == self.SHIVERING :
                self.state = self.ATTACKING

    def get_bb(self):
        r = 40
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return ( x, y, r )



