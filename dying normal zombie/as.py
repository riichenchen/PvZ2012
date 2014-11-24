#fix2.py
'''This program imports the .png files from fix1.py and removes a specific bg
color. (Automated Magic Wand)'''
from glob import *
from pygame import *

init()
newpics=glob("*.png")
col=(19,147,27)                     #Adjust color here
tol=60                              #Change tolerances
count=0
for i in newpics:
    count+=1
    curr=image.load(i).convert(32,SRCALPHA)
    image.save(curr,"dyingzombie%d.png"%count)

print "done"
