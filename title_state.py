import game_framework
import main_state

from pico2d import *

name = "TitleState"
main = None
press=None
title=None


ct=0.0


def enter():
    global main,press,title
    main=load_image('game_image\\guide\\concept.png')
    press=load_image('game_image\\guide\\press_key.png')
    title=load_image('game_image\\guide\\title_logo.png')

    pass


def exit():
    global main,press,title
    del(main)
    del(press)
    del(title)



    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if event.type==SDL_KEYDOWN:
                game_framework.change_state(main_state)
    pass


def draw():
    global  image,ct
    clear_canvas()

    main.clip_draw(0,0,500,200,800,450,1600,900)
    if ct%2==0:
        press.clip_draw(0,0,800,600,800,200,800,600)
    title.clip_draw(0,0,800,600,900,600,1000,800)
    update_canvas()

    pass


def update():
    global ct
    ct+=1
    enter()
    draw()
    delay(0.5)
    # exit()
    pass


def pause():
    pass


def resume():
    pass






