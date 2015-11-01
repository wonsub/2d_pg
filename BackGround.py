from pico2d import *
class Road:
    image=None
    def __init__(self):
        self.x,self.y=None,None
        if Road.image==None:
            self.image=load_image('game_image\\background\\road.png')

    def draw(self):
        self.image.clip_draw(0,0,2400,150,self.x,self.y,2400,150)


class Forest:
    image=None
    def __init__(self):
        self.x,self.y=None,None
        if Road.image==None:
            self.image=load_image('game_image\\background\\forest.png')

    def draw(self):
        self.image.clip_draw(0,0,600,300,self.x,self.y,800,600)

class Castle:
    image=None
    def __init__(self):
        self.x,self.y=None,None
        self.frame=0
        self.state=0
        self.dir=1
        if Road.image==None:
            self.image=load_image('game_image\\background\\castle.png')

    def draw(self):
        self.image.clip_draw(self.frame*400,self.dir*400,400,400,self.x,self.y,400,400)

