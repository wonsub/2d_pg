from pico2d import *
open_canvas()
#rass=load_image('grass.png')
goblin=load_image('dash.png')

x=90
frame=0
while(x<800):
 clear_canvas()
 #grass.draw(400,30)
 goblin.clip_draw(frame*185,0,185,120,x+40,80)
 update_canvas()
 frame=(frame+1)%8
# if frame==0:
  # x+=10
 delay(0.25)
 get_events()

close_canvas()