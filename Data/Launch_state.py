from pico2d import *
import os

Launching = True

class LaunchBackground :
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempMAP.png')

    def draw(self):
        self.image.draw(400, 300)



def handle_events():
    global Launching
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Launching = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Launching = False
            pass

open_canvas()

LB = LaunchBackground()

while Launching :
    handle_events()
    clear_canvas()
    LB.draw()
    update_canvas()

close_canvas()
