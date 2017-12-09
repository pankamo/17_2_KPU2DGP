from pico2d import *

import math

import game_framework

from BisonInFlyingState import Bison
from Jellybears import JellyBear
from Scenes import *

name = "FlyingState"

bison = None
jellybear = None
policebear = None
rocketbear = None
bombbear = None
ground = None
background = None
PIXEL_PER_METER = 108


def create_FlyingStage():
    global bison, ground, background, \
            jellybear, policebear, rocketbear, bombbear
    bison = Bison()
    ground = Ground()
    jellybear = JellyBear()
    background = Background()

    ground.set_main_object(bison)
    ground.set_jellybear(jellybear)
    ground.set_background(background)

    bison.set_mainground(ground)


    jellybear = [JellyBear() for i in range(20)]
    #policebear = [PoliceBear() for i in range(2)]
    #rocketbear = [RocketBear() for i in range(2)]
    #bombbear = [BombBear() for i in range(2)]

    pass

def destroy_FlyingStage():
    global bison, ground, background, jellybear
    del(ground)
    del(background)
    del(bison)
    del(jellybear)

def enter():
    open_canvas( 1080, 600 )
    hide_lattice()
    game_framework.reset_time()
    create_FlyingStage()

def exit():
    destroy_FlyingStage()
    close_canvas()

def collide(a,b):
    BisonX, BisonY, BisonR = a.get_bb()
    ObjectX, ObjectY, ObjectR= b.get_bb()

    if math.sqrt(
            math.pow((BisonX - ObjectX),2)
            + math.pow((BisonY - ObjectY),2)
                ) \
            > (BisonR + ObjectR ):
        return False
    return True

def falling(a,b):
    BisonX, BisonY, BisonR = a.get_bb()
    LeftB, BottomB, RightB, TopB = b.get_bb()

    if (BisonY - TopB) > BisonR :
        return False
    return True

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def update(frame_time):
    global jellybear
    background.update(bison, background, frame_time)
    bison.update(frame_time)
    ground.update(frame_time)
    if falling(bison, ground):
        if bison.state == bison.DESCENT :
            bison.state = bison.RISING
            bison.FLYING_SPEED_KMPH -= 0
            bison.ENERGY_LOSS += 0
        if bison.ELASTIC_ENERGY < 6 :
            bison.state = bison.KNOCKOUT
        if bison.FLYING_SPEED_KMPH < 10:
            bison.state = bison.KNOCKOUT

    for jb in jellybear :
        jb.update(frame_time)
        if collide(bison, jb):
            if bison.state == bison.DESCENT :
                bison.state = bison.RISING
                bison.FLYING_SPEED_KMPH -= 0
                bison.ENERGY_LOSS += 0





def draw(frame_time):
    clear_canvas()
    background.draw()
    bison.draw()
    for jb in jellybear :
        jb.draw(ground)
    ground.draw()
    update_canvas()
    pass

if __name__ == '__main__' :
    enter()