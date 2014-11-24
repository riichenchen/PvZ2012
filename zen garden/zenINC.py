#zenINC.py
from zenGraphics import *
from zenRects import *
from pygame import *
from random import *
from datetime import datetime
from time import clock
init()
username="paula"

class zPlant:
    "Plant class for representing, manipulating, and drawing plants"
    def __init__(self,kind,x,y,state,age,asn,date,time,water):
        self.type=kind
        self.row=x
        self.col=y
        self.state=state  #0-happy,1-thirsty,2-fertilizer,3-spray,4-music,5-none
        self.age=age
        self.date=date
        self.slide=asn
        self.passed=time
        self.water=water
    def __str__(self):
        now=self.date
        date="datetime(%d,%d,%d,%d,%d,%d,%d)"%(now.year,now.month,now.day,\
                                now.hour,now.minute,now.second,now.microsecond)
        return "zPlant(%d,%d,%d,%d,%d,%d,"%(self.type,self.row,self.col,\
                self.state,self.age,self.slide)+date+",clock(),%d)"%self.water
    def draw(self):
        
        potRect=garden[self.row][self.col]
        if self.state==4:
            screen.blit(states[4],(potRect[0]-20,potRect[1]-10))
        screen.blit(pot,garden[self.row][self.col])
        plantimg=plant[self.type][self.slide/20]
        ndx,ndy=plantimg.get_width()*(self.age+1)/4,plantimg.get_height()*(self.age+1)/4
        plantimg=transform.scale(plantimg,(ndx,ndy))
        plantRect=getDrawRect(plantimg,garden[self.row][self.col])
        screen.blit(plantimg,plantRect)
        if self.state!=4 and self.state!=5:
            screen.blit(states[self.state],(plantRect[0]+plantRect[2]-25,\
                                            plantRect[1]-27))
        self.slide+=1
        if self.slide>len(plant[self.type])*20-1:
            self.slide=0
class Coin:
    def __init__(self,kind,currY,destX,destY,asn,time):
        self.type=kind
        self.cy=currY
        self.dx=destX
        self.dy=destY
        self.slide=asn
        self.time=time
    def __str__(self):
        return "%d coin landing at (%d,%d)"%(self.type,self.dx,self.dy)
    def draw(self):
        screen.blit(coins[self.type],(self.dx-25,int(self.cy)-25))
        if self.cy<self.dy:
            self.cy=self.cy+1
        



def getDrawRect(img,potRect):
    x,y=img.get_width(),img.get_height()
    return Rect(potRect[0]+38-x/2,potRect[1]+28-y,x,y)

bg=image.load("zen copy.png")
def zenGarden(bg):
    data=map(eval,open(username+".txt").read().strip().split("\n"))
    topNum,topTypes,money,numPlants=data[:4]
    zplants=data[4:]
    myTopRects=topRects[:topNum]

    global running
    screen.blit(bg,(0,0))
    screen.blit(top[topNum-1],(0,0))
    
    allcoins=[]
    tool="none"

    out="none"
    while out!="quit":
        copy=screen.copy().convert()
        lclick=False
        lcx,lcy=999,999
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                out="quit"
            if evt.type==MOUSEBUTTONDOWN:
                lclick=True
                lcx,lcy=evt.pos
        mx,my=mouse.get_pos()
        
        for num in range (topNum):
            if tool!=num:
                screen.blit(stuff[topTypes[num]],myTopRects[num])
    
        plantRects=[]
        for p in zplants:
            p.draw()
            pic=plant[p.type][p.slide/20]
            rect=garden[p.row][p.col]
            plantRects.append(getDrawRect(pic,rect))
            

        for i in range (len(zplants)):
            r=plantRects[i]
            if r.collidepoint(lcx,lcy) and tool==zplants[i].state==0:
                tool="none"
                zplants[i].state=5
                zplants[i].water+=1
                zplants[i].passed=clock()
                allcoins.append(Coin(0,r[1]-10,\
                                  randint(r[0]-10,r[0]+r[2]+10),\
                                  r[1]+r[-2]+10,0,clock()))
            elif r.collidepoint(lcx,lcy) and tool==zplants[i].state==1:
                tool="none"
                zplants[i].state=5
                zplants[i].age+=1
                zplants[i].passed=clock()
                for c in range (zplants[i].age):
                    allcoins.append(Coin(1,r[1]-10,\
                                      randint(r[0]-10,r[0]+r[2]+10),\
                                      r[1]+r[-2]+10,0,clock()))
                    
            elif r.collidepoint(lcx,lcy) and tool==zplants[i].state:
                zplants[i].state=4
                tool="none"
                allcoins.append(Coin(1,r[1]-10,\
                                  randint(r[0]-10,r[0]+r[2]+10),\
                                  r[1]+r[-2]+10,0,clock()))
                
            if clock()-zplants[i].passed>24 and zplants[i].state==4:
                allcoins.append(Coin(choice([0,0,0,0,0,0,0,1,1,1,2]),r[1]-10,\
                                  randint(r[0]-10,r[0]+r[2]+10),\
                                  r[1]+r[-2]+10,0,clock()))
                zplants[i].passed=clock()

            if zplants[i].state==5:
                if clock()-zplants[i].passed>5:
                    if zplants[i].water<3:
                        zplants[i].state=0
                    elif zplants[i].age<3:
                        zplants[i].state=1
                    elif zplants[i].age>=3:
                        zplants[i].state=randint(2,3)

        for c in allcoins:
            c.draw()
            if Rect(c.dx-20,c.cy-20,40,40).collidepoint(lcx,lcy):
                money+=coinVals[c.type]
                c.time="x"

        if lclick:
            tool="none"
        for r in range(topNum):
            if myTopRects[r].collidepoint(lcx,lcy):
                tool=topTypes[r]
                
        if mainRect.collidepoint(lcx,lcy):
            out="menu"
        if shopRect.collidepoint(lcx,lcy):
            out="shop"
        if nextRect.collidepoint(lcx,lcy):
            out="quit"

        if tool!="none":
            screen.blit(zcursors[topTypes[tool]],(mx-35,my-35))
            
        display.flip()
        screen.blit(copy,(0,0))
        allcoins=filter(lambda x:x.time!="x" and clock()-x.time<8,allcoins)

        
    outf=open(username+".txt","w")
    outf.write("%d\n"%topNum+str(topTypes)+"\n%d\n%d\n"%(money,len(zplants))+\
               "\n".join(map(str,zplants)))
    outf.close()
    return out

quit()

            
