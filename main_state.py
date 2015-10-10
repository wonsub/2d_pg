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

running=True


class Castle:
    def __init__(self):
        self.image = load_image('castle.png')

    def draw(self):
        self.image.draw(240, 200)



class Hero:
    global running
    def __init__(self):
        self.x, self.y = 0, 45
        self.frame = 0
        self.image = load_image('swordman.png')
        self.dir = 1

    def update(self):

        if running==True:
            self.frame = (self.frame + 1) % 19
            self.x += 5*self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1
        delay(0.05)

    def draw(self):
        self.image.clip_draw(self.frame * 380, 0, 380, 120, self.x, self.y)




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
    hero.update()
    pass


def draw():
    clear_canvas()
    castle.draw()
    hero.draw()
    update_canvas()
    pass





