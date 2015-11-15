
from pico2d import *
class Font:
    font=None
    def __init__(self):
        self.x, self.y = None, None
        self.contet = None
        if Font.font == None:
            self.font = load_font("Fonts\\arial.ttf", 100)
    def draw(self):
        self.font.draw(self.x, self.y, str(self.contet), color=(255, 255, 255))



