import pico2d


speed = None

def SaveBisonSpeed(bison):
    global speed
    speed = bison.SaveBisonSpeed()

def LoadBisonSpeed(bison):
    bison.FLYING_SPEED_KMPH = speed
