from pygame import *
#music
mixer.pre_init(22050,-16,2,4096)
mixer.init(44100)
mixer.music.load("music/main menu.mp3")
mixer.music.play(-1)

loading=image.load("graphics\loading.PNG")
display.init()
screen=display.set_mode((800,600))
display.set_icon(image.load("icon.png"))
display.set_caption("Plants vs. Zombies")
screen.blit(loading,(0,0))
display.flip()
loaded=image.load("graphics\loaded.PNG")
font.init()
comicFont = font.SysFont("Comic Sans MS",16)

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

def almanac():
    "Initiates the almanac feature"
    checking=True
    screen.blit(bg_almanac,(0,0))
    while checking:
        lcx,lcy=999,999
        for evt in event.get():
            if evt.type==QUIT:
                writeData(username)
                qa()
            elif evt.type==MOUSEBUTTONDOWN:
                lcx,lcy=evt.pos
        for r in range (10):
            if alRects[r].collidepoint(lcx,lcy):
                screen.blit(almanacs[r],(450,80))
        if alDoneRect.collidepoint(lcx,lcy):
            checking=False
        display.flip()
        myClock.tick(100)

def printDate(now):
    return "datetime(%d,%d,%d,%d,%d,%d,%d)"%(now.year,now.month,now.day,\
                                now.hour,now.minute,now.second,now.microsecond)
def checkdate(date):
    "Check if a day has passed since date"
    now=datetime.now()
    return (now-date).days>0

def reset():
    "Reset global values for use in Adventure/Minigames"
    global lawnMowers,plants,sunPlants,dPlants,zombies,bullets,fallingsun
    global startTime,passTime,counting,progress,cursor,planting,shovelling
    global currShovel,whichplant,sun,allcoins,exploPlants
    lawnMowers=[[0,0],[1,0],[2,0],[3,0],[4,0]]
    plants=[]                               #Shooting Plants
    sunPlants=[]                            #Sun-producing Plants
    dPlants=[]                              #Defensive Plants
    exploPlants=[]                          #Explosive Plants, which does not work and is useless.
    zombies=[]
    bullets=[]
    fallingsun=[]
    allcoins=[]
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

def addCoin(plant,r,typeCoin):      #Adds a coin. Rocket science....
    global allcoins
    if typeCoin==3:
        typeCoin=choice([0,0,0,0,0,0,0,1,1,1,2])
    cy,dx,dy=r[1]-10,randint(r[0]-10,r[0]+r[2]+10),r[1]+r[-2]+10
    allcoins.append(Coin(typeCoin,cy,dx,dy,0,clock()))

def addZombie(kind,prob,freq):      
    '''Adds zombies. Type and number can be defined, if not, they will be
        randomly chosen based on a defined probability list.'''
    global zombies
    if kind=="x":
        kind=choice(prob)
    for i in range (choice(freq)):
        zombies.append(Zombie(kind,randint(0,4),0,zSpd[kind],zHP[kind],\
                              zDmg[kind],0,clock(),0,"living"))
    
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
        return "%d coin elanding at (%d,%d)"%(self.type,self.dx,self.dy)
    def draw(self):
        screen.blit(coins[self.type],(self.dx-25,int(self.cy)-25))
        if self.cy<self.dy:
            self.cy=self.cy+1
class Plant:
    #plant=["peashooter","sunflower","wallnut","repeater","icepea","firepea","cherry",
    #"squash","jalapeno"]
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
        if self.type<6:
            screen.blit(plant[self.type][self.slide/20],\
                        (40+self.col*80,90+self.row*100))
            self.slide+=1
            if self.slide>len(plant[self.type])*10-1:
                self.slide=0
        else:
            screen.blit(plant[self.type][self.slide/20],(40+self.col*80,90+self.row*100))
            self.slide+=1
            if self.slide>len(plant[self.type])*10-1:
                self.health=0
                
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
        if self.cy<self.dy:
            self.cy+=0.5

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
        if self.action=="eating":
            screen.blit(condition[self.type+2][self.state/10],(800-self.dist,50+self.row*100-25*min(1,self.type)+10))
        if self.action=="living":
            screen.blit(zombie[self.type][self.slide/10],(800-self.dist,50+self.row*100-25*min(1,self.type)))
        if self.action=="dying":
            screen.blit(condition[0][self.state/10],(800-self.dist,50+self.row*100-25*min(1,self.type)))
        if self.action=="newspaperdying":
            screen.blit(condition[6][self.state/10],(800-self.dist,50+self.row*100-25*min(1,self.type)))
        if self.health==0:
            screen.blit(condition[1][self.state/10],(800-self.dist,50+self.row*100-25*min(1,self.type)+30))            
                
            
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
 
def zenGarden(bg,user):
    "Main zen garden function to actually run the mini-game"
    global allcoins,topNum,topTypes,money,numPlants,zplants,numfert,numspray,allcoins

    mixer.music.stop()
    mixer.music.load("music/zen.mp3")
    mixer.music.play(-1)
    
    myTopRects=topRects[:topNum]

    screen.blit(bg,(0,0))
    screen.blit(top[topNum-1],(0,0))
    
    
    tool=out="none"             #We will return a page for the program to go to
            
    while out=="none":
        copy=screen.copy().convert_alpha()
        allcoins=[]
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
                if numfert>0:
                    tool="none"
                    zplants[i].state=5
                    zplants[i].age+=1
                    zplants[i].passed=clock()
                    for c in range (zplants[i].age):
                        addCoin(zplants[i],r,1)
                    numfert-=1
            elif r.collidepoint(lcx,lcy) and tool==zplants[i].state==2:
                if numspray>0:
                    zplants[i].state=4
                    tool="none"
                    addCoin(zplants[i],r,1)
                    numspray-=1
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

            if clock()-zplants[i].passed>30 and zplants[i].state==4:
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
                
        if tool!="none":                #Cursor
            screen.blit(zcursors[topTypes[tool]],(mx-35,my-35))

        fertPic=comicFont.render("x"+str(numfert),True,(255,255,255))
        screen.blit(fertPic,(108,48))
        sprayPic=comicFont.render("x"+str(numspray),True,(255,255,255))
        screen.blit(sprayPic,(181,48))
                
        if mainRect.collidepoint(lcx,lcy):
            out="menu"
        if shopRect.collidepoint(lcx,lcy):
            out="shop"

        display.flip()
        myClock.tick(100)
        screen.blit(copy,(0,0))
        allcoins=filter(lambda x:x.time!="x" and clock()-x.time<8,allcoins)
    return out
#-----End of Zen Garden----------------------------------------------

#-----Shop Stuff---------------------------------------------------
def changeSold(alreadybought,numfert,numspray,sprouts):
    "Function to return a list of what items in the shop should say 'Sold Out'"
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

def addPlant(kind):
    "Searches for an empty spot in the zen garden and adds a sprout"
    global zplants,numPlants
    pts=[(x,y) for x in range (4) for y in range (8)]
    occ=[]
    for p in zplants:
        occ.append((p.row,p.col))
    pts=filter(lambda x: x not in occ, pts)
    px,py=choice(pts)
    zplants.append(zPlant(kind,px,py,0,0,0,\
                          datetime(2010,6,14,9,3,1,325000),clock(),0))
    numPlants+=1
        
def shop():
    "Main function to run the shop"
    global money,numfert,numspray,alreadybought,sprouts,zplants,topTypes,topNum
    out="none"
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
                    if item==4:
                        numfert+=5
                    elif item==5:
                        numspray+=5
                    elif item in range(0,4):
                        sprouts[item]=datetime.now()
                        addPlant(randint(0,3))
                    else:
                        alreadybought.append(item)
                        topTypes.append(item-3)
                        topNum+=1
                    money-=costs[item]
                    soldout=changeSold(alreadybought,numfert,numspray,sprouts)

        moneyPic=comicFont.render(str(money),True,(205,205,0))
        screen.blit(moneyPic,sMoneyRect)

        display.flip()
        screen.blit(copy,(0,0))
    return out

#-----Adventure Mode stuff-------------------------------------------
#zombie=["normal","cone","bucket","flag","newspaper","imp","chen","joker","door"]
def getCol(z):
    "Gets the grid column position of a zombie"
    for col in range(9):
        if z.type in [1,2,3,6]:
            if yard[z.row][col].collidepoint(830-z.dist,150+z.row*100):
                return col
        elif z.type in [0,4,7,8]:
            if yard[z.row][col].collidepoint(830-z.dist,85+z.row*100):
                return col
        elif z.type in [5]:
            if yard[z.row][col].collidepoint(830-z.dist,65+z.row*100):
                return col
            
    return int((830-z.dist)/100)             #Return an approximation if not found

def pause():
    "Temporarily freezes the game"
    global startTime,plants,sunPlants,zombies,exploPlants
    timer=clock()
    slide=0
    out="pause"
    while out=="pause":
        for evt in event.get():
            if evt.type==QUIT:
                out="quit"
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1 and resumeRect.collidepoint(evt.pos):
                    out="none"
        screen.blit(pauseScr[slide/10],(187,89))
        display.flip()
        myClock.tick(100)
        slide+=1
        if slide==109:
            slide=0
    timepassed=clock()-timer            #Reset all times after pausing is done
    startTime+=timepassed
    for k in plants+sunPlants+zombies+exploPlants:
        k.passed+=timepassed
    return out

def igmenu():
    "Freezes the game and gives the user options"
    out="wait"
    bg=screen.copy().convert_alpha()
    
    while out=="wait":
        screen.blit(bg,(0,0))
        screen.blit(igMenu,(180,50))
        lcx,lcy=999,999
        for evt in event.get():
            if evt.type==QUIT:
                out="quit"
            elif evt.type==MOUSEBUTTONDOWN:
                lcx,lcy=evt.pos
        for r in range (4):
            if directRects[r].collidepoint(lcx,lcy):
                out=direct[r]
        if out=="almanac":
            almanac()
            out="wait"
        display.flip()
        myClock.tick(100)
    return out

def addSun():
    "Adds sun from both 'natural' causes and sunflowers"
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
    "Makes all bullet-shooting plants shoot."
    global plants, zombies, bullets
    for p in plants:
        for z in zombies:
            if p.row==z.row and clock()-p.passed>p.speed:
                bullets.append(Bullet(p.type,p.row,120+p.col*70,\
                                          bRng[p.type],bDmg[p.type],0))
                p.passed=clock()
                break       #So that they only shoot once/twice per row
            
def addPlants():
    "Gets the chosen plant and plants it on the lawn or cancels the planting"
    #plant=["peashooter","sunflower","wallnut","repeater","icepea","firepea","cherry",
    #"squash","jalapeno"]
    global planting,mx,my,whichplant,selection,sun,cursor,times
    if planting==True:
        for x in range (5):
            for y in range (9):
                if grid[x][y]!="p" and yard[x][y].collidepoint(mx,my):
                    screen.blit(plant[whichplant][0],(40+y*80,90+x*100))
                    #bullet plants
                    if whichplant in [0,3,4,5] and lclick:
                        plants.append(Plant(whichplant,x,y,pSpd[whichplant],\
                                    pHP[whichplant],pDmg[whichplant],0,clock()))
                        sun-=cost[whichplant]
                    #sun producing plant
                    elif whichplant in [1] and lclick:
                        sunPlants.append(Plant(whichplant,x,y,pSpd[whichplant],\
                                    pHP[whichplant],pDmg[whichplant],0,clock()))
                        sun-=cost[whichplant]
                    #defense plant
                    elif whichplant in [2] and lclick:
                        dPlants.append(Plant(whichplant,x,y,pSpd[whichplant],\
                                    pHP[whichplant],pDmg[whichplant],0,clock()))
                        sun-=cost[whichplant]
                    #explosive plants
                    elif whichplant in [6,7,8] and lclick:
                        exploPlants.append(Plant(whichplant,x,y,pSpd[whichplant],\
                                    pHP[whichplant],pDmg[whichplant],0,clock()))
                        sun-=cost[whichplant]
        
        if lclick:
            planting=False
            whichplant="x"
            cursor="none"
    for i in range (6):             #Checks to see if we're planting
        if bar[i].collidepoint(lcx,lcy) and planting==False and \
           sun>=cost[i] and selection[i]!="x":
            planting=True
            whichplant=selection[i]
            cursor=plant[whichplant][0]
            break
        
def shovel():
    "Allows user to remove plants"
    global grid,plants, shovelling,lclick,currShovel,cursor,lcx,lcy
    if shovelling==True:
        for p in plants+sunPlants+dPlants+exploPlants:
            if yard[p.row][p.col].collidepoint(lcx,lcy) and lclick:
                p.health=-100
        if lclick:
            shovelling=False
            currShovel=shovelFull           #Change the icon/button
            cursor="none"
    if shovelRect.collidepoint(lcx,lcy) and shovelling==False:
        shovelling=True
        currShovel=shovelEmpty              
        cursor=shovelCursor
                
def moveStuff():
    "Moves everything that's on-screen"
    global zombies,plants,sunPlants,bullets,fallingsun,grid,lclick,sun
    global dPlants,lawnMowers,exploPlants

    #Moving Zombies, Zombies Eating Plants & Lawn Mowers hitting zombies
    for z in zombies:
        if 800-z.dist<21 and [z.row,0] in lawnMowers:   #Start the mowers
            lawnMowers[z.row][1]=1
        for mower in lawnMowers:
            if mower[0]==z.row and mower[1]+20>800-z.dist:
                z.health=-1000
        c=getCol(z)
        if grid[z.row][c]!="p":         #Move if there's no plant
            z.dist+=0.08*z.speed
            z.slide+=1
            if z.slide>(10*len(zombie[z.type])-1):
                z.slide=0
        else:                           #Find and hurt the plant if there is
            for p in plants+sunPlants+dPlants+exploPlants:
                if p.row==z.row and p.col==c and clock()-z.passed>2:
                    p.health-=z.dmg
                    z.passed=clock()
                    break
                        
    #Moving Bullets and Bullets Hitting Zombies:
    for b in bullets:
        b.dist+=2
        for z in zombies:
            if b.row==z.row and b.dist>810-z.dist and b.dist!=999 :
                b.dist=999
                #Firepea and Chen
                if (z.type,b.type)==(6,5):
                    z.health-=10
                    break
                #Other plants
                elif z.type<6:
                    z.health-=bDmg[b.type]
                    break
    
    #Moving Sun & Picking up sun
    for s in fallingsun:
        if lclick:
            if Rect(s.dx-35,s.cy-35,70,70).collidepoint(lcx,lcy):
                sun+=25
                s.time="x"
    #states
    for z in zombies:
        c=getCol(z)
        #zombie=["normal","cone","bucket","flag","newspaper","imp","chen","joker","door","dancing"]
        for p in plants+sunPlants+dPlants+exploPlants:
            if p.row==z.row and p.col==c:
                z.action="eating"
                z.state+=1
                if p.health<1:
                    z.action="living"
        #normal-like zombies
        if z.type<3:
            #change tall zombies to normal
            if z.health<=10:
                z.type=0
            #change to one arm
            if z.health<5 and z.health>0:
                z.action="dying"
        
        if z.health!=100 and z.action!="eating":
            z.state+=1
            z.action="living"
        if z.state>(10*(action[z.action]-1)):
            z.state=0
        #dead
        if z.health==0:
            z.action="dead"

            
def updateScreen():
    global grid,zombies,plants,sunPlants,fallingsun,bullets,comicFont,sun
    global dPlants, lawnMowers, currShovel, cursor, exploPlants
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
    for p in plants+sunPlants+dPlants+exploPlants:
        grid[p.row][p.col]="p"
    
    for thing in plants+sunPlants+dPlants+exploPlants+bullets+fallingsun+zombies:
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
    screen.blit(menubutton,igMenuRect)
    sunPic=comicFont.render(str(sun),True,(0,0,0))
    screen.blit(sunPic,(50-sunPic.get_width()/2,71-sunPic.get_height()/2))

def reset():
    global lawnMowers,plants,sunPlants,dPlants,zombies,bullets,fallingsun
    global startTime,passTime,counting,progress,cursor,planting,shovelling
    global currShovel,whichplant,sun,exploPlants
    lawnMowers=[[0,0],[1,0],[2,0],[3,0],[4,0]]
    plants=[]                               #Shooting Plants
    sunPlants=[]                            #Sun-producing Plants
    dPlants=[]                              #Defensive Plants
    exploPlants=[]                          #Explosive Plants
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

def adventure(clevel):
    global lawnMowers,plants,sunPlants,dPlants,zombies,bullets,fallingsun
    global startTime,passTime,counting,progress,cursor,planting,shovelling
    global currShovel,whichplant,lcx,lcy,mx,my,lclick,sun,money,level
    global selection, cost, exploPlants
    scrollover(dayfull)
    selection=selectPlants()
    times=[clock() for i in range (6)]
    scrollback(dayfull)
    screen.blit(seedcart,(9,1))
    #selection of plant slots
    cost=[100,50,50,200,175,175,150]
    #button is in graphics.py
    for button in range(6):
        if selection[button]!="X":
            screen.blit(buttons[selection[button]],bar[button])

        
    filelevel=map(eval,open("level%d.txt"%clevel).read().strip().split("\n"))
    kindfreq=filelevel[-1]
    reset()

    mixer.music.stop()
    mixer.music.load("music/adventure.mp3")
    mixer.music.play(-1)
    
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

                    
        freq=[[0,0,0,1,1,2],[0,1,1,2,2,3],[1,1,2,2,3,4]]
        
        if counting==100:
            progress=0
        counting+=1
        if progress not in ["none","end"] and counting%800==0:
            addZombie("x",kindfreq[progress],freq[progress])
        if counting==filelevel[0]:
            progress=1
            addZombie(3,[],[1])
        if counting==filelevel[1]:
            progress=2
            addZombie(3,[],[1])
        if counting==filelevel[2]:
            progress="end"

        if progress=="end" and zombies==[]:
            money+=250
            level+=1
            if level==10:
                level=0
            out="adventure"
            
        mx,my=mouse.get_pos()

        updateScreen()
        shovel()
        addSun()
        addBullets()
        addPlants()    
        moveStuff()

        if pauseRect.collidepoint(lcx,lcy):
            out=pause()
        if igMenuRect.collidepoint(lcx,lcy):
            out=igmenu()
                
        if cursor!="none":
            if 0<=mx-cursor.get_width()<=800 and 0<=my-cursor.get_height()/2<=800:
                screen.blit(cursor,(mx-cursor.get_width()/2,my-cursor.get_height()/2))

        display.flip()
        myClock.tick(100)
        screen.blit(copy,(0,0))
    return out
#-----End of Adventure---------------------

#-----Mini-Game: Invisi-Ghoul---------------------
def invUpdateScreen():
    global grid,zombies,plants,sunPlants,fallingsun,bullets,comicFont,sun
    global dPlants, lawnMowers, currShovel, cursor,exploPlants
    bullets=filter(lambda x:0<=x.dist<=800,bullets)
    zombies=filter(lambda x:int(x.health)>0 and 0<=x.dist<=800,zombies)
    plants=filter(lambda x:x.health>0,plants)
    sunPlants=filter(lambda x:x.health>0,sunPlants)
    dPlants=filter(lambda x:x.health>0,dPlants)
    exploPlants=filter(lambda x:x.health>0,exploPlants)
    fallingsun=filter(lambda x:x.time!="x" and abs(clock()-x.time)<10,fallingsun)
    for i in range (len(lawnMowers)):
        if lawnMowers[i][1]>800:
            lawnMowers[i]=["x",9999]
    
    grid=[[0]*9 for i in range (5)]
    for p in plants+sunPlants+dPlants:
        grid[p.row][p.col]="p"
    
    for thing in plants+sunPlants+dPlants+bullets+fallingsun:
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
    screen.blit(menubutton,igMenuRect)
    sunPic=comicFont.render(str(sun),True,(0,0,0))
    screen.blit(sunPic,(50-sunPic.get_width()/2,71-sunPic.get_height()/2))
    
def invisiGhoul(clevel):
    global lawnMowers,plants,sunPlants,dPlants,zombies,bullets,fallingsun
    global startTime,passTime,counting,progress,cursor,planting,shovelling
    global currShovel,whichplant,lcx,lcy,mx,my,lclick,sun,money,level
    global selection, cost, exploPlants
    scrollover(dayfull)
    selection=selectPlants()
    times=[clock() for i in range (6)]
    scrollback(dayfull)
    screen.blit(seedcart,(9,1))
    #selection of plant slots
    cost=[100,50,50,200,175,175,150]
    #button is in graphics.py
    for button in range(6):
        if selection[button]!="X":
            screen.blit(buttons[selection[button]],bar[button])

        
    filelevel=map(eval,open("level%d.txt"%clevel).read().strip().split("\n"))
    kindfreq=filelevel[-1]
    reset()

    mixer.music.stop()
    mixer.music.load("music/adventure.mp3")
    mixer.music.play(-1)
    
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
                if evt.button==3:
                    #zombie=["normal","cone","bucket","flag","newspaper","imp","chen","joker","door"]
                    #zombies.append(Zombie(5,randint(0,4),0,zSpd[5],zHP[5],zDmg[5],0,clock(),0,"living"))
                    zombies.append(Zombie(6,randint(0,4),0,zSpd[6],zHP[6],zDmg[6],0,clock(),0,"living"))
                    #zombies.append(Zombie(7,randint(0,4),0,zSpd[7],zHP[7],zDmg[7],0,clock(),0,"living"))
                    zombies.append(Zombie(8,randint(0,4),0,zSpd[8],zHP[8],zDmg[8],0,clock(),0,"living"))
                    zombies.append(Zombie(9,randint(0,4),0,zSpd[9],zHP[9],zDmg[9],0,clock(),0,"living"))
                    
        freq=[[0,0,0,1,1,2],[0,1,1,2,2,3],[1,1,2,2,3,4]]
        
        if counting==100:
            progress=0
        counting+=1
        if progress not in ["none","end"] and counting%800==0:
            addZombie("x",kindfreq[progress],freq[progress])
        if counting==filelevel[0]:
            progress=1
            addZombie(3,[],[1])
        if counting==filelevel[1]:
            progress=2
            addZombie(3,[],[1])
        if counting==filelevel[2]:
            progress="end"

        if progress=="end" and zombies==[]:
            money+=250
            level+=1
            if level==10:
                level=0
            out="adventure"
            
        mx,my=mouse.get_pos()

        invUpdateScreen()
        shovel()
        addSun()
        addBullets()
        addPlants()    
        moveStuff()

        if pauseRect.collidepoint(lcx,lcy):
            out=pause()
        if igMenuRect.collidepoint(lcx,lcy):
            out=igmenu()
                
        if cursor!="none":
            if 0<=mx-cursor.get_width()<=800 and 0<=my-cursor.get_height()/2<=800:
                screen.blit(cursor,(mx-cursor.get_width()/2,my-cursor.get_height()/2))

        display.flip()
        myClock.tick(100)
        screen.blit(copy,(0,0))
    return out

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
        states=[True,True,False,False,False,True,True,True,True,True]
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

        
#users will not be able to select the explosive plants or the last three plants
plantList=range(7)                    
def selectPlants():
    global choiceRects, selectbox
    selecting=True
    selection=["X"]*6
    while selecting:
        lcx,lcy=999,999
        for evt in event.get():
            if evt.type==QUIT:
                writeData()
                qa()
            if evt.type==MOUSEBUTTONDOWN:
                lcx,lcy=evt.pos
        screen.blit(seedcart,(0,0))
        screen.blit(selectbox,(0,85))
        for i in range (len(buttons)):
            screen.blit(buttons[i],choiceRects[i])
        for i in range (7):
            if choiceRects[i].collidepoint(mouse.get_pos()):
                draw.rect(screen,(255,255,0),choiceRects[i],1)
            if choiceRects[i].collidepoint((lcx,lcy)):
                if "X" in selection and i not in selection:
                    selection[selection.index("X")]=i
        for i in range (6):
            if bar[i].collidepoint(lcx,lcy) and selection[i]!="X":
                selection[i]="X"
            if selection[i]!="X":
                screen.blit(buttons[selection[i]],bar[i])
        if playRect.collidepoint((lcx,lcy)) and "X" not in selection:
            return selection
        display.flip()

def scrollover(img):
    sx=0
    while sx<600:
        for evt in event.get():
            if evt.type==QUIT:
                quit()
        screen.blit(img.subsurface(Rect(sx,0,800,600)),(0,0))
        display.flip()
        myClock.tick(100)
        sx+=5
        
def scrollback(img):
    sx=600
    while sx>214:
        for evt in event.get():
            if evt.type==QUIT:
                quit()
        screen.blit(img.subsurface(Rect(sx,0,800,600)),(0,0))
        display.flip()
        myClock.tick(100)
        sx-=5
#------End of Other Random Stuff------------

#-----Datafile------------------------
def getData(username):
    global topNum,topTypes,money,numPlants,zplants,numfert,numspray,level
    global alreadybought,sprouts
    data=map(eval,open(username+"All.txt").read().split("\n"))
    topNum,topTypes,money,numPlants=data[:4]
    zplants=data[4:4+numPlants]
    numfert,numspray,alreadybought=data[4+numPlants:7+numPlants]
    sprouts=data[7+numPlants:]
    del sprouts[-1]
    level=data[-1]
def writeData(username):
    outf=open(username+"All.txt","w")
    outf.write("%d\n"%topNum+str(topTypes)+"\n%d\n%d\n"%(money,len(zplants))+\
               "\n".join(map(str,zplants)))
    outf.write("\n%d\n%d\n%s\n"%(numfert,numspray,str(alreadybought)))
    outf.write("\n".join(map(printDate,sprouts))+"\n%d"%level)
    
    outf.close()
#-----End of Datafile-------------------

#-----Main---------------------------
getData(username)
pg="menu"
while pg!="quit":
    if pg=="menu":
        pg=menu()
    if pg=="help":
        pg=pvzhelp()
    if pg=="adventure":
        pg=adventure(level)
    if pg=="mini":
        pg=invisiGhoul(level)
    if pg=="almanac":
        almanac()
        pg="menu"
    if pg=="zen":
        pg=zenGarden(bg,username)
    if pg=="shop":
        pg=shop()
    display.flip()
writeData(username)
quit()
