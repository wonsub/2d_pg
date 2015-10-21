
import random
import json
import os
import math
from pico2d import *
from math import *

import game_framework
import Letter
import BackGround
import Character

global delaytime,Timer
global road,castle,forest
global goblin,goblins
global goblincnt



delaytime=None
#숫자를 문자로 : str(숫자)
#문자를 숫자로 : 자료형(문자) ex)int(s)

name = "MainState"

def enter():
    global delaytime,Timer
    global road,castle,forest
    global goblin,goblins
    global goblincnt

    goblincnt=1
    delaytime=10

    forest=[BackGround.Forest() for i in range(2)]
    for i in range(2):
        forest[i].x=600+1200*i
        forest[i].y=450
    goblins=[Character.Goblin() for i in range(100)]
    for i in range(100):
        goblins[i].x=400
        goblins[i].y=150





    road=BackGround.Road()
    road.x=1200
    road.y=75

    castle=BackGround.Castle()
    castle.x=300
    castle.y=400

    Timer=Letter.Font()
    Timer.contet=180
    Timer.x=650
    Timer.y=800
    pass



def exit():
    close_canvas()
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    global delaytime,Timer
    global road,castle,forest
    global goblin,goblins

    global goblincnt

    events=get_events()
    for event in events:
        if event.type==SDL_QUIT or event.key==SDLK_ESCAPE:
            game_framework.quit()
        if event.type==SDL_KEYDOWN and event.key==SDLK_1:
            goblincnt+=1


    pass

def update():
    global delaytime,Timer
    global road,castle,forest
    global goblin,goblins

    global goblincnt

    delaytime+=1
    if(delaytime%10==9): #1초마다 작동할수 있게 변경
        if(Timer.contet>0):
            Timer.contet-=1
        if(Timer.contet==0):
            game_framework.quit()

    for goblin in goblins[:goblincnt]:
        goblin.update()


    delay(0.1)


    pass


def draw():
    global delaytime,Timer
    global road,castle,forest
    global goblin,goblins

    global goblincnt


    clear_canvas()
    for i in range(2):
        forest[i].draw()
    road.draw()
    castle.draw()
    for goblin in goblins[:goblincnt]:
        goblin.draw()



    Timer.draw()
    update_canvas()
    pass





