from pico2d import *

import math

import game_framework

from BisonInLaunchState import Bison
from Monster import Monster
from Gauge import *

name = "LaunchState"

bison = None
monster = None
gaugebar = None
gaugepoint = None
PIXEL_PER_METER = 108


def create_LaunchingStage():
    global bison, monster, gaugebar, gaugepoint
    bison = Bison()
    monster = Monster()
    gaugebar = GaugeBar()
    gaugepoint = GaugePoint()
    pass

def destroy_LaunchingStage():
    global bison, monster, gaugebar, gaugepoint
    del(bison)
    del(monster)
    del(gaugebar)
    del(gaugepoint)

def enter():
    open_canvas( 1080, 600 )
    hide_lattice()
    game_framework.reset_time()
    create_LaunchingStage()

def exit():
    destroy_LaunchingStage()
    close_canvas()

def collide(a,b):
    BisonX, BisonY, BisonR = a.get_bb()
    MonsterX, MonsterY, MonsterR = b.get_bb()

    if math.sqrt(
            math.pow((BisonX - MonsterX),2)
            + math.pow((BisonY - MonsterY),2)
                ) \
            > (BisonR + MonsterR ):
        return False
    return True
    # 주인공 개체의 X1,Y1 좌표값과 충돌판정될 반지름
    # 몬스터 개체의 X2,Y2 좌표값과 반지름을 get_bb로 반환시켜
    # 루트 ( (X1 - X2)^2 + (Y1 - Y2)^2 )가
    # 각 반지름의 합보다 클경우는
    # 두 개체가 접하지 않은것으로 판정 -> False 반환 !

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else :
                bison.handle_event(event)


def update(frame_time):
    monster.update(frame_time)
    bison.update(frame_time)
    if collide(bison, monster) :
        if bison.state == bison.ATTACKING \
            or bison.state == bison.BOOSTERED:
            bison.state = bison.HITTING
        if bison.state == bison.FAILED :
            bison.state = bison.REFLECTING
    gaugebar.update(frame_time, bison)
    gaugepoint.update(frame_time, bison)

def draw(frame_time):
    clear_canvas()
    bison.draw()
    monster.draw()
    gaugebar.draw()
    gaugepoint.draw()
    update_canvas()
    pass

if __name__ == '__main__' :
    enter()