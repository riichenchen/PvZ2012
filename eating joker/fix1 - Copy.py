#fix1.py
'''This program takes in .bmp screenshots from AnimGet and processes the images:
Crops to a specified Rect, renames, and converts to .png'''
from glob import glob
from pygame import *

pics=glob("*.png")
box=Rect(98,41,123,156)           #Make changes here
for i in range (len(pics)):
    curr=image.load(pics[i])
    image.save(curr.subsurface(box),"1eatingjoker%d.png"%(i+1))     #And here

print "done"
