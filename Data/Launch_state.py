from pico2d import *
import os

Launching = True
shivering = 0

class LaunchBackground :
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempMAP.png')

    def draw(self):
        self.image.draw(400, 300)


class Bison :
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempB.png')
        self.x, self.y = ( 200, 100 )

    def update(self):
        global shivering
        if ( shivering + 1 ) % 2 == 1 :
            self.x = self.x + 2
            shivering = shivering + 1
        else :
            self.x = self.x - 2
            shivering = shivering + 1

    def draw(self):
        self.image.draw(self.x, self.y)



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
BS = Bison()

while Launching :
    handle_events()
    clear_canvas()
    LB.draw()
    BS.update()
    BS.draw()
    update_canvas()

close_canvas()
