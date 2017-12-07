from pico2d import *

import game_framework

from BisonInLaunchState import Bison
from Monster import Monster

name = "LaunchState"

bison = None
monster = None
PIXEL_PER_METER = 108


def create_LaunchingStage():
    global bison, monster
    bison = Bison()
    monster = Monster()
    pass

def destroy_LaunchingStage():
    global bison, monster

    del(bison)
    del(monster)

def enter():
    open_canvas( 1080, 600 )
    game_framework.reset_time()
    create_LaunchingStage()

def exit():
    destroy_LaunchingStage()
    close_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def update(frame_time):
    bison.update(frame_time)
    monster.update(frame_time)

def draw(frame_time):
    clear_canvas()
    bison.draw()
    monster.draw()
    update_canvas()
    pass

