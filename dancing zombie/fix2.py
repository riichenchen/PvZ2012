#fix2.py
'''This program imports the .png files from fix1.py and removes a specific bg
color. (Automated Magic Wand)'''
from glob import *
from pygame import *

init()
newpics=glob("*.png")
col=(106,134,107)                     #Adjust color here
tol=20                             #Change tolerances
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
    image.save(curr,"dancingzombie%d.png"%count)

print "done"
