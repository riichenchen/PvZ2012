from pygame import *
coins=[image.load("silver.png").convert_alpha(),image.load("gold.png").convert_alpha(),
       image.load("diamond.png").convert_alpha()]
coinVals=[10,50,1000]

pot=image.load("flowerpot.png").convert_alpha()

stuff=[image.load("watering can.png").convert_alpha(),image.load("fertilizer.png").convert_alpha(),
       image.load("bug spray.png").convert_alpha(),image.load("phonograph.png").convert_alpha()]

top=[image.load("top%d.png"%i).convert_alpha() for i in range (1,9)]

zcursors=[image.load("cursor%d.png"%i).convert_alpha() for i in range (4)]

states=[image.load("state%d.png"%i).convert_alpha() for i in range (5)]
