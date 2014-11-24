from pygame import *
plant=[[image.load("peashooter/peashooter%d.png"%i) for i in range (1,16)],
       [image.load("sunflower/sunflower%d.png"%i) for i in range (2,24)],
       [image.load("potato/potato%d.png"%i) for i in range (1,11)],
       [image.load("repeater/repeater%d.png"%i) for i in range (1,12)]]

coins=[image.load("silver.png"),image.load("gold.png"),
       image.load("diamond.png")]
coinVals=[10,50,1000]

pot=image.load("flowerpot.png")

stuff=[image.load("watering can.png"),image.load("fertilizer.png"),
       image.load("bug spray.png"),image.load("phonograph.png")]

top=[image.load("top%d.png"%i) for i in range (1,9)]

zcursors=[image.load("cursor%d.png"%i) for i in range (4)]

states=[image.load("state%d.png"%i) for i in range (5)]
