from pico2d import*



class Hero():
    imgStand=None
    imgWalk=None
    imgDash=None
    attack1=None
    guard=None
    jump=None
    spd=0
    def __init__(self):
        self.x,self.y=200,100
        self.frame=0
        self.state=0
        self.dir=1
        if Hero.imgStand==None:
            self.imgStand = load_image('game_image\\character\\hero\\stand.png')
        if Hero.imgWalk==None:
            self.imgWalk = load_image('game_image\\character\\hero\\walk.png')
        if Hero.imgDash==None:
            self.imgDash = load_image('game_image\\character\\hero\\dash.png')
        if Hero.attack1==None:
            self.attack1 = load_image('game_image\\character\\hero\\attack1.png')
        if Hero.guard==None:
            self.guard = load_image('game_image\\character\\hero\\guard.png')
        if Hero.jump==None:
            self.jump = load_image('game_image\\character\\hero\\jump.png')


    def draw(self):
        if self.state==0:
            self.imgStand.clip_draw(self.frame*100,self.dir*150,100,150,self.x,self.y,150,225)
        if self.state==1:
            self.imgWalk.clip_draw(self.frame*110,self.dir*150,110,150,self.x,self.y,165,225)
        if self.state==2:
            self.imgDash.clip_draw(self.frame*200,self.dir*150,200,150,self.x,self.y,300,225)
        if self.state==3:
            self.attack1.clip_draw(self.frame*250,self.dir*150,250,150,self.x,self.y,325,225)
        if self.state==4:
            self.guard.clip_draw(self.frame*150,self.dir*150,150,150,self.x,self.y,225,225)
        if self.state==5:
            self.jump.clip_draw(self.frame*100,self.dir*150,100,150,self.x,self.y,150,225)





    def update(self):

        self.frame+=1

        if self.state==0:
            self.frame%=2
        elif self.state==1 or self.state==2:
            self.frame%=4
        elif self.state==3:
            self.frame%=5
        elif self.state==4:
            self.frame=0
        elif self.state==5:
            # if self.frame==0:
            #     self.y+=50
            if self.frame==1:
                self.y+=50
            if self.frame==2:
                self.y-=0
            if self.frame==3:
                self.y-=50

            if self.frame==4:
                self.state=0
                self.frame=0








class Goblin():
    image=None
    spd=0
    def __init__(self):
        self.x,self.y=200,100
        self.frame=0
        self.state=0
        self.dir=0
        if Goblin.image==None:
            self.image = load_image('game_image\\character\\monster\\goblin_stand.png')
    def draw(self):
         self.image.clip_draw(0,0,60,100,self.x,self.y,60,100)
    def update(self):
        self.frame+=1
