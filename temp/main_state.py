import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None

running=True




class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    global running
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):

        if running==True:
            self.frame = (self.frame + 1) % 8
            self.x += 5*self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1
        delay(0.05)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)




def enter():
    global boy,grass,running
    boy=Boy()
    grass=Grass()
    running=True

    pass


def exit():
    global boy,grass
    del(boy)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_RETURN:
            #running=False if running==True else running=True
            if running==True:
                running=False
            else:
                running=True
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
           game_framework.change_state(title_state)

    pass


def update():
    boy.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass





