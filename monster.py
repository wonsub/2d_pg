from pico2d import *
open_canvas()
#rass=load_image('grass.png')
goblin=load_image('goblin.png')

x=90
frame=0
while(x<800):
 clear_canvas()
 #grass.draw(400,30)
 goblin.clip_draw(frame*90,0,100,100,x,50)
 update_canvas()
 frame=(frame+1)%5
# if frame==0:
  # x+=10
 delay(0.25)
 get_events()

close_canvas()