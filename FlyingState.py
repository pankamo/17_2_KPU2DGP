from pico2d import *

import math

import game_framework

import LaunchState

from BisonInFlyingState import Bison
from Jellybears import *
from FlyingStateBackgrounds import *
from FlyingStateSlamGauge import *

name = "FlyingState"

bison = None
greenjelly = None

mudjelly = None
rocketbear = None
bombbear = None

ground = None
upperground = None
background = None

firstgauge = None
secondgauge = None
thirdgauge = None

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

def load_JellyPoopSound():
    global jelly_poop_sound
    jelly_poop_sound = load_wav('./Sounds/JellyPoop.wav')
    jelly_poop_sound.set_volume(100)

def load_JellyBoostSound():
    global jelly_boost_sound
    jelly_boost_sound = load_wav('./Sounds/JellyBooster.wav')
    jelly_boost_sound.set_volume(80)

def load_KnockoutSound():
    global KnockoutSound
    KnockoutSound = load_wav('./Sounds/BooSound.wav')
    KnockoutSound.set_volume(100)

def play_JellyPoppingSound():
    jelly_popping_sound.play()

def play_CrashingSound():
    crashing_sound.play()

def play_JellyPoopSound():
    jelly_poop_sound.play()

def play_JellyBoostSound():
    jelly_boost_sound.play()

def play_KnockoutSound():
    KnockoutSound.play()

def create_FlyingStage():
    global bison,\
            ground, upperground,\
            backgroundfirst, backgroundsecond, backgroundthird,\
            greenjelly, mudjelly, pinkjelly, \
            firstgauge, secondgauge, thirdgauge

    bison = Bison()
    upperground = UpperGround()
    ground = Ground()

    backgroundfirst = BackgroundFirst()
    backgroundsecond = BackgroundSecond()
    backgroundthird = BackgroundThird()

    firstgauge = FirstGauge()
    secondgauge = SecondGauge()
    thirdgauge = ThirdGauge()

    greenjelly = [GreenJelly() for i in range(6)]
    mudjelly = [MudJelly() for i in range(2)]
    pinkjelly = [PinkJelly() for i in range(1)]

    #policebear = [PoliceBear() for i in range(2)]
    #rocketbear = [RocketBear() for i in range(2)]
    #bombbear = [BombBear() for i in range(2)]

    pass

def destroy_FlyingStage():
    global bison,\
            ground, upperground,\
            backgroundfirst, backgroundsecond, backgroundthird,\
            greenjelly, mudjelly, pinkjelly, \
            firstgauge, secondgauge, thirdgauge, \
            bgm

    del(ground)
    del(upperground)
    del(backgroundfirst)
    del(backgroundsecond)
    del(backgroundthird)
    del(bison)

    del(greenjelly)
    del(mudjelly)
    del(pinkjelly)

    del(bgm)

    del(firstgauge)
    del(secondgauge)
    del(thirdgauge)

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
    load_JellyPoopSound()
    load_JellyBoostSound()
    load_KnockoutSound()

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
                game_framework.change_state(LaunchState)
            else :
                bison.handle_event(firstgauge, secondgauge, thirdgauge, event)


def update(frame_time):

    firstgauge.update(bison, frame_time)
    secondgauge.update(bison, frame_time)
    thirdgauge.update(bison, frame_time)

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
                for jelly in greenjelly :
                    jelly.RUNNING_SPEED_KMPH += 10
                for jelly in mudjelly :
                    jelly.RUNNING_SPEED_KMPH += 10
                for jelly in pinkjelly :
                    jelly.RUNNING_SPEED_KMPH += 10
                bison.state = bison.ROTATING

            elif bison.FLYING_SPEED_KMPH < 10 :
                play_KnockoutSound()
                bison.state = bison.KNOCKOUT

        if bison.state == bison.ROCKETSLAM :
            play_CrashingSound()
            bison.ENERGY_LOSS -= 1
            if bison.FLYING_SPEED_KMPH > 1 :
                bison.FLYING_SPEED_KMPH -= 1
                for jelly in greenjelly:
                    jelly.RUNNING_SPEED_KMPH += 1
                for jelly in mudjelly:
                    jelly.RUNNING_SPEED_KMPH += 1
                for jelly in pinkjelly:
                    jelly.RUNNING_SPEED_KMPH += 1
                bison.state = bison.RISING

        elif bison.state == bison.RISING :
            pass


    for jelly in greenjelly :
        jelly.update(bison, frame_time)
        if collide(bison, jelly):
            if bison.state == bison.DESCENT :
                play_JellyPoppingSound()
                jelly.state = jelly.EXPLODED
                if bison.FLYING_SPEED_KMPH > 3 :
                    bison.FLYING_SPEED_KMPH -= 3
                    for jelly in greenjelly :
                        jelly.RUNNING_SPEED_KMPH += 3
                    for jelly in mudjelly :
                        jelly.RUNNING_SPEED_KMPH += 3
                    for jelly in pinkjelly :
                        jelly.RUNNING_SPEED_KMPH += 3
                bison.ENERGY_LOSS -= 2
                bison.rocketgauge += 0.25
                bison.state = bison.RISING

            if jelly.state == jelly.EXPLODED :
                pass

            if bison.state == bison.ROCKETSLAM :
                play_JellyPoppingSound()
                jelly.state = jelly.EXPLODED
                bison.ENERGY_LOSS -= 4
                bison.rocketgauge += 0.25


    for jelly in mudjelly :
        jelly.update(bison, frame_time)
        if collide(bison, jelly):
            if bison.state == bison.DESCENT :
                play_JellyPoopSound()
                jelly.state = jelly.EXPLODED
                if bison.FLYING_SPEED_KMPH > 15 :
                    bison.FLYING_SPEED_KMPH -= 15
                    for jelly in greenjelly :
                        jelly.RUNNING_SPEED_KMPH += 15
                    for jelly in mudjelly :
                        jelly.RUNNING_SPEED_KMPH += 15
                    for jelly in pinkjelly :
                        jelly.RUNNING_SPEED_KMPH += 15
                bison.ENERGY_LOSS -= 2
                bison.rocketgauge += 0.25
                bison.state = bison.ROTATING

            if jelly.state == jelly.EXPLODED :
                pass

            if bison.state == bison.ROCKETSLAM :
                play_JellyPoppingSound()
                jelly.state = jelly.EXPLODED
                bison.ENERGY_LOSS -= 4
                bison.rocketgauge += 0.25

    for jelly in pinkjelly :
        jelly.update(bison, frame_time)
        if collide(bison, jelly):
            if bison.state == bison.DESCENT :
                play_JellyBoostSound()
                jelly.state = jelly.EXPLODED
                if bison.FLYING_SPEED_KMPH < 128 :
                    bison.FLYING_SPEED_KMPH += 30
                    for jelly in greenjelly :
                        jelly.RUNNING_SPEED_KMPH -= 30
                    for jelly in mudjelly :
                        jelly.RUNNING_SPEED_KMPH -= 30
                    for jelly in pinkjelly :
                        jelly.RUNNING_SPEED_KMPH -= 30
                bison.ENERGY_LOSS -= 4
                bison.rocketgauge += 0.25
                bison.state = bison.RISING

            if jelly.state == jelly.EXPLODED :
                pass

            if bison.state == bison.ROCKETSLAM :
                play_JellyBoostSound()
                jelly.state = jelly.EXPLODED
                if bison.FLYING_SPEED_KMPH < 128 :
                    bison.FLYING_SPEED_KMPH += 30
                    for jelly in greenjelly :
                        jelly.RUNNING_SPEED_KMPH -= 30
                    for jelly in mudjelly :
                        jelly.RUNNING_SPEED_KMPH -= 30
                    for jelly in pinkjelly :
                        jelly.RUNNING_SPEED_KMPH -= 30
                bison.ENERGY_LOSS -= 4
                bison.rocketgauge += 0.25




def draw(frame_time):
    clear_canvas()
    backgroundthird.draw()
    backgroundsecond.draw()
    backgroundfirst.draw()
    upperground.draw()
    bison.draw()

    for jelly in greenjelly :
        jelly.draw()

    for jelly in mudjelly:
        jelly.draw()

    for jelly in pinkjelly:
        jelly.draw()

    ground.draw()

    firstgauge.draw()
    secondgauge.draw()
    thirdgauge.draw()

    update_canvas()
    pass

def pause():
    pass

def resume():
    pass

if __name__ == '__main__' :
    enter()