import game_framework
import main_state
from pico2d import *

name = "TitleState"
image = None
image2=None

ct=0.0


def enter():
    global image,image2
    image=load_image('title.png')
    image2=load_image('title2.png')


    pass


def exit():
    global image,image2
    del(image)
    del(image2)
    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
               # main_state.data()
                game_framework.change_state(main_state)
               # game_framework.pop_state()


    pass


def draw():
    global ct
    clear_canvas()
    if(ct<0.25):
        image.draw(400,300)
    else:
        image2.draw(400,300)
    update_canvas()

    pass


def update():
    global ct
    if (ct > 0.5):
        ct = 0

    delay(0.01)
    ct += 0.01
    pass


def pause():
    pass


def resume():
    pass






