from pico2d import *

import random
import math
import KeepingBisonSpeed
import LaunchState

class Bison:

    image = None
    normal_launchsound = None
    success_launchsound = None

    SHIVERING, ATTACKING, FAILED, BOOSTERED, HITTING, REFLECTING, FLYING, KNOCKOUT \
    = 1, 2, 4, 6, 3, 8, 7, 5

    FLYING_SPEED_KMPH = 0

    scene_change_time = 0

    def SaveBisonSpeed(self):
        return self.FLYING_SPEED_KMPH

    def __init__(self):
        global PIXEL_PER_METER
        global frame_count
        global time_count
        PIXEL_PER_METER = 108
        frame_count = 0
        time_count = 0
        self.x, self.y = (250, 100)
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
            self.FLYING_SPEED_KMPH = 128
            KeepingBisonSpeed.SaveBisonSpeed(self)

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
            self.FLYING_SPEED_KMPH = 256
            KeepingBisonSpeed.SaveBisonSpeed(self)

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
            self.FLYING_SPEED_KMPH = 10
            KeepingBisonSpeed.SaveBisonSpeed(self)

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

            HITTING_SPEED_MPS = 1
            HITTING_SPEED_PPS = (HITTING_SPEED_MPS * PIXEL_PER_METER)
            distance = HITTING_SPEED_PPS * frame_time

            self.x += distance * 0.4
            self.y += distance * 0.5

            time_count += frame_time
            if int(time_count) == 2 :
                self.state = self.FLYING
                time_count = 0

        elif self.state == self.FLYING :
            FLYING_SPEED_MPS = 1
            FLYING_SPEED_PPS = (FLYING_SPEED_MPS * PIXEL_PER_METER)
            distance = FLYING_SPEED_PPS * frame_time

            self.x += distance * 8
            self.y += distance * 10

            frame_count += frame_time
            if frame_count > 0.05:
                self.frame = (self.frame + 1) % 6
                frame_count = 0

            self.scene_change_time += frame_time

            if int(self.scene_change_time) > 1 :
                self.scene_change_time = 0
                LaunchState.LAUNCHING = False
            pass

        elif self.state == self.REFLECTING :
            self.frame = 0

            REFLECTING_SPEED_MPS = 1
            REFLECTING_SPEED_PPS = (REFLECTING_SPEED_MPS * PIXEL_PER_METER)
            distance = REFLECTING_SPEED_PPS * frame_time

            self.x -= distance * 0.4
            self.y += distance * 0.4

            time_count += frame_time
            if time_count > 1.5 :
                self.x -= distance * 2
                self.y -= distance * 3
                pass

            if self.y < 100 :
                time_count = 0
                self.state = self.KNOCKOUT

        elif self.state == self.KNOCKOUT :
            pass


    def draw(self):
        self.image.clip_draw(self.frame * 250, self.state * 250,
                             250, 250, self.x, self.y)

    def handle_event(self, event) :
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state == self.SHIVERING :
                self.state = self.ATTACKING

    def get_bb(self):
        r = 300
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return ( x, y, r )




