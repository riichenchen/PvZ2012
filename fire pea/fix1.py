#fix1.py
'''This program takes in .bmp screenshots from AnimGet and processes the images:
Crops to a specified Rect, renames, and converts to .png'''
from glob import glob
from pygame import *

pics=glob("*.png")
pics.sort()
box=Rect(586,220,173,157)           #Make changes here
for i in range (len(pics)):
    curr=image.load(pics[i])
    image.save(curr,"firepea%d.png"%(i+1))     #And here

print "done"
