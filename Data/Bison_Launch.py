from pico2d import *
import random
import os

name = "Bison_Launch"

PIXEL_PER_METER = 108
ShootingFail = False
ShootingNormal = False
ShootingBoost = False

class Bison :
    def __init__(self):
        os.chdir('E:\Pytemp\Burrito\Pandaria\Images')
        self.image = load_image('TempB.png')
        self.x, self.y = ( 300, 250 )

    def update(self, frame_time):
        ATTACK_SPEED_MPS = 15
        ATTACK_SPEED_MPM = (ATTACK_SPEED_MPS * 60.0)
        ATTACK_SPEED_KMPH = (ATTACK_SPEED_MPM * 60.0 / 1000.0)
        ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)
        distance = ATTACK_SPEED_PPS * frame_time
        # 시속 54 Km / 초당 1620 픽셀이동

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
            if ShootingNormal == True :
                self.image = load_image('TempLaunch.png')
                # 750위치에서 몬스터와 부딪힘을 구현합니다.
                if self.x <= 750:
                    self.x += distance
                if self.x > 750 and MonsterHit == 0:
                    MonsterHit = 1

                # 부딪힌 후 날아가는 모습을 구현합니다.
                if self.x > 750:
                    if self.x < 900:
                        self.x = self.x + 0.4
                        self.y = self.y + 0.5
                    elif self.x >= 900:
                        self.x = self.x + 4
                        self.y = self.y + 5

            if ShootingBoost == True :
                self.image = load_image('TempBoosted.png')
                # 750위치에서 몬스터와 부딪힘을 구현합니다.
                if MonsterHit == 0:
                    self.x += distance
                if self.x >= 750 and MonsterHit == 0:
                    MonsterHit = 1

                # 부딪힌 후 날아가는 모습을 구현합니다.
                if self.x > 750:
                    if self.x < 900:
                        self.x = self.x + 0.4
                        self.y = self.y + 0.5
                    elif self.x >= 900:
                        self.x = self.x + 4
                        self.y = self.y + 5

            if ShootingFail == True :
                self.image = load_image('TempFail.png')
                # 750위치에서 몬스터와 부딪힘을 구현합니다.
                if self.x <= 750 and MonsterHit == 0:
                    self.x += distance
                if self.x > 750 and MonsterHit == 0:
                    MonsterHit = 1

                # 부딪힌 후 튕겨지는 모습을 구현합니다.
                    if self.x < 900:
                        self.x = self.x - 0.4
                        self.y = self.y + 0.5
                    elif self.x >= 900:
                        self.x = self.x - 4
                        self.y = self.y - 5


    def draw(self):
        self.image.draw(self.x, self.y)

BS = Bison()

def draw():
    BS.draw()

def update():
    BS.update()