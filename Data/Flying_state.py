from pico2d import *
import random
import os
import math
import Jellybears
import Flying_map

name = "Flying_state"

Flying = True
BouncingDirection = None
BD = BouncingDirection
descent = 0
jellypop = False
RocketSlam = False

# 화면 내의 너비 : 10 METER로 설정
# 미터당 픽셀 : 108 px
PIXEL_PER_METER = 108

class FBison :

    image = None
    FBrising, FBdescent, FBrotating= 0, 1, 2

    frame = 0
    state = 0

    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        if FBison.image == None :
            self.image = load_image('FlyingB_sprite.png')
        self.x, self.y = ( 250, 600 )
        global BD
        global BOUNCING_SPEED_MPS
        BD = -1
        BOUNCING_SPEED_MPS = 0


    def update(self, frame_time):
        global BD
        global BOUNCING_SPEED_MPS
        global descent
        global jellypop
        global RocketSlam
        global Fallen

        if RocketSlam == False:
            if BD == -1:
                Fallen = False
                self.state = self.FBdescent
                self.frame = 0
                BOUNCING_SPEED_MPS += 9.81 / 500
                BOUNCING_SPEED_PPS = (BOUNCING_SPEED_MPS * PIXEL_PER_METER)
                distance = BOUNCING_SPEED_PPS * frame_time
                descent += 1
                self.y += ( BD * distance )
                if self.y <= 100 :
                    BD = 1
                    Fallen = True
                    Flying_map.groundspeed -= 6
                elif jellypop == True :
                    BD = 1
                    jellypop = False

            if BD == 1 :
                if Fallen == False :
                    self.state = self.FBrising
                    self.frame = ( self.frame + 1 ) % 6
                if Fallen == True :
                    self.state = self.FBrotating
                    self.frame = ( self.frame + 1) % 6
                BOUNCING_SPEED_MPS -= 9.81 / 500
                BOUNCING_SPEED_PPS = (BOUNCING_SPEED_MPS * PIXEL_PER_METER)
                distance = BOUNCING_SPEED_PPS * frame_time
                descent -= 1

                self.y += ( BD * distance )
                if descent == 0:
                    BD = -1

        if RocketSlam == True:
            RocketSlam = False
            #로켓슬램 구현해야해!!


    def draw(self):
        self.image.clip_draw(self.frame * 250, self.state * 250, \
            250, 250, self.x, self.y )

    def get_bb(self):
        r = 50
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r

def collide(o,p):
    FBX, FBY, FBR = o.get_bb()
    BRX, BRY, BRR = p.get_bb()

    if math.sqrt(math.pow((FBX - BRX),2) + math.pow((FBY - BRY),2)) \
        > (FBR + BRR ):
        return False
    # 주인공 개체의 움직이는 X1,Y1 좌표값과 충돌판정될 반지름
    # Bear 개체의 움직이는 X2,Y2 좌표값과 반지름을 get_bb로 반환시켜
    # 루트 ( (X1 - X2)^2 + (Y1 - Y2)^2 )가
    # 각 반지름의 합보다 클경우는
    # 주인공 개체와 Bear개체가 접하지 않은것으로 판정 -> False반환
    return True

def handle_events(frame_time):
    global Flying
    global RocketSlam
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Flying = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Flying = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            RocketSlam = True
            pass


current_time = 0.0
def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time
open_canvas(1080,600)

FB = FBison()
BR = [Jellybears.Bear() for i in range(4)]
PBR = [Jellybears.PoliceBear() for i in range(2)]
RBR = [Jellybears.RocketBear() for i in range(1)]
BRS = BR + PBR + RBR
CG = [Flying_map.Candygrass() for i in range(3)]
SB = [Flying_map.Scrollingscene() for i in range(3)]

while Flying :

    frame_time = get_frame_time()
    handle_events(frame_time)
    clear_canvas()
    FB.update(frame_time)
    for bear in BRS :
        bear.update(frame_time)
        if collide(FB,bear) == True:
            bear.x = 1400
            jellypop = True
    for police in BRS :
        police.update(frame_time)
    for rocbe in BRS :
        rocbe.update(frame_time)

    for grass in CG :
        grass.update(frame_time)

    for scene in SB:
        scene.update(frame_time)

    for scene in SB:
        scene.draw()
    FB.draw()
    for bear in BRS :
        bear.draw()
    for police in BRS :
        police.draw()
    for rocbe in BRS :
        rocbe.draw()
    for grass in CG :
        grass.draw()
    #delay(0.015)
    update_canvas()

close_canvas()

