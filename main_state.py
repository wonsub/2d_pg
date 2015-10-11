
import random
import json
import os

import math
from pico2d import *
from math import *

import game_framework
import title_state



name = "MainState"

hero = None
castle = None
tile=None
font = None
catupult=None

AUTO_KEY=None
running=True

class Freefall:

    def __init__(self):
        self.x,self.y=0,0
        self.acceleration=10
        self.time=0
        self.spd=10
        self.angle=0
        self.PI=3.1415926535897/180
    def update(self):
        self.spd=sqrt(self.x^2+self.y^2)
        self.x= self.spd*cos(self.angle*self.PI)
        self.y= self.spd*sin(self.angle*self.PI)



class Catupult:
    def __init__(self):
        self.x,self.y=240,470
        self.stone_x,self.stone_y=  self.x,self.y
        self.frame,self.stone_frame=0,0 # body / stone
        self.dir=1
        self.state=1  # 0 wait/ 1 launch /2 reload
        self.Rlaunch=load_image('Rcatapult_launch.png')
        self.Llaunch=load_image('Lcatapult_launch.png')
        self.Rreload=load_image('Rcatapult_reload.png')
        self.Lreload=load_image('Lcatapult_reload.png')
        self.stone=load_image('stone.png')
    def draw(self):
        if self.state==1:
            if(self.dir==1):
                self.Rlaunch.clip_draw(self.frame*188,0,188,200,self.x,self.y)
            elif(self.dir==-1):
                self.Llaunch.clip_draw(self.frame*188,0,188,200,self.x,self.y)
        elif self.state==2:
            if(self.dir==1):
                self.Rreload.clip_draw(2+self.frame*188,0,186,200,self.x,self.y)
            elif(self.dir==-1):
                self.Lreload.clip_draw(2+self.frame*188,0,186,200,self.x,self.y)
        self.stone.clip_draw(self.stone_frame*63,0,63,100,self.stone_x,self.stone_y)
        self.stone_x+=10
        if self.stone_y<self.y+200:
            self.stone_y+=30
        else:
            self.stone_y-=3
    def update(self):
       if self.state==0:
           self.stone_frame = 0
           self.frame = 0
       else:

           self.stone_frame = (self.stone_frame + 1) % 3
           if self.state==1:
              self.frame = (self.frame + 1) % 7
              if self.frame==6:
                  self.state=2
                  self.frame=0
           elif self.state==2:
               self.frame = (self.frame + 1) % 8
               if self.frame==7:
                  self.state=1
                  self.frame=0








class Tile:
    def __init__(self):
        self.x,self.y=100,25
        self.image=load_image('tile.png')
    def draw(self):
        self.image.clip_draw(0,100,200,50,self.x,self.y)



class Castle:
    def __init__(self):
        self.x,self.y=240,220
        self.edge_distance=0
        self.image = load_image('castle.png')


    def draw(self):
        self.image.draw(self.x,  self.y)



class Hero:

    def __init__(self):
        self.x, self.y = 300,80
        self.frame_dash = 0
        self.frame_stop=0
        self.Rdash = load_image('Rdash.png')
        self.Ldash = load_image('Ldash.png')
        self.Rstop=load_image('Rstand_stop.png')
        self.Lstop=load_image('Lstand_stop.png')
        self.dir = 1
        self.state=1    #   /1 stand /2 dash

    def update(self):
        global AUTO_KEY,running
        if running==True:

            self.frame_stop = (self.frame_stop + 3) % 4
            self.frame_dash = (self.frame_dash + 1) % 8

            if AUTO_KEY==True:
                if self.x<220 and self.dir==-1:
                    AUTO_KEY=False


                if self.x>20 and self.x-castle.x<460:
                    self.x += 20*self.dir


                else :

                    castle.x-=20*self.dir
                    catupult.x-=20*self.dir
                    catupult.stone_x-=20*self.dir
                    for i in range(20):
                        tile[i].x-=20*self.dir
                '''
                if self.x >= 800:
                    self.dir = -1
                elif self.x <= 0:
                    self.dir = 1
                    '''

        delay(0.05)

    def draw(self):

        if self.state==1:
                if hero.dir==1:
                    self.Rstop.clip_draw(self.frame_stop * 95, 0, 95, 120, self.x, self.y)
                elif hero.dir==-1:
                    self.Lstop.clip_draw(self.frame_stop * 95, 0, 95, 120, self.x, self.y)
        elif self.state==2:
            if hero.dir==1:
                self.Rdash.clip_draw(self.frame_dash * 185, 0, 185, 120, self.x, self.y)
            elif hero.dir==-1:
                self.Ldash.clip_draw(self.frame_dash * 185, 0, 185, 120, self.x, self.y)





def enter():
    global hero,castle,running,tile,catupult
    hero=Hero()
    castle=Castle()
    catupult=Catupult()
    tile=[Tile() for i in range(20)]
    for i in range(20):
        tile[i].x=200*i

    running=True

    pass


def exit():
    global hero,castle,catupult
    del(hero)
    del(castle)
    del(catupult)

    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global running,AUTO_KEY
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:


            if event.key==SDLK_RIGHT :
                AUTO_KEY=True
                hero.dir=1
                hero.state=2
                #if dir==-1:
                #        hero.x+=40



            elif event.key==SDLK_LEFT:
                AUTO_KEY=True
                hero.dir=-1
                hero.state=2
                if hero.x<100:
                    hero.x+=40



            elif running==True  and event.key==SDLK_RETURN:
                running=False
            else:
                running=True
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
           game_framework.change_state(title_state)
        elif event.type==SDL_KEYUP:
            hero.state=1
            AUTO_KEY=False


    pass


def update():
    Freefall.update()
    hero.update()
    catupult.update()
    pass


def draw():

    clear_canvas()
    for i in range(20):
        tile[i].draw()
    castle.draw()
    catupult.draw()

    hero.draw()

    update_canvas()
    pass





