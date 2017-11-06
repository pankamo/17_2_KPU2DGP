from pico2d import *
import os

Launching = True
shivering = 0
Shooting = False
MonsterHit = 0

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
        self.x, self.y = ( 150, 250 )

    def update(self):
        global Shooting
        if Shooting == False :
            global shivering
            if ( shivering + 1 ) % 2 == 1 :
                self.x = self.x + 2
                shivering = shivering + 1
            else :
                self.x = self.x - 2
                shivering = shivering + 1

        elif Shooting == True :
            global MonsterHit
            self.image = load_image('TempLaunch.png')

            if self.x <= 550 :
                self.x = self.x + 5

            if self.x > 500 and MonsterHit == 0:
                MonsterHit = 1

            if self.x > 550 :
                if self.x < 700 :
                    self.x = self.x + 0.4
                    self.y = self.y + 0.5
                elif self.x >= 700 :
                    self.x = self.x + 4
                    self.y = self.y + 5


    def draw(self):
        self.image.draw(self.x, self.y)


class Monster:
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempM.png')
        self.x, self.y = (600, 280)

    def update(self):
        if Shooting == True:
            global MonsterHit
            if MonsterHit >= 1 and MonsterHit < 500 :
                self.image = load_image('TempMHit.png')
                self.x = self.x + 0.1
                MonsterHit = MonsterHit + 1
            if MonsterHit == 500 :
                pass
        elif Shooting == False:
            pass

    def draw(self):
        self.image.draw(self.x, self.y)

class Rope:
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempR.png')
        self.x, self.y = ( 100, 250 )

    def update(self):
        global Shooting
        if Shooting == False :
            global shivering
            if ( shivering + 1 ) % 2 == 1 :
                self.x = self.x - 2
            else :
                self.x = self.x + 2
        if Shooting == True :
            self.x = min(200, self.x + 10)

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global Launching
    global Shooting
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Launching = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Launching = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            Shooting = True
            pass

open_canvas()

LB = LaunchBackground()
BS = Bison()
MS = Monster()
RP = Rope()

while Launching :
    handle_events()
    clear_canvas()
    LB.draw()
    MS.update()
    MS.draw()
    BS.update()
    BS.draw()
    RP.update()
    RP.draw()
    update_canvas()

close_canvas()
