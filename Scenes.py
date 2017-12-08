from pico2d import *

class Ground :

    image = None

    def __init__(self):
        self.x, self.y = ( 540, 50 )
        if self.image == None :
            self.image = load_image('./Images/TempGrass.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 540, self.y - 50, self.x + 540, self.y + 25



class Background :

    image = None

    def __init__(self):
        self.x, self.y = ( 540, 300 )
        if self.image == None :
            self.image = load_image('./Images/TempScene.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)