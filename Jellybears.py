from pico2d import *
import random
import Launch_state
import math

class Bear:
    global frame_time
    frame_time = Launch_state.frame_time

    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempBear.png')
        (self.x, self.y) = 1400, 100
        self.Velocity = random.randint(120, 600)

    def update(self,frame_time):
        self.x -= self.Velocity * frame_time
        if self.x <= -600 :
            self.x = 1400

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        r = 50
        t = 0
        x = self.x - math.cos(t) * r
        y = self.y + math.sin(t) * r
        while True :
            t += 0.25
            return x, y, r

class PoliceBear(Bear):
    global frame_time
    frame_time = Launch_state.frame_time

    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempPolice.png')
        (self.x, self.y) = 2400, 100
        self.Velocity = random.randint(120, 400)

    def update(self,frame_time):
        self.x -= self.Velocity * frame_time
        if self.x <= -800 :
            self.x = 1400

    def draw(self):
        self.image.draw(self.x, self.y)

    def remove(self):
        pass

class RocketBear(Bear):
    global frame_time
    frame_time = Launch_state.frame_time

    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempRocBe.png')
        (self.x, self.y) = 3600, 100
        self.Velocity = random.randint(80, 160)

    def update(self,frame_time):
        self.x -= self.Velocity * frame_time
        if self.x <= -3600 :
            self.x = 1400

    def draw(self):
        self.image.draw(self.x, self.y)
