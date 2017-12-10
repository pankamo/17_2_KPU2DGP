from pico2d import *
import random

class GaugeBar:
    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/Gauge.png')
            self.x, self.y = (540, 300)

    def update(self, frame_time, bison):
        if bison.state == bison.HITTING :
            self.y += 1

    def draw(self):
        self.image.draw(self.x, self.y)


class GaugePoint:
    image = None

    def __init__(self):
        if self.image == None :
            self.image = load_image('./Images/GaugePin.png')
            self.x, self.y = (random.randint (200,880), 365)
            self.direction = random.choice([-1,1])

    def update(self, frame_time, bison):
        if bison.state == bison.SHIVERING :
            #PIXEL_PER_METER = 108
            GAUGE_SPEED_PPS = 600
            distance = GAUGE_SPEED_PPS * frame_time

            if self.direction :
                self.x = clamp (200, self.x + (self.direction * distance), 880)
                if self.x == 200 or self.x == 880 :
                    self.direction = -(self.direction)
                    pass

        if bison.state == bison.ATTACKING :
            if (self.x >= 490 and self.x <= 590):
                bison.state = bison.BOOSTERED
            elif (self.x < 370 or self.x > 710):
                bison.state = bison.FAILED
            else :
                bison.state = bison.ATTACKING
            pass

        if bison.state in (bison.HITTING, bison.FLYING, bison.REFLECTING) :
            self.y += 1

    def draw(self):
        self.image.draw(self.x, self.y)

