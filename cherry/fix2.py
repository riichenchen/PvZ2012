#fix2.py
'''This program imports the .png files from fix1.py and removes a specific bg
color. (Automated Magic Wand)'''
from glob import *
from pygame import *

init()
newpics=glob("*.png")
col=(255,228,96)                    #Adjust color here
'''
(202,211,70)
(2,164,26)
(3,82,17)
(1,136,18)
(23,209,83)
(196,153,32) 
'''
tol=50                              #Change tolerances
count=0
for i in newpics:
    count+=1
    crop=0
    curr=image.load(i).convert(32,SRCALPHA)
    for x in range (curr.get_width()):
        for y in range (curr.get_height()):
            c=curr.get_at((x,y))
            if col[0]-tol<c[0]<col[0]+tol:
                if col[1]-tol<c[1]<col[1]+tol:
                    if col[2]-tol<c[2]<col[2]+tol:
                        curr.set_at((x,y),(0,0,0,0))
    image.save(curr,"eatingflag%d.png"%count)

print "done"
