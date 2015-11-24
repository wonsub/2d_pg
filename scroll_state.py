from pico2d import *

import game_framework


from hero import FreeHero as Hero # import Boy class from boy.py
from background import FixedBackground as Background



name = "scroll_state"

hero = None
background = None
bgm = None

def create_world():
    global hero, background, bgm
    hero = Hero()
    background = Background()

    bgm = load_music('bgm.ogg')
    bgm.set_volume(32)
    bgm.repeat_play()

    background.set_center_object(hero)
    hero.set_background(background)

    # fill here


def destroy_world():
    global hero, background, bgm
    del(bgm)
    del(hero)
    del(background)



def enter():
    open_canvas(800, 600)
    # hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                hero.handle_event(event)
                background.handle_event(event)



def update(frame_time):
    hero.update(frame_time)
    background.update(frame_time)



def draw(frame_time):
    clear_canvas()
    background.draw()
    hero.draw()
    update_canvas()






