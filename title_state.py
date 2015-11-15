import game_framework
import main_state
import Image_Format
import json


from pico2d import *

name = "TitleState"
BackGround = None
Press_Key = None
Title_Logo = None

count=0
# class Image():
#     Image_Start_x,Image_Start_Y=None,None
#     Image_Width,Image_Height=None,None
#     Draw_Center_X,Draw_Center_Y=None,None
#     Draw_Width,Draw_Height=None,None




def enter():
    global BackGround, Press_Key, Title_Logo
    global title_data
    BackGround = load_image('game_image\\loading\\concept.png')
    Press_Key = load_image('game_image\\loading\\Press_Key.png')
    Title_Logo = load_image('game_image\\loading\\title_logo.png')

    title_data_file = open('title_data.txt', 'r')
    title_data = json.load(title_data_file)
    title_data_file.close()
    pass


def exit():
    global BackGround, Press_Key, Title_Logo
    del(BackGround)
    del(Press_Key)
    del(Title_Logo)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN:
                game_framework.change_state(main_state)
    pass


def draw():
    global title_data
    clear_canvas()

    background=Image_Format.Attribute()
    background.Image_Start_X=title_data['BackGronud']['Image_Start_X']
    background.Image_Start_Y=title_data['BackGronud']['Image_Start_Y']
    background.Image_Width=title_data['BackGronud']['Image_Width']
    background.Image_Height=title_data['BackGronud']['Image_Height']
    background.Draw_Center_X=title_data['BackGronud']['Draw_Center_X']
    background.Draw_Center_Y=title_data['BackGronud']['Draw_Center_Y']
    background.Draw_Width=title_data['BackGronud']['Draw_Width']
    background.Draw_Height=title_data['BackGronud']['Draw_Height']

    press_key=Image_Format.Attribute()
    press_key.Image_Start_X=title_data['Press_Key']['Image_Start_X']
    press_key.Image_Start_Y=title_data['Press_Key']['Image_Start_Y']
    press_key.Image_Width=title_data['Press_Key']['Image_Width']
    press_key.Image_Height=title_data['Press_Key']['Image_Height']
    press_key.Draw_Center_X=title_data['Press_Key']['Draw_Center_X']
    press_key.Draw_Center_Y=title_data['Press_Key']['Draw_Center_Y']
    press_key.Draw_Width=title_data['Press_Key']['Draw_Width']
    press_key.Draw_Height=title_data['Press_Key']['Draw_Height']

    title_logo=Image_Format.Attribute()
    title_logo.Image_Start_X=title_data['Title_Logo']['Image_Start_X']
    title_logo.Image_Start_Y=title_data['Title_Logo']['Image_Start_Y']
    title_logo.Image_Width=title_data['Title_Logo']['Image_Width']
    title_logo.Image_Height=title_data['Title_Logo']['Image_Height']
    title_logo.Draw_Center_X=title_data['Title_Logo']['Draw_Center_X']
    title_logo.Draw_Center_Y=title_data['Title_Logo']['Draw_Center_Y']
    title_logo.Draw_Width=title_data['Title_Logo']['Draw_Width']
    title_logo.Draw_Height=title_data['Title_Logo']['Draw_Height']



    BackGround.clip_draw(background.Image_Start_X, background.Image_Start_Y,  background.Image_Width,  background.Image_Height,
                         background.Draw_Center_X, background.Draw_Center_Y, background.Draw_Width, background.Draw_Height)

    if count < 5:
        Press_Key.clip_draw(press_key.Image_Start_X, press_key.Image_Start_Y,  press_key.Image_Width,  press_key.Image_Height,
                         press_key.Draw_Center_X, press_key.Draw_Center_Y, press_key.Draw_Width, press_key.Draw_Height)

    Title_Logo.clip_draw(title_logo.Image_Start_X, title_logo.Image_Start_Y,  title_logo.Image_Width,  title_logo.Image_Height,
                         title_logo.Draw_Center_X, title_logo.Draw_Center_Y, title_logo.Draw_Width, title_logo.Draw_Height)

    update_canvas()

    pass


def update():
    global count
    count += 1
    count %= 10
    enter()
    draw()
    pass


def pause():
    pass


def resume():
    pass






