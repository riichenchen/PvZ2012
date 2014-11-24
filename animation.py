#Animation.py
from pygame import *
init()

pauseScr=[image.load("paused screen/paused%d.png"%i) for i in range (2,13)]
for i in range (len(pauseScr)):
    pauseScr[i]=pauseScr[i].convert_alpha()

zombie=[]
#zombie=["normal","cone","bucket","flag","newspaper","imp","chen","joker","door","dancing"]

normal=[image.load("normal zombie/normalzombie%d.png"%i) for i in range (1,59)]
for i in range (len(normal)):
    normal[i]=normal[i].convert_alpha()
zombie.append(normal)
cone=[image.load("conehead zombie/conehead%d.png"%i) for i in range (1,54)]
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
newspaper=[image.load("newspaper slow/npslow%d.png"%i) for i in range(1,24)]
for i in range (len(newspaper)):
    newspaper[i]=newspaper[i].convert_alpha()
zombie.append(newspaper)
imp=[image.load("imp/imp%d.png"%i) for i in range(1,33)]
for i in range(len(imp)):
    imp[i]=imp[i].convert_alpha()
zombie.append(imp)
hungerzombie=[image.load("chen zombie/hungerzombie%d.png"%i) for i in range(1,41)]
for i in range(len(hungerzombie)):
    hungerzombie[i]=hungerzombie[i].convert_alpha()
zombie.append(hungerzombie)
joker=[image.load("joker/joker%d.png"%i) for i in range(1,32)]
for i in range(len(joker)):
    joker[i]=joker[i].convert_alpha()
zombie.append(joker)
door=[image.load("door zombie/doorzombie.png").convert_alpha()]
zombie.append(door)
dancing=[image.load("dancing zombie/dancingzombie%d.png"%i) for i in range(1,22)]
for i in range(len(dancing)):
    dancing[i]=dancing[i].convert_alpha()
zombie.append(dancing)
    


#plant=["peashooter","sunflower","wallnut","repeater","icepea","firepea","cherry",
#"squash","jalapeno"]
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
icepea=[image.load("ice pea/icepea%d.png"%i) for i in range(1,31)]
for i in range (len(icepea)):
    icepea[i]=icepea[i].convert_alpha()
plant.append(icepea)
firepea=[image.load("fire pea/firepea%d.png"%i) for i in range(1,31)]
for i in range(len(firepea)):
    firepea[i]=firepea[i].convert_alpha()
plant.append(firepea)
cherry=[image.load("cherry/cherrybomb%d.png"%i) for i in range(1,17)]
for i in range(len(cherry)):
    cherry[i]=cherry[i].convert_alpha()
plant.append(cherry)
squash=[image.load("squash/squash%d.png"%i) for i in range(1,10)]
for i in range(len(squash)):
    squash[i]=squash[i].convert_alpha()
plant.append(squash)
jalapeno=[image.load("jalapeno/jalapeno%d.png"%i) for i in range(1,13)]
for i in range(len(jalapeno)):
    jalapeno[i]=jalapeno[i].convert_alpha()
plant.append(jalapeno)

#plant=["peashooter","sunflower","wallnut","repeater","icepea","firepea","cherry",
#"squash","jalapeno"]
bullet=[image.load("pea.png"),"x","x",image.load("pea.png"),image.load("bluepea.png"),image.load("FirePea.png"),"x",
        "x","x","x"]

seeds=[image.load("seeds/seed%d.png"%i) for i in range (0,8)]
for i in range (len(seeds)):
    seeds[i]=seeds[i].convert_alpha()


condition=[]

#zombie=["normal","cone","bucket","flag"]
#condition=["dyingnormal","dyingnormal2","eatingnormal","eatingconehead","eatingbuckethead","eatingflag"/
#"eatingnewspaper","eatingchen","eatingjoker",eatingdancing]

dyingnormal=[image.load("dying normal zombie/dyingzombie%d.png"%i) for i in range (1,31)]
for i in range (len(dyingnormal)):
    dyingnormal[i]=dyingnormal[i].convert_alpha()
condition.append(dyingnormal)
dyingnormal2=[image.load("dying normal zombie 2/deadzombie%d.png"%i) for i in range(15,46)]
for i in range (len(dyingnormal2)):
    dyingnormal2[i]=dyingnormal2[i].convert_alpha()
condition.append(dyingnormal2)
eatingnormal=[image.load("eating normal zombie/eatingnormalzombie%d.png"%i)\
              for i in range(1,29)]
for i in range (len(eatingnormal)):
    eatingnormal[i]=eatingnormal[i].convert_alpha()
condition.append(eatingnormal)
eatingconehead=[image.load("eating cone head/eatingconehead%d.png"%i) for i in range(1,29)]
for i in range(len(eatingconehead)):
    eatingconehead[i]=eatingconehead[i].convert_alpha()
condition.append(eatingconehead)
eatingbuckethead=[image.load("eating bucket head/eatingbuckethead%d.png"%i) for i in range(1,29)]
for i in range(len(eatingbuckethead)):
    eatingbuckethead[i]=eatingbuckethead[i].convert_alpha()
condition.append(eatingbuckethead)
eatingflag=[image.load("eating flag/eatingflag%d.png"%i) for i in range(1,29)]
for i in range(len(eatingflag)):
    eatingflag[i]=eatingflag[i].convert_alpha()
condition.append(eatingflag)
eatingnewspaper=[image.load("eating newspaper/eatingnewspaper%d.png"%i) for i in range(1,29)]
for i in range(len(eatingnewspaper)):
    eatingnewspaper[i]=eatingnewspaper[i].convert_alpha()
condition.append(eatingnewspaper)
eatingimp=[image.load("eating imp/1eatingimpd%d.png"%i) for i in range(4,32)]
for i in range(len(eatingimp)):
    eatingimp[i]=eatingimp[i].convert_alpha()
condition.append(eatingimp)
eatingchenzombie=[image.load("eating chen zombie/eatingchen%d.png"%i) for i in range(1,29)]
for i in range(len(eatingchenzombie)):
    eatingchenzombie[i]=eatingchenzombie[i].convert_alpha()
condition.append(eatingchenzombie)
eatingjoker=[image.load("eating joker/eatingjoker%d.png"%i) for i in range(1,29)]
for i in range(len(eatingjoker)):
    eatingjoker[i]=eatingjoker[i].convert_alpha()
condition.append(eatingjoker)
eatingdoor=[image.load("eating door zombie/eatingdoor%d.png"%i) for i in range(1,29)]
for i in range(len(eatingdoor)):
    eatingdoor[i]=eatingdoor[i].convert_alpha()
condition.append(eatingdoor)
eatingdancing=[image.load("eating dancing zombie/eatingdancing%d.png"%i) for i in range(1,29)]
for i in range(len(eatingdancing)):
    eatingdancing[i]=eatingdancing[i].convert_alpha()
condition.append(eatingdancing)



