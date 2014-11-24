from pygame import *
loading=image.load("graphics\loading.PNG")
display.init()
screen=display.set_mode((800,600))
display.set_icon(image.load("icon.png"))
screen.blit(loading,(0,0))
display.flip()
loaded=image.load("graphics\loaded.PNG")
from rects import *
from animation import *
from graphics import *
from zenGraphics import *
from zenRects import *
from random import *
from datetime import datetime
from time import clock
from attributes import *
from shopStuff import *
import os

running=True
myClock=time.Clock()
username="chen"
screen.blit(loaded,(0,0))
while running:
    for evt in event.get():
        if evt.type==QUIT:
            quit()
        if evt.type==MOUSEBUTTONDOWN:
            if Rect(245,520,303,54).collidepoint(evt.pos):
                running=False
    display.flip()
    
#----General Functions--------------------
def qa():
    global comicFont
    del comicFont
    quit()
def printDate(now):
    return "datetime(%d,%d,%d,%d,%d,%d,%d)"%(now.year,now.month,now.day,\
                                now.hour,now.minute,now.second,now.microsecond)
def checkdate(date):
    "Check if a day has passed since date"
    now=datetime.now()
    return (now-date).days>0

#----Classes for use in multiple modes----------------
class Coin:
    "Coin class for representing and drawing coins"
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
class Plant:
    def __init__(self,kind,x,y,speed,health,damage,asn,time):
        self.type=kind
        self.row=x
        self.col=y
        self.speed=speed
        self.health=health
        self.dmg=damage
        self.slide=asn
        self.passed=time
    def __str__(self):
        return "%d plant at (%d,%d)"%(self.type,self.row,self.col)
    def draw(self):
        screen.blit(plant[self.type][self.slide/20],\
                    (40+self.col*80,90+self.row*100))
        self.slide+=1
        if self.slide>len(plant[self.type])*10-1:
            self.slide=0
class Bullet:
    def __init__(self,kind,x,y,range1,damage, asn):
        self.type=kind
        self.row=x
        self.dist=y
        self.range=range1
        self.dmg=damage
        self.slide=asn
    def __str__(self):
        return "%d bullet %d down row %d"%(self.type,self.dist,self.row)
    def draw(self):
        screen.blit(bullet[self.type],(self.dist,100+self.row*100))

class Sun:
    def __init__(self,size,currY,destX,destY,asn,time):
        self.type=size
        self.cy=currY
        self.dx=destX
        self.dy=destY
        self.slide=asn
        self.time=time
    def __str__(self):
        return "%d sized sun landing at (%d,%d)"%(self.type,self.dx,self.dy)
    def draw(self):
        screen.blit(sunSpr,(self.dx-25,int(self.cy)-25))

class Zombie:
    def __init__(self,kind,x,y,speed,health,damage,asn,time,state,action):
        self.type=kind
        self.row=x
        self.dist=y
        self.speed=speed
        self.health=health
        self.dmg=damage
        self.slide=asn
        self.passed=time
        self.state=state
        self.action=action
    def __str__(self):
        return "%d zombie, %d up row %d"%(self.type,self.dist,self.row)


    def draw(self):
        #normal zombie
        if self.health>10:
            if self.action=="eating":
                screen.blit(states[self.type+2][self.state/10],(800-self.dist,50+self.row*100-25*min(1,self.type)+10))
            else:
                screen.blit(zombie[self.type][self.slide/10],(800-self.dist,50+self.row*100-25*min(1,self.type)))
        #change to normal zombie
        if self.health<=10 and self.health>=5:
            screen.blit(zombie[0][self.slide/10],(800-self.dist,50+self.row*100-25*min(1,self.type)+10))
        #change to one arm
        if self.health<5 and self.health>0:
            screen.blit(states[0][self.state/10],(800-self.dist,50+self.row*100-25*min(1,self.type)))
        #dead
        if self.health==0:
            screen.blit(states[1][self.state/10],(800-self.dist,50+self.row*100-25*min(1,self.type)+30))
        
            
#----Zen Garden Stuff----------------
bg=image.load("zen copy.png")
class zPlant:
    "zPlant class for representing and drawing plants in the zen garden"
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
            screen.blit(states[self.state],(plantRect[0]+plantRect[2]-5,\
                                            plantRect[1]-7))
        self.slide+=1
        if self.slide>len(plant[self.type])*20-1:
            self.slide=0

def getDrawRect(img,potRect):
    "Return the Rect of the plant based on the image and the Rect of the pot"
    x,y=img.get_width(),img.get_height()
    return Rect(potRect[0]+38-x/2,potRect[1]+28-y,x,y)


def addCoin(plant,r,typeCoin):      #Adds a coin. Rocket science....
    global allcoins
    if typeCoin==3:
        typeCoin=choice([0,0,0,0,0,0,0,1,1,1,2])
    cy,dx,dy=r[1]-10,randint(r[0]-10,r[0]+r[2]+10),r[1]+r[-2]+10
    allcoins.append(Coin(typeCoin,cy,dx,dy,0,clock()))
    
def zenGarden(bg,user):
    "Main zen garden function to actually run the mini-game"
    global allcoins
    data=map(eval,open(username+".txt").read().strip().split("\n"))
    topNum,topTypes,money,numPlants=data[:4]
    zplants=data[4:]
    myTopRects=topRects[:topNum]

    screen.blit(bg,(0,0))
    screen.blit(top[topNum-1],(0,0))
    
    allcoins=[]
    tool="none"
    out="none"              #We will return a page for the program to go to
            
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
        mx,my=mouse.get_pos()

        for i in range (len(zplants)):  #Changing state to 0 after a day
            if zplants[i].state not in [0,5] and checkdate(zplants[i].date):
                zplants[i].state=0
                zplants[i].water=0
        
        for num in range (topNum):      #Toolbar
            if tool!=num:
                screen.blit(stuff[topTypes[num]],myTopRects[num])
    
        plantRects=[]                   #Gets a list of the Rects of all plants
        for p in zplants:
            p.draw()
            pic=plant[p.type][p.slide/20]
            rect=garden[p.row][p.col]
            plantRects.append(getDrawRect(pic,rect))
            

        for i in range (len(zplants)):  #State changes and coin production
            r=plantRects[i]
            if r.collidepoint(lcx,lcy) and tool==zplants[i].state==0:
                tool="none"
                zplants[i].state=5
                zplants[i].water+=1
                zplants[i].passed=clock()
                addCoin(zplants[i],r,0)
            elif r.collidepoint(lcx,lcy) and tool==zplants[i].state==1:
                tool="none"
                zplants[i].state=5
                zplants[i].age+=1
                zplants[i].passed=clock()
                for c in range (zplants[i].age):
                    addCoin(zplants[i],r,1)
            elif r.collidepoint(lcx,lcy) and tool==zplants[i].state:
                zplants[i].state=4
                tool="none"
                addCoin(zplants[i],r,1)
            if zplants[i].state==5:
                if clock()-zplants[i].passed>5:
                    if zplants[i].water<3:
                        zplants[i].state=0
                    elif zplants[i].age<3 and checkdate(zplants[i].date):
                        zplants[i].state=1
                        zplants[i].date=datetime.now()
                    elif zplants[i].age>=3 and checkdate(zplants[i].date):
                        zplants[i].state=randint(2,3)
                        zplants[i].date=datetime.now()

            if clock()-zplants[i].passed>10 and zplants[i].state==4:
                if randint(1,2)==1:
                    addCoin(zplants[i],r,3)
                    zplants[i].passed=clock()
            
        for c in allcoins:              #Drawing and picking up coins
            c.draw()
            if Rect(c.dx-20,c.cy-20,40,40).collidepoint(lcx,lcy):
                money+=coinVals[c.type]
                c.time="x"

        if lclick:                      #Getting and resetting tool
            tool="none"
        for r in range(topNum):
            if myTopRects[r].collidepoint(lcx,lcy):
                tool=topTypes[r]
        if tool!="none":
            screen.blit(zcursors[topTypes[tool]],(mx-35,my-35))
                
        if mainRect.collidepoint(lcx,lcy):
            out="menu"
        if shopRect.collidepoint(lcx,lcy):
            out="shop"

        display.flip()
        myClock.tick(100)
        screen.blit(copy,(0,0))
        allcoins=filter(lambda x:x.time!="x" and clock()-x.time<8,allcoins)

    outf=open(username+".txt","w")          #Write datafile after exiting loop
    outf.write("%d\n"%topNum+str(topTypes)+"\n%d\n%d\n"%(money,len(zplants))+\
               "\n".join(map(str,zplants)))
    outf.close()
    return out
#-----End of Zen Garden----------------------------------------------

#-----Shop Stuff---------------------------------------------------
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

#-----Adventure Mode stuff-------------------------------------------
def getCol(z):
    'This function gets the grid column position of a zombie'
    for col in range(9):
        if z.type in [1,2,3,4]:
            if yard[z.row][col].collidepoint(830-z.dist,150+z.row*100):
                return col
        elif z.type in [0]:
            if yard[z.row][col].collidepoint(830-z.dist,85+z.row*100):
                return col
    return -1

def pause():
    global running,startTime
    timer=clock()
    slide=0
    bg=screen.copy()
    screen.blit(bg,(0,0))
    pausing=True
    while pausing:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                pausing=False
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1 and resumeRect.collidepoint(evt.pos):
                    pausing=False
        screen.blit(pauseScr[slide/10],(187,89))
        display.flip()
        screen.blit(bg,(0,0))
        slide+=1
        if slide==109:
            slide=0
    timepassed=clock()-timer
    startTime+=timepassed
    for k in plants+sunPlants+zombies:
        k.passed+=timepassed

def addSun():
    global startTime,fallingsun,sunPlants
    if clock()-startTime>10:
        fallingsun.append(Sun(1,30,randint(65,775),randint(150,575),0,clock()))
        startTime=clock()
    for i in sunPlants:
        if clock()-i.passed>i.speed:
            fallingsun.append(Sun(1,110+100*i.row,\
                                  randint(40+i.col*80-30,40+i.col*80+30),\
                                  120*(i.row+1),0,clock()))
            i.passed=clock()
def addBullets():
    global plants, zombies, bullets
    for p in plants:
        for z in zombies:
            if p.row==z.row and clock()-p.passed>p.speed:
                bullets.append(Bullet(p.type,p.row,120+p.col*70,\
                                          bRng[p.type],bDmg[p.type],0))
                p.passed=clock()
                break       #So that they only shoot once/twice per row
            
def addPlants():
    #plant=["peashooter","sunflower","wallnut","repeater","icepea"]
    global planting,mx,my,whichplant,selection,sun,cursor
    if planting==True:
        for x in range (5):
            for y in range (9):
                if grid[x][y]!="p" and yard[x][y].collidepoint(mx,my):
                    screen.blit(plant[whichplant][0],(40+y*80,90+x*100))
                    if whichplant in [0,3,4] and lclick:
                        plants.append(Plant(whichplant,x,y,pSpd[whichplant],\
                                    pHP[whichplant],pDmg[whichplant],0,clock()))
                        sun-=cost[whichplant]
                    elif whichplant in [1] and lclick:
                        sunPlants.append(Plant(whichplant,x,y,pSpd[whichplant],\
                                    pHP[whichplant],pDmg[whichplant],0,clock()))
                        sun-=cost[whichplant]
                    elif whichplant in [2] and lclick:
                        dPlants.append(Plant(whichplant,x,y,pSpd[whichplant],\
                                    pHP[whichplant],pDmg[whichplant],0,clock()))
                        sun-=cost[whichplant]
        
        if lclick:
            planting=False
            whichplant="x"
            cursor="none"
    for i in range (5):
        if bar[i].collidepoint(lcx,lcy) and planting==False and \
           sun>=cost[i] and selection[i]!="x":
            planting=True
            whichplant=selection[i]
            cursor=plant[whichplant][0]
            break
        
def shovel():
    global grid,plants, shovelling,lclick,currShovel,cursor,lcx,lcy
    if shovelling==True:
        for p in plants+sunPlants+dPlants:
            if yard[p.row][p.col].collidepoint(lcx,lcy) and lclick:
                p.health=-100
        if lclick:
            shovelling=False
            currShovel=shovelFull
            cursor="none"
    if shovelRect.collidepoint(lcx,lcy) and shovelling==False:
        shovelling=True
        currShovel=shovelEmpty
        cursor=shovelCursor
                

                
def moveStuff():
    global zombies,plants,sunPlants,bullets,fallingsun,grid,lclick,sun
    global dPlants,lawnMowers

    #Moving Zombies and Zombies Eating Plants & Lawn Mowers hitting zombies
    for z in zombies:
        if 800-z.dist<21 and [z.row,0] in lawnMowers:
            lawnMowers[z.row][1]=1
        for mower in lawnMowers:
            if mower[0]==z.row and mower[1]+20>800-z.dist:
                z.health=-1000
                
        c=getCol(z)
        if c==-1:
            if z.slide<800 or z.slide>850:
                z.dist+=0.08*z.speed
            z.slide+=1
            if z.slide>(10*len(zombie[z.type])-1):
                z.slide=0

        if c!=-1:
            if grid[z.row][c]!="p":
                if z.slide<800 or z.slide>850:
                    z.dist+=0.08*z.speed
                z.slide+=1
                if z.slide>(10*len(zombie[z.type])-1):
                    z.slide=0
            else:
                for p in plants+sunPlants+dPlants:
                    if p.row==z.row and p.col==c and clock()-z.passed>2:
                        p.health-=1
                        z.passed=clock()
                        break
                        
    #Moving Bullets and Bullets Hitting Zombies:
    for b in bullets:
        b.dist+=2
        for z in zombies:
            if b.row==z.row and b.dist>810-z.dist:
                b.dist=999
                z.health-=1
                break
    
    #Moving Sun & Picking up sun
    for s in fallingsun:
        if s.cy<s.dy:
            s.cy+=0.5
        if lclick:
            if Rect(s.dx-35,s.cy-35,70,70).collidepoint(lcx,lcy):
                sun+=25
                s.time="x"
    #states
    for z in zombies:
        c=getCol(z)
        for p in plants+sunPlants+dPlants:
            if p.row==z.row and p.col==c:
                z.action="eating"
                z.state+=1
                if p.health==0:
                    z.action="living"
        if z.health!=100 and z.action!="eating":
            z.state+=1
            z.action="living"
        if z.state>(10*(action[z.action]-1)):
            z.state=0
        #change to one arm
        if z.health<5 and z.health>0:
            z.action="dying"
        #dead
        if z.health==0:
            z.action="dead"
 
                
def updateScreen():
    global grid,zombies,plants,sunPlants,fallingsun,bullets,comicFont,sun
    global dPlants, lawnMowers, currShovel, cursor
    bullets=filter(lambda x:0<=x.dist<=800,bullets)
    zombies=filter(lambda x:int(x.health)>0 and 0<=x.dist<=800,zombies)
    plants=filter(lambda x:x.health>0,plants)
    sunPlants=filter(lambda x:x.health>0,sunPlants)
    dPlants=filter(lambda x:x.health>0,dPlants)
    fallingsun=filter(lambda x:x.time!="x" and abs(clock()-x.time)<10,fallingsun)
    for i in range (len(lawnMowers)):
        if lawnMowers[i][1]>800:
            lawnMowers[i]=["x",9999]
    
    grid=[[0]*9 for i in range (5)]
    for p in plants+sunPlants+dPlants:
        grid[p.row][p.col]="p"
    
    for thing in plants+sunPlants+dPlants+bullets+fallingsun+zombies:
        thing.draw()
    for mower in lawnMowers:
        if mower!=["x",9999]:
            if mower[1]==0:
                screen.blit(lawnWSpr,(0,90+mower[0]*100))
            else:
                screen.blit(lawnSpr,(mower[1],90+mower[0]*100))
                mower[1]=mower[1]+2
    screen.blit(currShovel,shovelRect)
    screen.blit(pausebutton,pauseRect)
    sunPic=comicFont.render(str(sun),True,(0,0,0))
    screen.blit(sunPic,(50-sunPic.get_width()/2,71-sunPic.get_height()/2))

font.init()
comicFont = font.SysFont("Comic Sans MS", 16)

display.set_caption("Plants vs. Zombies")

bg_day=image.load("Frontyard play.jpg").convert_alpha()
screen.blit(bg_day,(0,0))

cost=[100,50,50,200,175]
screen.blit(seedcart,(9,1))
for button in range (5):
    screen.blit(buttons[button],bar[button])
selection=[0,1,2,3,4,"X","X"]

def adventure():
    global lawnMowers,plants,sunPlants,dPlants,zombies,bullets,fallingsun
    global startTime,passTime,counting,progress,cursor,planting,shovelling
    global currShovel,whichplants,level,filelevel,lcx,lcy,mx,my,lclick,sun
    screen.blit(bg_day,(0,0))
    cost=[100,50,50,200]
    screen.blit(seedcart,(9,1))
    for button in range (5):
        screen.blit(buttons[button],bar[button])
    selection=[0,1,2,3,"X","X"]
    lawnMowers=[[0,0],[1,0],[2,0],[3,0],[4,0]]
    plants=[]                               #Shooting Plants
    sunPlants=[]                            #Sun-producing Plants
    dPlants=[]                              #Defensive Plants
    zombies=[]
    bullets=[]
    fallingsun=[]
    sun=10000
    startTime=clock()
    passTime=clock()
    counting=0
    progress="none"
    cursor="none"
    planting=False
    shovelling=False
    currShovel=shovelFull 
    whichplant="X"
    level="levelOne"
    filelevel=open(level+".txt").read().strip().split("\n")

    out="none"
    while out=="none":
        copy=screen.copy().convert_alpha()
        lclick=rclick=False
        lcx,lcy=999,999
        for evt in event.get():
            if evt.type==QUIT:
                out="quit"
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                    lclick=True
                    lcx,lcy=evt.pos
                    
        if counting==0:
            progress="beginning"
        if progress!="end":
            counting+=1
        if progress=="beginning" or "middle wave" or "ending wave":
            if counting%800==0:
                zombies.append(Zombie(0,randint(0,4),0,zSpd[0],zHP[0],zDmg[0],0,clock(),0,0))
        if counting==1000:
            progress="middle wave"
            zombies.append(Zombie(3,randint(0,4),0,zSpd[3],zHP[3],zDmg[3],0,clock(),0,0))
        if counting==2300:
            progress="ending wave"
            zombies.append(Zombie(3,randint(0,4),0,zSpd[3],zHP[3],zDmg[3],0,clock(),0,0))
        if counting==5000:
            progress="end"

        print counting
            
        mx,my=mouse.get_pos()

        updateScreen()
        shovel()
        addSun()
        addBullets()
        addPlants()    
        moveStuff()

        if pauseRect.collidepoint(lcx,lcy):
            pause()       
                
        if cursor!="none":
            if 0<=mx-cursor.get_width()<=800 and 0<=my-cursor.get_height()/2<=800:
                screen.blit(cursor,(mx-cursor.get_width()/2,my-cursor.get_height()/2))

        display.flip()
        myClock.tick(100)
        screen.blit(copy,(0,0))
    return out
#-----End of Adventure---------------------

#-----Other Stuff-------------------
def menu():
    global running
    waiting=True
    while waiting:
        lclick=False
        for evt in event.get():
            if evt.type == QUIT:
                return "quit"
            if evt.type==MOUSEBUTTONDOWN:
                lclick=True
        screen.blit(menupg,(0,0))
        mx,my= mouse.get_pos()
        pgs=["adventure","mini","puzzle","survival","options","help","quit",
             "zen","almanac","shop"]
        cols=[(0,0,255),(255,0,0),(0,255,0),(255,255,0),(0,255,255),(255,0,255),
              (255,255,255),(0,0,0),(111,111,111),(222,222,222)]
        states=[True,False,False,False,False,True,True,True,False,True]
        if lclick:
            for i in range(10):
                pos=menubuttons.get_at((mx,my))
                if cols[i]==pos[:3] and lclick and states[i]:
                    return pgs[i]
        myClock.tick(100)
        display.flip()
        
def pvzhelp():
    while True:
        for evt in event.get():
            if evt.type==QUIT:
                return "quit"
            if evt.type==MOUSEBUTTONDOWN:
                if helpRect.collidepoint(evt.pos):
                    return "menu"
        screen.blit(helppg,(0,0))
        if helpRect.collidepoint(mouse.get_pos()):
            draw.rect(screen,(0,144,148),helpRect,3)
        myClock.tick(100)
        display.flip()
                    
def selectPlants(plantList):
    global choiceRects, running
    if len(plantList)<7:
        return plantList+["X"]*(6-len(plantList))
    selecting=True
    selection=["X"]*6
    while selecting:
        lcx,lcy=999,999
        for evt in event.get():
            if evt.type == QUIT:
                running=False
                return "quit"
            if evt.type==MOUSEBUTTONDOWN:
                lcx,lcy=evt.pos
        for i in range (len(choiceRects)):
            if choiceRects[i].collidepoint((lcx,lcy)):
                if "X" in selection and i not in selection:
                    selection[selection.index("X")]=i
        if playRect.collidepoint((lcx,lcy)) and "X" not in selection:
            return selection

def scrollover(img):
    global running
    sx=0
    while sx<600:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                break
        screen.blit(img.subsurface(Rect(sx,0,800,600)),(0,0))
        display.flip()
        myClock.tick(100)
        sx+=5
def scrollback(img):
    global running
    sx=600
    while sx>214:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                break
        screen.blit(img.subsurface(Rect(sx,0,800,600)),(0,0))
        display.flip()
        myClock.tick(100)
        sx-=5
        
pg="menu"
while pg!="quit":
    if pg=="menu":
        pg=menu()
    if pg=="help":
        pg=pvzhelp()
    if pg=="adventure":
        pg=adventure()
    if pg=="zen":
        pg=zenGarden(bg,username)
    if pg=="shop":
        pg=shop()

    display.flip()
quit()
