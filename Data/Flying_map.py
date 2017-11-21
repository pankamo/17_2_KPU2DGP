from pico2d import *
import Launch_state

scrollground = 1
scrollmap = 1
groundspeed = 60 # KMPH

class Candygrass:
    def __init__(self):
        global distance
        global scrollground
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempGrass.png')

        if scrollground % 3 == 1:
            self.x, self.y = ( 540, 50 )
            scrollground += 1
        elif scrollground % 3 == 2 :
            self.x, self.y = ( 1820, 50 )
            scrollground += 1
        elif scrollground % 3 == 0 :
            self.x, self.y = ( 3100, 50 )

    def update(self,frame_time):
        global groundspeed
        PIXEL_PER_METER = Launch_state.PIXEL_PER_METER
        frame_time = Launch_state.frame_time
        GROUND_SPEED_KMPH = groundspeed
        GROUND_SPEED_MPM = (GROUND_SPEED_KMPH * 1000.0 / 60)
        GROUND_SPEED_MPS = (GROUND_SPEED_MPM / 60)
        GROUND_SPEED_PPS = (GROUND_SPEED_MPS * PIXEL_PER_METER)
        distance = GROUND_SPEED_PPS * frame_time
        self.x -= distance
        if self.x <= -740 :
            self.x = 1820

    def draw(self):
        self.image.draw(self.x, self.y)

class Scrollingscene:
    def __init__(self):
        global scene_distance
        global scrollmap
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempScene.png')
        PIXEL_PER_METER = Launch_state.PIXEL_PER_METER
        frame_time = Launch_state.frame_time
        SCENE_SPEED_KMPH = 5
        SCENE_SPEED_MPM = (SCENE_SPEED_KMPH * 1000.0 / 60)
        SCENE_SPEED_MPS = (SCENE_SPEED_MPM / 60)
        SCENE_SPEED_PPS = (SCENE_SPEED_MPS * PIXEL_PER_METER)
        scene_distance = SCENE_SPEED_PPS * frame_time
        if scrollmap % 3 == 1:
            self.x, self.y = ( 540, 300 )
            scrollmap += 1
        elif scrollmap % 3 == 2 :
            self.x, self.y = ( 1820, 300 )
            scrollmap += 1
        elif scrollmap % 3 == 0 :
            self.x, self.y = ( 3100, 300 )

    def update(self,frame_time):
        self.x -= scene_distance
        if self.x <= -740 :
            self.x = 1820

    def draw(self):
        self.image.draw(self.x, self.y)