import random
import scroll_state

from pico2d import *

class FreeHero:

    # PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    # RUN_SPEED_KMPH = 80.0                    # Km / Hour
    PIXEL_PER_METER = (10.0 / 0.5)
    RUN_SPEED_KMPH = 40.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_STAND, RIGHT_STAND, LEFT_WALK, RIGHT_WALK,\
    LEFT_RUN, RIGHT_RUN, LEFT_THRUST, RIGHT_THRUST,\
    LEFT_UPPER_SLASH, RIGHT_UPPER_SLASH= 0, 1, 2, 3, 4, 5, 6, 7, 8, 9



    def __init__(self):
        self.x, self.y = 1700, 200
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.run = 0
        self.attack = 0
        self.skill=0


        self.state = self.RIGHT_STAND
        if FreeHero.image == None:
            FreeHero.walk_image = load_image('saber\\walk\\walk_sprite.png')
            FreeHero.stand_image = load_image('saber\\stand\\stand_sprite.png')
            FreeHero.run_image = load_image('saber\\run\\run_sprite.png')
            FreeHero.thrust_image = load_image('saber\\thrust\\thrust_sprite.png')
            FreeHero.upper_slash_image = load_image('saber\\upper_slash\\upper_slash_sprite.png')

            # FreeBoy.image = load_image('animation_sheet.png')


    def set_background(self, bg):
        self.bg = bg


    def update(self, frame_time):

        if self.xdir == -1:
            self.state = self.LEFT_WALK
            if self.run == 1:
                self.state = self.LEFT_RUN
                if self.attack == 1:
                    self.state = self.LEFT_THRUST
            if self.skill==2:
                self.state=self.LEFT_UPPER_SLASH


        elif self.xdir == 1:
            self.state = self.RIGHT_WALK
            if self.run == 1:
                self.state = self.RIGHT_RUN
                if self.attack == 1:
                    self.state = self.RIGHT_THRUST
            if self.skill==2:
                self.state=self.RIGHT_UPPER_SLASH
        elif self.xdir == 0:
            if self.state in (self.RIGHT_WALK, self.RIGHT_RUN): self.state = self.RIGHT_STAND
            elif self.state in (self.LEFT_WALK, self. LEFT_RUN): self.state = self.LEFT_STAND
            elif self.state == self.LEFT_STAND:
                if self.skill==2: self.state=self.LEFT_UPPER_SLASH
            elif self.state == self.RIGHT_STAND:
                if self.skill==2: self.state=self.RIGHT_UPPER_SLASH
            elif self.skill==0:
                if self.state==self.LEFT_UPPER_SLASH:
                    self.state=self.LEFT_STAND
                elif self.state==self.RIGHT_UPPER_SLASH:
                    self.state=self.RIGHT_STAND


        self.life_time += frame_time
        distance = FreeHero.RUN_SPEED_PPS * frame_time
        self.total_frames +=\
            FreeHero.FRAMES_PER_ACTION * FreeHero.ACTION_PER_TIME * frame_time

        if self.state in (self.LEFT_STAND, self.RIGHT_STAND):
            self.frame = int(self.total_frames) % 2
        elif self.state in (self.LEFT_WALK, self.RIGHT_WALK):
            self.frame = int(self.total_frames) % 5
        elif self.state in (self.LEFT_RUN, self.RIGHT_RUN):
            self.frame = int(self.total_frames) % 8
        elif self.state in (self.LEFT_THRUST, self.RIGHT_THRUST):
            self.frame = int(self.total_frames) % 7

            # 해제
            if self.frame == 6:
                self.attack = 0
                self.run = 0


        elif self.state in (self.LEFT_UPPER_SLASH, self.RIGHT_UPPER_SLASH):
            self.frame = int(self.total_frames) % 7

            # 해제
            if self.frame == 6:
                self.attack = 0
                self.run = 0
                self.skill=0


        self.x += (self.xdir *distance)
        # 추가적인 이동
        if self.run == 1:
            self.x += (self.xdir *distance)



        if self.x < 50:
            self.x = max(50, self.x)
        elif self.x > scroll_state.background.image.w-50:
            self.x = min(self.x, scroll_state.background.image.w-50)

        self.y += (self.ydir *distance)

        if self.y < 185:
            self.y = max(185, self.y)
        elif self.y > 315:
            self.y = min(self.y, 315)


        # print(self.x)

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        # self.image.clip_draw(self.frame *100, self.state * 100, 100, 100, sx, sy)
        if self.state in (self.LEFT_STAND, self.RIGHT_STAND):
            self.stand_image.clip_draw(self.frame * 550, self.state % 2 * 430, 550, 430, sx, sy, 215, 275)

        elif self.state in (self.LEFT_WALK, self.RIGHT_WALK):
            self.walk_image.clip_draw(self.frame * 550, self.state % 2 * 430, 550, 430, sx, sy, 215, 275)

        elif self.state in (self.LEFT_RUN, self.RIGHT_RUN):
            self.run_image.clip_draw(self.frame * 550, self.state % 2 * 430, 550, 430, sx, sy, 215, 275)
        elif self.state in (self.LEFT_THRUST, self.RIGHT_THRUST):
            self.thrust_image.clip_draw(self.frame * 550, self.state % 2 * 430, 550, 430, sx, sy, 215, 275)

        elif self.state in (self.LEFT_UPPER_SLASH, self.RIGHT_UPPER_SLASH):
            self.upper_slash_image.clip_draw(self.frame * 550, self.state % 2 * 430, 550, 430, sx, sy, 215, 275)



        debug_print('x=%d, y=%d, sx=%d, sy=%d' % (self.x, self.y, sx, sy))

        # fill here
        pass




    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:

            if event.key == SDLK_LEFT: self.xdir += -1
            elif event.key == SDLK_RIGHT: self.xdir += 1
            elif event.key == SDLK_UP: self.ydir += 1
            elif event.key == SDLK_DOWN: self.ydir -= 1
            elif event.key == SDLK_v: self.run = 1
            elif event.key == SDLK_x:
                self.attack =1
                # 일단 임시로 변경
                self.total_frames = 0
            elif event.key == SDLK_s:
                self.skill = 2
                self.total_frames = 0


        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.xdir += 1
            elif event.key == SDLK_RIGHT: self.xdir += -1
            elif event.key == SDLK_UP: self.ydir -= 1
            elif event.key == SDLK_DOWN: self.ydir += 1
            elif event.key == SDLK_v: self.run = 0
            elif event.key == SDLK_x: self.attack = 0
            elif event.key == SDLK_s: self.skill = 0

