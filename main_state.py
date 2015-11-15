
import random
import json
import os
import math
from pico2d import *
from math import *

import game_framework
import Letter
import UI



delaytime = None
#숫자를 문자로 : str(숫자)
#문자를 숫자로 : 자료형(문자) ex)int(s)

global image

def enter():
    global image
    # image = UI()
    # image = UI.Main_Image()


    pass

name = "MainState"


def exit():
    close_canvas()
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()

    pass

def update():
    pass


def draw():
    global image
    clear_canvas()
    UI.draw()




    update_canvas()
    pass







