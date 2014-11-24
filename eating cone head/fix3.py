#fix3.py
'''This program is only to be used after the results from fix2 have been
photoshopped (i.e. All extra color erased and removed). It imports and crops
the .png images so that it is "centered" in the top-left corner'''

from glob import *
from pygame import *

newnpics=glob("*.png")
for i in range (len(newnpics)):
    curr=image.load(newnpics[i])
    fx,fy=0,0
    x,y=0,0
    while True:
        for ny in range (curr.get_height()):
            if curr.get_at((x,ny)).a!=0:
                fx=x
        if fx!=0:
            break
        x+=1
    while True:
        for nx in range (curr.get_width()):
            if curr.get_at((x,y)).a!=0:
                fy=y
        if fy!=0:
            break
        x+=y 
    image.save(curr.subsurface(fx,fy,curr.get_width()-fx,curr.get_height()-fy)\
               ,"eatingconehead%d.png"%i)
print "done"
