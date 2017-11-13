from pico2d import *
import random
import os

name = "Launch_State"

Launching = True
shivering = 0
Shooting = False
MonsterHit = 0
Direction = None

# 화면 내의 너비 : 10 METER로 설정
# 미터당 픽셀 : 108 px
PIXEL_PER_METER = 108

class LaunchBackground :
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempMAP.png')

    def draw(self):
        self.image.draw(540, 300)


class Bison :
    global PIXEL_PER_METER
    ATTACK_SPEED_MPS = 15
    ATTACK_SPEED_MPM = (ATTACK_SPEED_MPS * 60.0)
    ATTACK_SPEED_KMPH = (ATTACK_SPEED_MPM * 60.0 / 1000.0)
    ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)
    # 시속 54 Km / 초당 1620 픽셀이동

    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempB.png')
        self.x, self.y = ( 300, 250 )

    def update(self, frame_time):
        distance = Bison.ATTACK_SPEED_PPS * frame_time
        global Shooting
        # 핸들이벤트에서 SPACE -> Shooting이 발동되면
        # 이를 받아사용합니다
        if Shooting == False :
            global shivering
            if ( shivering + 1 ) % 2 == 1 :
                self.x = self.x + 2
                shivering = shivering + 1
            else :
                self.x = self.x - 2
                shivering = shivering + 1
            # 밧줄탄력에 의한 캐릭터 떨림 구현입니다.

        elif Shooting == True :
            global MonsterHit
            self.image = load_image('TempLaunch.png')

            # 750위치에서 몬스터와 부딪힘을 구현합니다.
            if self.x <= 750 :
                self.x += distance
            if self.x > 750 and MonsterHit == 0:
                MonsterHit = 1

            # 부딪힌 후 날아가는 모습을 구현합니다.
            if self.x > 750 :
                if self.x < 900 :
                    self.x = self.x + 0.4
                    self.y = self.y + 0.5
                elif self.x >= 900 :
                    self.x = self.x + 4
                    self.y = self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)


class Monster:
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempM.png')
        self.x, self.y = (800, 280)

    def update(self, frame_time):
        if Shooting == True:
            global MonsterHit
            # 몬스터가 부딪힌 후 밀려나는 모습을 구현합니다.
            if MonsterHit >= 1 and MonsterHit < 400 :
                self.image = load_image('TempMHit.png')
                self.x = self.x + 0.1
                MonsterHit = MonsterHit + 1
            if MonsterHit == 400 :
                pass
        elif Shooting == False:
            pass

    def draw(self):
        self.image.draw(self.x, self.y)

class Rope:
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempR.png')
        self.x, self.y = ( 250, 250 )

    def update(self, frame_time):
        global Shooting
        if Shooting == False :
            global shivering
            if ( shivering + 1 ) % 2 == 1 :
                self.x = self.x - 2
            else :
                self.x = self.x + 2
        if Shooting == True :
            self.x = min(300, self.x + 10)

    def draw(self):
        self.image.draw(self.x, self.y)

class Guagebar:
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempGuage.png')
        self.x, self.y = (540, 550)

    def draw(self):
        if MonsterHit < 1:
            self.image.draw(self.x, self.y)
        if MonsterHit >= 1:
            self.image.draw(self.x, self.y)
            self.y = self.y + 1
        # 몬스터와 부딪히면 게이지바가 사라집니다

class Guagepoint:
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempGuagePoint.png')
        self.x, self.y = (random.randint(200,880), 450)
        global direction
        direction = [-1,1]
        direction = random.choice(direction)

    def update(self, frame_time):
        # 게이지포인트가 좌우반복운동하도록 합니다.
        if Shooting == False:
            global direction
            if direction == 1:
                self.x = min(880, self.x + (direction * 3))
                if self.x == 880:
                    direction = -1
            if direction == -1:
                self.x = max(200, self.x + (direction * 3))
                if self.x == 200:
                    direction = 1
        if Shooting == True:
            pass

    def draw(self):
        if MonsterHit < 1:
            self.image.draw(self.x, self.y)
        if MonsterHit >= 1:
            self.image.draw(self.x, self.y)
            self.y = self.y + 1

def handle_events(frame_time):
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

current_time = 0.0
def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

open_canvas(1080,600)

LB = LaunchBackground()
BS = Bison()
MS = Monster()
RP = Rope()
GB = Guagebar()
GP = Guagepoint()

while Launching :

    frame_time = get_frame_time()
    handle_events(frame_time)
    clear_canvas()
    LB.draw()
    MS.update(frame_time)
    MS.draw()
    BS.update(frame_time)
    BS.draw()
    RP.update(frame_time)
    RP.draw()
    GB.draw()
    GP.update(frame_time)
    GP.draw()
    update_canvas()

close_canvas()
