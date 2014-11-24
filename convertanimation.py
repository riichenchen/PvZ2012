#chen's version
#Animation.py
from pygame import *
init()

pauseScr=[image.load("paused screen/paused%d.png"%i) for i in range (2,13)]
for i in range (len(pauseScr)):
    pauseScr[i]=pauseScr[i].convert_alpha()

zombie=[]

normal=[image.load("normal zombie/normalzombie%d.png"%i) for i in range (1,59)]
for i in range (len(normal)):
    normal[i]=normal[i].convert_alpha()
zombie.append(normal)
cone=[image.load("conehead zombie/conehead%d.png"%i for i in range (1,54))]
for i in range (len(cone)):
    cone[i]=cone[i].convert_alpha()
zombie.append(cone)
bucket=[image.load("buckethead zombie/buckethead%d.png"%i) for i in range (1,41)]
for i in range (len(bucket)):
    bucket[i]=bucket[i].convert_alpha()
zombie.append(bucket)
flag=[image.load("flag zombie/flagzombie%d.png"%i) for i in range (1,31)]
for i in range (len(flag)):
    flag[i]=flag[i].convert_alpha()
zombie.append(flag)




plant=[]
peashooter=[image.load("peashooter/peashooter%d.png"%i) for i in range (1,16)]
plant.append(peashooter)
for i in range (len(peashooter)):
    peashooter[i]=peashooter[i].convert_alpha()
sunflower=[image.load("sunflower/sunflower%d.png"%i) for i in range (2,24)]
for i in range (len(sunflower)):
    sunflower[i]=sunflower[i].convert_alpha()
plant.append(sunflower)
wallnut=[image.load("potato/potato%d.png"%i) for i in range (1,11)]
for i in range (len(wallnut)):
    wallnut[i]=wallnut[i].convert_alpha()
plant.append(wallnut)
repeater=[image.load("repeater/repeater%d.png"%i) for i in range (1,12)]
for i in range (len(repeater)):
    repeater[i]=repeater[i].convert_alpha()
plant.append(repeater)

bullet=[image.load("pea.png"),"x","x",image.load("pea.png")]
seeds=[image.load("seeds/seed%d.png"%i) for i in range (0,4)]
for i in range (len(seeds)):
    seeds[i]=seeds[i].convert_alpha()
states=[]

dyingnormal=[image.load("dying normal zombie/dyingzombie%d.png"%i) for i in range (1,31)]
for i in range (len(dyingnormal)):
    dyingnormal[i]=dyingnormal[i].convert_alpha()
states.append(dyingnormal)
dyingnormal2=[image.load("dying normal zombie 2/deadzombie%d.png"%i) for i in range(15,46)]
for i in range (len(dyingnormal2)):
    dyingnormal2[i]=dyingnormal2[i].convert_alpha()
states.append(dyingnormal2)
eatingnormal=[image.load("eating normal zombie/eatingnormalzombie%d.png"%i)\
              for i in range(1,29)]
for i in range (len(eatingnormal)):
    eatingnormal[i]=eatingnormal[i].convert_alpha()
states.append(eatingnormal)
