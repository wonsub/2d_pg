
from pico2d import *

class Font:
    font=None

    def __init__(self):
        self.x, self.y = None, None
        self.content = None

        if Font.font == None:
            self.font = load_font("ConsolaMalgun.ttf", 20)

    def resize(self, size, font, font_format):
        # self.font = load_font("ConsolaMalgun.ttf", size)
        self.font = load_font("{size}.{font_format}".format(size, font_format))



    def draw(self):

        if type(self.content) != str:
            self.font.draw(self.x, self.y, str(self.content), color=(255, 255, 255))
        else:
            self.font.draw(self.x, self.y, self.content, color=(255, 255, 255))
