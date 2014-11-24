from pygame import *
bg_day=image.load("Frontyard play.jpg").convert_alpha()

menupg=image.load("main screen/main.png").convert_alpha()
menubuttons=image.load("main screen/main buttons.png").convert_alpha()
helppg=image.load("graphics/help.png").convert_alpha()
dayfull=image.load("Frontyard.jpg").convert_alpha()

nightfull=image.load("Nightfrontyard.jpg").convert_alpha()
sunSpr=image.load("graphics/sun.png").convert_alpha()
lawnSpr=image.load("graphics/Lawn_Mower.png").convert_alpha()
lawnWSpr=image.load("graphics/lawn_mower_waiting.png").convert_alpha()
shovelFull=image.load("graphics/shovel.jpg").convert_alpha()
shovelEmpty=image.load("graphics/shovelEmpty.png").convert_alpha()
shovelCursor=image.load("graphics/ShovelCursor.png").convert_alpha()
pausebutton=image.load("graphics/pause button.png").convert_alpha()
menubutton=image.load("graphics/menu button.png").convert_alpha()
buttons=[image.load("seeds/seed%d.png"%i).convert_alpha() for i in range (9)]
seedcart=image.load("graphics/seedcart.png").convert_alpha()
bg_day=image.load("Frontyard play.jpg").convert_alpha()
selectbox=image.load("graphics/selectbox.png").convert_alpha()

igMenu=image.load("graphics/igmenu.png").convert_alpha()

bg_almanac=image.load("graphics/almanac.png").convert_alpha()
almanacs=[image.load("graphics/almanac%d.png"%x).convert_alpha() \
         for x in range (10)]
