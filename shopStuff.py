from pygame import *

#rects
itemRects=[Rect(416,221,58,73),Rect(494,225,52,69),Rect(567,224,53,69),
           Rect(641,222,53,72),Rect(368,318,52,79),Rect(442,315,52,84),
           Rect(512,313,58,82),Rect(585,318,70,79)]
sMainRect=Rect(368,516,134,71)
sMoneyRect=Rect(695,559,76,15)

#itemCosts
costs=[2500,2500,2500,10000,750,1000,15000,1000]

#graphics
bgShop=image.load("shop.png").convert_alpha()
soldoutSpr=image.load("soldout.png").convert_alpha()
