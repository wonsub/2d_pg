from pico2d import*
class Goblin():
    image=None
    def __init__(self):
        self.x,self.y=200,100
        self.edge_distance=0
        if Goblin.image==None:
            self.image = load_image('game_image\\character\\monster\\goblin_stand.png')
    def draw(self):
         self.image.clip_draw(0,0,60,100,self.x,self.y,100,150)
    def update(self):
        self.x+=10