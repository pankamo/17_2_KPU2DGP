from pico2d import *

import math

import game_framework

import LaunchState

from BisonInFlyingState import Bison
from Jellybears import JellyBear
from FlyingStateBackgrounds import *

name = "FlyingState"

bison = None
jellybear = None
policebear = None
rocketbear = None
bombbear = None
ground = None
upperground = None
background = None
PIXEL_PER_METER = 108


def create_FlyingStage():
    global bison,\
            ground, upperground,\
            backgroundfirst, backgroundsecond, backgroundthird,\
            jellybear, jellybears

    bison = Bison()
    upperground = UpperGround()
    ground = Ground()
    jellybear = JellyBear(bison)
    backgroundfirst = BackgroundFirst()
    backgroundsecond = BackgroundSecond()
    backgroundthird = BackgroundThird()


    jellybear = [JellyBear(bison) for jellybear in range(6)]
    jellybears = jellybear

    #policebear = [PoliceBear() for i in range(2)]
    #rocketbear = [RocketBear() for i in range(2)]
    #bombbear = [BombBear() for i in range(2)]

    pass

def destroy_FlyingStage():
    global bison,\
            ground, upperground,\
            backgroundfirst, backgroundsecond, backgroundthird,\
            jellybear,\
            bgm
    del(ground)
    del(upperground)
    del(backgroundfirst)
    del(backgroundsecond)
    del(backgroundthird)
    del(bison)
    del(jellybear)
    del(bgm)

def bgm_play() :
    global bgm
    bgm = load_wav('./Sounds/FlyingBGM.wav')
    bgm.set_volume(50)
    bgm.play()

def enter():
    hide_lattice()
    game_framework.reset_time()
    create_FlyingStage()
    bgm_play()

def exit():
    destroy_FlyingStage()

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
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                game_framework.change_state(LaunchState)
            else :
                bison.handle_event(event)


def update(frame_time):
    backgroundfirst.update(bison, frame_time)
    backgroundsecond.update(bison, frame_time)
    backgroundthird.update(bison,frame_time)
    upperground.update(bison,frame_time)
    bison.update(frame_time)
    ground.update(bison, frame_time)
    if falling(bison, ground):
        if bison.state == bison.DESCENT :
            bison.state = bison.ROTATING
            bison.FLYING_SPEED_KMPH -= 10
            bison.ENERGY_LOSS += 0.2
            for jellybear in jellybears :
                jellybear.RUNNING_SPEED_KMPH += 10

        if bison.state == bison.ROCKETSLAM :
            bison.state = bison.RISING
            bison.FLYING_SPEED_KMPH -= 1
            bison.ENERGY_LOSS -= 1
            for jellybear in jellybears :
                jellybear.RUNNING_SPEED_KMPH += 1

        if bison.ELASTIC_ENERGY < 3 :
            bison.state = bison.KNOCKOUT
        if bison.FLYING_SPEED_KMPH < 10:
            bison.state = bison.KNOCKOUT

    for jellybear in jellybears :
        jellybear.update(frame_time)
        if collide(bison, jellybear):
            if bison.state == bison.DESCENT :
                jellybear.state = jellybear.EXPLODED
                bison.state = bison.RISING
                bison.FLYING_SPEED_KMPH -= 3
                jellybear.RUNNING_SPEED_KMPH += 3
                bison.ENERGY_LOSS -= 4

            if bison.state == bison.ROCKETSLAM :
                jellybear.state = jellybear.EXPLODED
                bison.state = bison.RISING
                bison.ENERGY_LOSS -= 4



def draw(frame_time):
    clear_canvas()
    backgroundthird.draw()
    backgroundsecond.draw()
    backgroundfirst.draw()
    upperground.draw()
    bison.draw()
    for jb in jellybear :
        jb.draw()
    ground.draw()
    update_canvas()
    pass

if __name__ == '__main__' :
    enter()