import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

hero = None
castle = None
font = None

AUTO_KEY=None
running=True


class Castle:
    def __init__(self):
        self.x,self.y=240,200
        self.edge_distance=0
        self.image = load_image('castle.png')


    def draw(self):
        self.image.draw( self.x,  self.y)



class Hero:

    def __init__(self):
        self.x, self.y = 300,60
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


                if self.x>0 and self.x-castle.x<460:
                    self.x += 20*self.dir

                else:
                    castle.x-=20*self.dir
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
    global hero,castle,running
    hero=Hero()
    castle=Castle()
    running=True

    pass


def exit():
    global hero,castle
    del(hero)
    del(castle)
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
    hero.update()
    pass


def draw():
    clear_canvas()
    castle.draw()
    hero.draw()
    update_canvas()
    pass





