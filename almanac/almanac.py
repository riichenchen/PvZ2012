### Drop the function into the general function section of main
### To call it, in the middle of another function, have a line
''' if almanacRect.collidepoint(lcx,lcy):
        almanac()'''
### It will pause, go to the almanac, then go straight back again. More of a
### pause than pause(). If the quitting doesn't work there, just change the
### writeData()//qa() part into simply checking=False.

def almanac():
    "Initiates the almanac feature"
    checking=True
    screen.blit(bg_almanac,(0,0))
    while checking:
        lcx,lcy=999,999
        for evt in event.get():
            if evt.type==QUIT:
                writeData(username)
                qa()
            elif evt.type==MOUSEBUTTONDOWN:
                lcx,lcy=evt.pos
        for r in range (10):
            if alRects[r].collidepoint(lcx,lcy):
                screen.blit(almanac[r],(450,80))
        if alDoneRect.collidepoint(lcx,lcy):
            checking=False
        display.flip()
        myClock.tick(100)
    return out

###Drop these bits in graphics. Put the actual pics in too.
bg_almanac=image.load("graphics/almanac.png").convert_alpha()
almanac=[image.load("graphics/almanac%d.png"%x).convert_alpha() \
         for x in range (10)]

###Drop these in rects:
alRects=[Rect(26,89,69,67),Rect(109,88,70,70),Rect(195,90,68,68),
         Rect(279,88,71,70),Rect(365,88,69,68),Rect(24,170,69,67),
         Rect(110,171,69,64),Rect(194,171,70,64),Rect(279,169,72,67),
         Rect(365,170,69,65)]
alDoneRect=Rect(679,569,81,18)
