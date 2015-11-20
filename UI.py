__author__ = 'wonsub'
import game_framework
import Image_Format
import json
import Letter

from pico2d import *

UI_data_file = open('Json\\UI_data.txt','r')
UI_data = json.load(UI_data_file)
UI_data_file.close()


Guage_data_file = open('Json\\Guage_data.txt','r')
Guage_data = json.load(Guage_data_file)
Guage_data_file.close()

global HP, MP, EXP

HP, MP, EXP = Letter.Gauge(), Letter.Gauge(), Letter.Gauge()




class Main_Image():

    def __init__(self):
        self.image = load_image('game_image\\UI\\Main_img.png')


    def draw(self):

        # UI_data_file = open('Json\\UI_data.txt','r')
        # UI_data = json.load(UI_data_file)
        # UI_data_file.close()

        main_image = Image_Format.Attribute()
        main_image.Image_Start_X = UI_data['Main_Image']['Image_Start_X']
        main_image.Image_Start_Y = UI_data['Main_Image']['Image_Start_Y']
        main_image.Image_Width = UI_data['Main_Image']['Image_Width']
        main_image.Image_Height = UI_data['Main_Image']['Image_Height']
        main_image.Draw_Center_X = UI_data['Main_Image']['Draw_Center_X']
        main_image.Draw_Center_Y = UI_data['Main_Image']['Draw_Center_Y']
        main_image.Draw_Width = UI_data['Main_Image']['Draw_Width']
        main_image.Draw_Height = UI_data['Main_Image']['Draw_Height']

        self.image.clip_draw(
            main_image.Image_Start_X, main_image.Image_Start_Y,  main_image.Image_Width, main_image.Image_Height,
            main_image.Draw_Center_X, main_image.Draw_Center_Y, main_image.Draw_Width, main_image.Draw_Height)

class Board():
    def __init__(self):
        self.image = load_image('game_image\\UI\\Board.png')

    def draw(self):

        # UI_data_file = open('Json\\UI_data.txt','r')
        # UI_data = json.load(UI_data_file)
        # UI_data_file.close()

        board = Image_Format.Attribute()
        board.Image_Start_X = UI_data['Board']['Image_Start_X']
        board.Image_Start_Y = UI_data['Board']['Image_Start_Y']
        board.Image_Width = UI_data['Board']['Image_Width']
        board.Image_Height = UI_data['Board']['Image_Height']
        board.Draw_Center_X = UI_data['Board']['Draw_Center_X']
        board.Draw_Center_Y = UI_data['Board']['Draw_Center_Y']
        board.Draw_Width = UI_data['Board']['Draw_Width']
        board.Draw_Height = UI_data['Board']['Draw_Height']

        self.image.clip_draw(
            board.Image_Start_X, board.Image_Start_Y,  board.Image_Width, board.Image_Height,
            board.Draw_Center_X, board.Draw_Center_Y, board.Draw_Width, board.Draw_Height)

class Mark_Gauage():
    global HP

    def __init__(self):
        self.hp_bar = load_image('game_image\\UI\\HP_Bar.png')
        self.mp_bar = load_image('game_image\\UI\\MP_Bar.png')
        self.exp_bar = load_image('game_image\\UI\\EXP_Bar.png')


    def draw(self):

         self.hp_bar.clip_draw_to_origin(0,0,100,100,500,70,400*Guage_data["HP"]["now"]/Guage_data["HP"]['max'],20)
         self.mp_bar.clip_draw_to_origin(0,0,100,100,500,50,400,20)
         self.exp_bar.clip_draw_to_origin(0,0,100,100,500,20,400,20)



def draw():
    global main, board,Mark_gauage
    main = Main_Image()
    board = Board()
    Mark_gauage=Mark_Gauage()



    board.draw()
    main.draw()
    Mark_gauage.draw()


