
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
import object

global delaytime,Timer
global commandtime
global road,castle,castles,forest,forests

global hero
global goblin,goblins
global goblincnt

global state,over,LEFT,RIGHT





delaytime=None
#숫자를 문자로 : str(숫자)
#문자를 숫자로 : 자료형(문자) ex)int(s)


def enter():
    global delaytime,Timer
    global commandtime
    global road
    global castle,castles
    global forest,forests
    global hero
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT
    global tower,towers

    state=None
    over=None


    goblincnt=1
    delaytime=10
    commandtime=0


    Timer=Letter.Font()
    Timer.contet=180
    Timer.x=650
    Timer.y=800


    hero=Character.Hero()
    hero.x=800
    hero.y=300
    hero.dir=0
    hero.spd=5
    hero.state=0


    goblins=[Character.Goblin() for i in range(100)]
    for i in range(100):
        goblins[i].x=400
        goblins[i].y=280
        goblins[i].spd=8
        goblins[i].dir=0
    #     캐릭


    forests=[BackGround.Forest() for i in range(3)]
    for i in range(3):
        forests[i].x=400+800*i
        forests[i].y=600




    road=BackGround.Road()
    road.x=1200
    road.y=225

    castles=[BackGround.Castle() for i in range(2)]
     # castle=BackGround.Castle()

    for i in range(2):
        castles[i].y=450

    castles[0].x=200
    castles[0].dir=0

    castles[1].x=2150
    castles[1].dir=1
    # castle.y=450


    towers=[object.Tower() for i in range(2)]

    for i in range(2):
        towers[i].y=625

    towers[0].x=550
    towers[0].dir=0

    towers[1].x=1800
    towers[1].dir=1
    # 배경


    pass

name = "MainState"


def left():
    global delaytime,Timer
    global commandtime
    global road
    global castle,castles
    global forest,forests
    global hero
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT
    global tower,towers


    road.x+=hero.spd
    if road.x>=1200:
        road.x-=hero.spd
        over=1


    # castle.x+=hero.spd
    # if castle.x>200:
    #     castle.x-=hero.spd
    #     over=1

    if over!=1:
        for i in range(100):
            goblins[i].x+=hero.spd




    castles[0].x+=hero.spd
    if castles[0].x>=200:
        castles[0].x-=hero.spd
        over=1
    castles[1].x+=hero.spd
    if castles[1].x>=2150:
        castles[1].x-=hero.spd
        over=1


    for i in range(3):
        forests[i].x+=hero.spd
        if forests[i].x>=400+800*i:
            forests[i].x-=hero.spd
            over=1


    towers[0].x+=hero.spd
    if towers[0].x>=550:
        towers[0].x-=hero.spd
        over=1
    towers[1].x+=hero.spd
    if towers[1].x>=1800:
        towers[1].x-=hero.spd
        over=1



def right():
    global delaytime,Timer
    global commandtime
    global road
    global castle,castles
    global forest,forests
    global hero
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT
    global tower,towers


    road.x-=hero.spd
    if road.x<=1200-900:
        road.x+=hero.spd
        over=1



    # castle.x-=hero.spd
    # if castle.x<200-900:
    #     castle.x+=hero.spd
    #     over=1

    if over!=1:
        for i in range(100):
            goblins[i].x-=hero.spd


    castles[0].x-=hero.spd
    if castles[0].x<=200-900:
        castles[0].x+=hero.spd
        over=1
    castles[1].x-=hero.spd
    if castles[1].x<=2150-900:
        castles[1].x+=hero.spd
        over=1


    towers[0].x-=hero.spd
    if towers[0].x<=550-900:
        towers[0].x+=hero.spd
        over=1
    towers[1].x-=hero.spd
    if towers[1].x<=1800-900:
        towers[1].x+=hero.spd
        over=1




    for i in range(3):
        forests[i].x-=hero.spd
        if forests[i].x<=400+800*i-900:
            forests[i].x+=hero.spd
            over=1






def exit():
    close_canvas()
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    global delaytime,Timer
    global commandtime
    global road
    global castle,castles
    global forest,forests
    global hero
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT
    global tower,towers


    events=get_events()
    for event in events:
        if event.type==SDL_QUIT or event.key==SDLK_ESCAPE:
            game_framework.quit()

        if event.type==SDL_KEYDOWN and event.key==SDLK_LEFT:
            state=0

            hero.frame=0
            hero.dir=1
            hero.state=1
            hero.spd=5
            if commandtime>0 and commandtime<2:
                commandtime=0
                hero.state=2
                hero.spd=20

        elif event.type==SDL_KEYDOWN and event.key==SDLK_RIGHT:
            state=1

            hero.frame=0
            hero.dir=0
            hero.state=1
            hero.spd=5

            if commandtime>0 and commandtime<2:
                commandtime=0
                hero.state=2
                hero.spd=20

        if event.type==SDL_KEYUP:
            state=None
            over=None
            if hero.state!=5:
                hero.frame=0
                hero.state=0
                commandtime=0

        if event.type==SDL_KEYDOWN and event.key==SDLK_x:
            hero.state=3
            hero.frame=0
            # commandtime=0
        if event.type==SDL_KEYDOWN and event.key==SDLK_c:
            hero.state=5
            hero.frame=0

        if event.type==SDL_KEYDOWN and event.key==SDLK_SPACE:
            hero.state=4
            hero.frame=0

        if event.type==SDL_KEYDOWN and event.key==SDLK_1:

            goblincnt+=1



            # commandtime=0




    pass

def update():
    global delaytime,Timer
    global commandtime
    global road
    global castle,castles
    global forest,forests
    global hero
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT
    global tower,towers

    delaytime+=1
    delaytime%=10


    if state==0:
        if hero.x>800 or (over==1 and hero.x>300):
            hero.x-=hero.spd
        else:

            left()
    elif state==1:
        if hero.x<800 or (over==1 and hero.x<1150 ):
            hero.x+=hero.spd
        else:
            right()

    for i in range(goblincnt):
        if goblins[i].dir==0:
            goblins[i].x+=goblins[i].spd
        else:
            goblins[i].x-=goblins[i].spd





    if hero.state==0:
        if delaytime%4==0:
            hero.update()
    elif hero.state==1:
        if delaytime%2==0:
            hero.update()
    elif hero.state==2:
        if delaytime%2==0:
            hero.update()
    elif hero.state==3:
        if delaytime%1==0:
            if hero.frame==4:
                hero.state=0
            hero.update()
    elif hero.state==4:
            hero.update()
    elif hero.state==5:
        if delaytime%2==0:
            hero.update()





    if(delaytime%10==9): #1초마다 작동할수 있게 변경

        if(Timer.contet>0):
            Timer.contet-=1
        if(Timer.contet==0):
            game_framework.quit()



    for goblin in goblins[:goblincnt]:
        goblin.update()



    commandtime+=1
    commandtime%=5
    delay(0.1)


    pass


def draw():
    global delaytime,Timer
    global commandtime
    global road
    global castle,castles
    global forest,forests
    global hero
    global goblin,goblins
    global goblincnt
    global state,over,LEFT,RIGHT
    global tower,towers


    clear_canvas()
    for i in range(3):
        forests[i].draw()
    road.draw()

    for tower in towers[:2]:
        tower.draw()


    for castle in castles[:2]:
        castle.draw()
    # castle.draw()

    for goblin in goblins[:goblincnt]:
        goblin.draw()
    hero.draw()


    Timer.draw()
    update_canvas()
    pass





