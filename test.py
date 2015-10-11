#__author__ = 'wonsub'

from pico2d import *
#from math import *

class a:
    def __init__(self):
        self.x,self.y=10,10
    def func(self):
        self.x+=100
        self.y+=100
class b:
    def __init__(self):
        a.__init__(self)
        self.x,self.y=0,0
    def fun(self):
        a.fun(self)
        self.x=a.x+100
        self.y=a.y+100

A=a()
B=b()

open_canvas()

image=load_image('stone.png')

image.draw(B.x,B.y)
#image.draw(a().x,a().y)
update_canvas()
delay(1.0)
close_canvas()





