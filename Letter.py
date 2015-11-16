
from pico2d import *

global maxhp,nowhp
global test

class Font:
    font=None

    def __init__(self):
        self.x, self.y = None, None
        self.content = None

        if Font.font == None:
            self.font = load_font("Fonts\\arial.ttf", 20)

    def draw(self):

        if type(self.content) != str:
            self.font.draw(self.x, self.y, str(self.content), color=(255, 255, 255))
        else:
            self.font.draw(self.x, self.y, self.content, color=(255, 255, 255))


class HP_MP():
    now,max=None,None




def enter():
    global HP, MP
    global test

    test=Font()

    HP=MP=HP_MP()

    HP.now=50
    HP.max=100


    test.x, test.y, test.content = 625, 125, "{NOW:<10}/{MAX:>10}".format(NOW=HP.now, MAX=HP.max)


def update():
    Letter_data_file = open('Json\\Letter_data.txt','r')
    Letter_data = json.load(Letter_data_file)
    Letter_data_file.close()



def draw():
    global test

    test.draw()
