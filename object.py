__author__ = 'wonsub'
from pico2d import*



class Tower():
    image=None

    def __init__(self):
        self.x,self.y=200,100
        self.frame=0
        self.state=0
        self.dir=1
        if Tower.image==None:
            self.image = load_image('game_image\\object\\tower.png')


    def draw(self):

        self.image.clip_draw(self.frame*300,self.dir*600,300,600,self.x,self.y,300,800)

    def update(self):

        self.frame=0









