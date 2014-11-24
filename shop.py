from pygame import *
init()
screen=display.set_mode((800,600))

from shopStuff import *
from datetime import datetime

def printDate(now):
    return "datetime(%d,%d,%d,%d,%d,%d,%d)"%(now.year,now.month,now.day,\
                                now.hour,now.minute,now.second,now.microsecond)
    
username="chen"

def checkdate(date):
    "Check if a day has passed since date"
    now=datetime.now()
    return (now-date).days>0

def changeSold(alreadybought,numfert,numspray,sprouts):
    soldout=[False]*8
    for i in alreadybought:
        soldout[i]=True
    if numfert>15:
        soldout[4]=True
    if numspray>15:
        soldout[5]=True
    for i in range (4):
        if checkdate(sprouts[i])==False:
            soldout[i]=True
    return soldout
        
def shop():
    global money
    out="none"
    data=map(eval,open(username+"Shop.txt").read().split("\n"))
    numfert,numspray,alreadybought=data[:3]
    sprouts=data[3:]
    screen.blit(bgShop,(0,0))
    soldout=changeSold(alreadybought,numfert,numspray,sprouts)
   
    while out=="none":
        copy=screen.copy().convert_alpha()
        lclick=False
        lcx,lcy=999,999
        for evt in event.get():
            if evt.type==QUIT:
                out="quit"
            if evt.type==MOUSEBUTTONDOWN:
                lclick=True
                lcx,lcy=evt.pos
        if sMainRect.collidepoint(lcx,lcy):
            out="menu"
        mx,my=mouse.get_pos()
        for i in range (8):
            if soldout[i]:
                screen.blit(soldoutSpr,itemRects[i])
                
        for item in range (8):
            if itemRects[item].collidepoint(mx,my):
                draw.rect(screen,(14,213,43),itemRects[item],2)
            if itemRects[item].collidepoint(lcx,lcy) and soldout[item]==False:
                if money>costs[item]:
                    if item==5:
                        numfert+=5
                    elif item==6:
                        numspray+=5
                    elif item in range(0,4):
                        sprouts[item]=datetime.now()
                    else:
                        alreadybought.append(item)
                    money-=costs[item]
                    soldout=changeSold(alreadybought,numfert,numspray,sprouts)
        display.flip()
        screen.blit(copy,(0,0))

    outf=open(username+"Shop.txt","w")
    outf.write("%d\n%d\n%s\n"%(numfert,numspray,str(alreadybought)))
    outf.write("\n".join(map(printDate,sprouts)))
    outf.close()
    return out
pg="shop"
while pg!="quit":
    pg=shop()
quit()
                    
