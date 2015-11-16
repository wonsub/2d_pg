import game_framework
import title_state
import Image_Format
import json
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1400,700)
    image = load_image('game_image\\loading\\kpu_credit.png')
    pass


def exit():
    global image
    del(image)
    close_canvas()
    pass


def update():
    global logo_time

    if (logo_time > 2.0):
        logo_time = 0
       # game_framework.quit()
        game_framework.push_state(title_state)
    logo_time += 0.01
    pass


def draw():
    global  image

    start_data_file=open('Json\\start_data.txt','r')
    start_data=json.load(start_data_file)
    start_data_file.close()

    clear_canvas()

    kpu_credit = Image_Format.Attribute()
    kpu_credit.Image_Start_X = start_data['KPU_Credit']['Image_Start_X']
    kpu_credit.Image_Start_Y = start_data['KPU_Credit']['Image_Start_Y']
    kpu_credit.Image_Width = start_data['KPU_Credit']['Image_Width']
    kpu_credit.Image_Height = start_data['KPU_Credit']['Image_Height']
    kpu_credit.Draw_Center_X = start_data['KPU_Credit']['Draw_Center_X']
    kpu_credit.Draw_Center_Y = start_data['KPU_Credit']['Draw_Center_Y']
    kpu_credit.Draw_Width = start_data['KPU_Credit']['Draw_Width']
    kpu_credit.Draw_Height = start_data['KPU_Credit']['Draw_Height']

    image.clip_draw(
        kpu_credit.Image_Start_X, kpu_credit.Image_Start_Y,  kpu_credit.Image_Width, kpu_credit.Image_Height,
        kpu_credit.Draw_Center_X, kpu_credit.Draw_Center_Y, kpu_credit.Draw_Width, kpu_credit.Draw_Height)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




