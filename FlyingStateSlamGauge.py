from pico2d import *


class FirstGauge :

    image = None

    Charging, Charged = 0,1

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/RocketSlamGauge.png')
        self.state = self.Charged
        self.frame = -1
        self.x, self.y = 58, 447

    def update(self,bison, frame_time):
        if self.state == self.Charged :
            if self.frame == 5:
                pass
            else :
                self.frame = (self.frame + 1) % 6
            if bison.rocketgauge < 3:
                self.state = self.Charging

        if self.state == self.Charging :
            if bison.rocketgauge <= 2:
                self.frame = 0
            if bison.rocketgauge == 2.25:
                self.frame = 1
            if bison.rocketgauge == 2.5:
                self.frame = 2
            if bison.rocketgauge == 2.75:
                self.frame = 3
            if bison.rocketgauge == 3:
                self.state = self.Charged

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


class SecondGauge :

    image = None

    Charging, Charged = 0,1

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/RocketSlamGauge.png')
        self.state = self.Charged
        self.frame = -1
        self.x, self.y = 58, FirstGauge().y - 90

    def update(self,bison, frame_time):
        if self.state == self.Charged :
            if self.frame == 5:
                pass
            else :
                self.frame = (self.frame + 1) % 6
            if bison.rocketgauge < 2 :
                self.state = self.Charging

        if self.state == self.Charging :
            if bison.rocketgauge <= 1:
                self.frame = 0
            if bison.rocketgauge == 1.25:
                self.frame = 1
            if bison.rocketgauge == 1.5:
                self.frame = 2
            if bison.rocketgauge == 1.75:
                self.frame = 3
            if bison.rocketgauge == 2 or bison.rocketgauge > 2 :
                self.state = self.Charged

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

class ThirdGauge :

    image = None

    Charging, Charged = 0,1

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/RocketSlamGauge.png')
        self.state = self.Charged
        self.frame = -1
        self.x, self.y = 58, SecondGauge().y - 90

    def update(self, bison, frame_time):
        if self.state == self.Charged :
            if self.frame == 5:
                pass
            else :
                self.frame = (self.frame + 1) % 6
            if bison.rocketgauge < 1 :
                self.state = self.Charging

        if self.state == self.Charging :
            if bison.rocketgauge == 0:
                self.frame = 0
            if bison.rocketgauge == 0.25:
                self.frame = 1
            if bison.rocketgauge == 0.5:
                self.frame = 2
            if bison.rocketgauge == 0.75:
                self.frame = 3
            if bison.rocketgauge == 1 or bison.rocketgauge > 1:
                self.state = self.Charged

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


