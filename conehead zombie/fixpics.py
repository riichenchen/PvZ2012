#fixpics.py
from glob import glob
from pygame import *

pics=glob("*.bmp")
box=Rect(586,220,173,157)
for i in range (len(pics)):
    curr=image.load(pics[i])
    image.save(curr.subsurface(box),"conehead%d.png"%(i+1))
print "done"
    
