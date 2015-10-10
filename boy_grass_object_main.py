from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('castle.png')

    def draw(self):
        self.image.draw(240, 200)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 45
        self.frame = 0
        self.image = load_image('swordman.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 19
        self.x += self.dir
        delay(0.05)

    def draw(self):
        self.image.clip_draw(self.frame * 380, 0, 380, 120, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# fill here for boy, grass
boy=None
grass=None
runnig=True

running = True

def enter():
    global boy,grass
    open_canvas()
    boy=Boy()
    grass=Grass()
    pass


def exit():
    global boy,grass
    del(boy)
    del(grass)
    close_canvas()
    pass


def update():
    boy.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass


def main():
    enter()
    while running:
        handle_events()
        update()
        draw()
    exit()
    pass



if __name__=='__main__':
    main()
# fill here


