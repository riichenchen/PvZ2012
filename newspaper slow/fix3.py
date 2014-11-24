#fix3.py
'''This program is only to be used after the results from fix2 have been
photoshopped (i.e. All extra color erased and removed). It imports and crops
the .png images so that it is "centered" in the top-left corner'''

from glob import *
from pygame import *

newnpics=glob("*.png")
for i in range (len(newnpics)):
    curr=image.load(newnpics[i])
    fx=0
    x=0
    while True:
        for ny in range (curr.get_height()):
            if curr.get_at((x,ny)).a!=0:
                fx=x
                break
        if fx!=0:
            break
        x+=1

    image.save(curr.subsurface(fx,0,curr.get_width()-fx,curr.get_height())\
               ,"npslow%d.png"%(i+1))
print "done"
