
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

global state,over,LEFT,RIGHT
global startx



delaytime=None
#숫자를 문자로 : str(숫자)
#문자를 숫자로 : 자료형(문자) ex)int(s)

name = "MainState"


def left():
    global delaytime,Timer
    global road,castle
    global forest,forests
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT
    global startx

    road.x+=5
    if road.x>1200:
        road.x-=5
        over=1


    castle.x+=5
    if castle.x>300:
        castle.x-=5
        over=1




    for goblin in goblins[:goblincnt]:
        for i in range(goblincnt):
            goblins[i].x+=5


    # for forest in forests[2]:
    for i in range(2):
        forests[i].x+=5
        if forests[i].x>600+1200*i:
            forests[i].x-=5
            over=1



def right():

    global delaytime,Timer
    global road,castle
    global forest,forests
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT

   
    road.x-=5
    if road.x<1200-900:
        road.x+=5
        over=1



    castle.x-=5
    if castle.x<300-900:
        castle.x+=5
        over=1




    for goblin in goblins[:goblincnt]:
        for i in range(goblincnt):
            goblins[i].x-=5
    #        영역 밖일 때 삭제하는거 필요


    # for forest in forests[2]:
    for i in range(2):
        forests[i].x-=5
        if forests[i].x<600+1200*i-900:
            forests[i].x+=5
            over=1






def enter():

    global delaytime,Timer
    global road,castle
    global forest,forests
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT

    state=None
    over=None


    goblincnt=1
    delaytime=10

    forests=[BackGround.Forest() for i in range(2)]
    for i in range(2):
        forests[i].x=600+1200*i
        forests[i].y=450

    goblins=[Character.Goblin() for i in range(100)]
    for i in range(goblincnt):
        goblins[i].x=200
        goblins[i].y=100





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
    global road,castle
    global forest,forests
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT


    events=get_events()
    for event in events:
        if event.type==SDL_QUIT or event.key==SDLK_ESCAPE:
            game_framework.quit()

        if event.type==SDL_KEYDOWN and event.key==SDLK_LEFT:
            state=0

        elif event.type==SDL_KEYDOWN and event.key==SDLK_RIGHT:
            state=1

        if event.type==SDL_KEYUP:
            state=None


        '''
            road.x-=5
            castle.x-=5




            for goblin in goblins[:goblincnt]:
                for i in range(goblincnt):
                    goblins[i].x-=5

            for forest in forests[:goblincnt]:
                for i in range(3):
                    forests[i].x-=5
        '''




        if event.type==SDL_KEYDOWN and event.key==SDLK_1:
            goblincnt+=1



    pass

def update():

    global delaytime,Timer
    global road,castle
    global forest,forests
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT

    delaytime+=1
    if state==0:
        left()

    elif state==1:
        right()

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
    global road,castle
    global forest,forests
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT


    clear_canvas()
    for i in range(2):
        forests[i].draw()
    road.draw()
    castle.draw()
    for goblin in goblins[:goblincnt]:
        goblin.draw()



    Timer.draw()
    update_canvas()
    pass





