
from pico2d import *

Guage_data_file = open('Json\\Guage_data.txt','r')
Guage_data = json.load(Guage_data_file)
Guage_data_file.close()


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


class Gauge():
    now, max = None, None
    mark = None
    rate=None


def enter():
    global HP, MP, EXP

    HP = Gauge()
    MP = Gauge()
    EXP = Gauge()

    HP.now = Guage_data['HP']['now']
    HP.max = Guage_data['HP']['max']
    HP.rate = HP.now/HP.max
    HP.mark = Font()

    MP.now = 10
    MP.max = 20
    MP.mark = Font()

    EXP.now = 0
    EXP.max = 1000
    EXP.mark = Font()

    HP.mark.x, HP.mark.y, HP.mark.content = 650, 80, "{NOW:<5}/{MAX:>5}".format(NOW=HP.now, MAX=HP.max)
    MP.mark.x, MP.mark.y, MP.mark.content = 650, 60, "{NOW:<5}/{MAX:>5}".format(NOW=MP.now, MAX=MP.max)
    EXP.mark.x, EXP.mark.y, EXP.mark.content = 650, 30, "{NOW:<5}/{MAX:>5}".format(NOW=EXP.now, MAX=EXP.max)


# def update():

    # Letter_data_file = open('Json\\Letter_data.txt','r')
    # Letter_data = json.load(Letter_data_file)
    # Letter_data_file.close()



def draw():

    HP.mark.draw()
    MP.mark.draw()
    EXP.mark.draw()

