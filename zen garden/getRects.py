from pygame import *
screen=display.set_mode((800,600))
bg_day=image.load("zen copy.png")
top=image.load("top8.png")
screen.blit(bg_day,(0,0))
screen.blit(top,(0,0))
##seedcart=image.load("graphics/seedcart.png")
##screen.blit(seedcart,(9,1))
pts=[]
running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            pts+=[evt.pos]
    display.flip()
fout=open("rects.txt","w")
try:
    for i in range (0,len(pts),2):
        x,y,w,h=pts[i][0],pts[i][1],pts[i+1][0]-pts[i][0],pts[i+1][1]-pts[i][1]
        fout.write("Rect(%d,%d,%d,%d),"%(x,y,w,h))
except:
    fout.write("CRASH")
fout.close()
quit()
