#zombie test.py
from pygame import *
from random import *
screen=display.set_mode((800,600))
paused=[image.load("paused%d.png"%i) for i in range (1,13)]

running=True 
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        for i in range(1,13):
            screen.blit(paused[i])
display.flip()
quit()
    
