import game_framework
import main_state
from pico2d import *

name = "TitleState"
main_image = None
press_image=None
title_image=None


ct=0.0


def enter():
    global main_image,press_image,title_image
    main_image=load_image('concept.png')
    press_image=load_image('press_key.png')
    title_image=load_image('title_logo.png')

    pass


def exit():
    global main_image,press_image,title_image
    del(main_image)
    del(press_image)
    del(title_image)

    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if event.type==SDL_KEYDOWN:
                game_framework.change_state(main_state)
            '''
            if (event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state)
                '''



    pass


def draw():
    global ct
    clear_canvas()
    main_image.clip_draw(0, 0, 1600, 900, 800,450)
    title_image.clip_draw(0,0,1300,600,900,500)
    if(ct<0.5):
        press_image.draw(800,150)

    update_canvas()

    pass


def update():
    global ct
    if (ct > 1.0):
        ct = 0

    delay(0.01)
    ct += 0.01
    pass


def pause():
    pass


def resume():
    pass






