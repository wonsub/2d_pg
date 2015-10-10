from pico2d import*

open_canvas()
title=load_image('title.png')
loading=load_image('loading.png')

clear_canvas()

#title.draw(400,300)
title.clip_draw(0,0,800,600,400,300)
#loading.clip_draw(0,0,400,100,400,300)


#loading.draw(300,200)
update_canvas()
delay(5.5)
close_canvas()

