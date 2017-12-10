from pico2d import *

import game_framework


name = 'LogoStateSecond'
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('./Images/TitleLogoSecond.png')
    pass

def exit():
    global image
    del(image)
    pass

import MainTitleState

def update(frame_time):
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        game_framework.push_state(MainTitleState)
    delay(0.01)
    logo_time += 0.01
    pass

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(540, 300)
    update_canvas()
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
    pass

def pause(): pass

def resume(): pass
