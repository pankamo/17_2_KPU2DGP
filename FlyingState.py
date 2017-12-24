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

jelly_popping_sound = None
crashing_sound = None

def load_JellyPoppingSound():
    global jelly_popping_sound
    jelly_popping_sound = load_wav('./Sounds/JellyPopping.wav')
    jelly_popping_sound.set_volume(80)

def load_CrashingSound():
    global crashing_sound
    crashing_sound = load_wav('./Sounds/GroundCrashing.wav')
    crashing_sound.set_volume(80)

def play_JellyPoppingSound():
    jelly_popping_sound.play()

def play_CrashingSound():
    crashing_sound.play()

def create_FlyingStage():
    global bison,\
            ground, upperground,\
            backgroundfirst, backgroundsecond, backgroundthird,\
            jellybear, jellybears

    bison = Bison()
    upperground = UpperGround()
    ground = Ground()
    jellybear = JellyBear()
    backgroundfirst = BackgroundFirst()
    backgroundsecond = BackgroundSecond()
    backgroundthird = BackgroundThird()


    jellybear = [JellyBear() for jellybear in range(6)]
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
    #open_canvas(1080, 600, sync=60)
    hide_lattice()
    game_framework.reset_time()
    create_FlyingStage()
    bgm_play()
    load_CrashingSound()
    load_JellyPoppingSound()

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
            else :
                bison.handle_event(event)


def update( frame_time):
    backgroundfirst.update(bison, frame_time)
    backgroundsecond.update(bison, frame_time)
    backgroundthird.update(bison,frame_time)
    upperground.update(bison,frame_time)
    bison.update(frame_time)
    ground.update(bison, frame_time)
    if falling(bison, ground):
        if bison.state == bison.DESCENT :
            play_CrashingSound()
            bison.ENERGY_LOSS += 0.2
            if bison.FLYING_SPEED_KMPH > 10 :
                bison.FLYING_SPEED_KMPH -= 10
                for jellybear in jellybears :
                    jellybear.RUNNING_SPEED_KMPH += 10
                    bison.state = bison.ROTATING

            elif bison.FLYING_SPEED_KMPH < 10 :
                bison.state = bison.KNOCKOUT

        if bison.state == bison.ROCKETSLAM :
            play_CrashingSound()
            bison.ENERGY_LOSS -= 1
            if bison.FLYING_SPEED_KMPH > 1 :
                bison.FLYING_SPEED_KMPH -= 1
                for jellybear in jellybears:
                    jellybear.RUNNING_SPEED_KMPH += 1
                bison.state = bison.RISING


    for jellybear in jellybears :
        jellybear.update(bison, frame_time)
        if collide(bison, jellybear):
            if bison.state == bison.DESCENT :
                play_JellyPoppingSound()
                jellybear.state = jellybear.EXPLODED
                bison.state = bison.RISING
                if bison.FLYING_SPEED_KMPH > 3 :
                    bison.FLYING_SPEED_KMPH -= 3
                    jellybear.RUNNING_SPEED_KMPH += 3
                bison.ENERGY_LOSS -= 4

            if bison.state == bison.ROCKETSLAM :
                play_JellyPoppingSound()
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