import pygame
import random
from spiders import enemy
import math

#Required pygame things------------------------
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Space Invaders")
doExit=False
clock = pygame.time.Clock()


#mouse variables--------------------------------
mousePos = (0,0)
fire = False
tap = True

#sword variables-----------------------------------
sharpness = 1
swordpos = [512,384]
sharppos = [0,0]
angle = 0
am = 1 #Angular momentum

#enemy variables--------------------------------------
the = [enemy(1),enemy(1),enemy(1)]
mlvl = 1 #The level enemies should spawn at
sr = 10 #Spawn Rate. The overall chance of an enemy appearing out of the blue out of 10000
while not doExit:
    clock.tick(60)
    #Input--------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
        if event.type == pygame.MOUSEBUTTONDOWN and tap:
            fire = True
            tap = False
        if event.type == pygame.MOUSEBUTTONUP:
            tap = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    #Random stuff---------------------------------------
    if random.randint(sr,200) == 200:
        the.append(enemy(random.randint(1,mlvl)))
    #Sword movement------------------------------------
    angle += am/360
            
    radians = angle*20/3.14
    
    sharppos[0] = 25*math.cos(radians)+swordpos[0]
    sharppos[1] = 25*math.sin(radians)+swordpos[1]
    
    #Physics-------------------------------------------
    for i in range(len(the)):
        if i < len(the):
            the[i].step(swordpos,sharppos,mousePos,fire,sharpness)
            if the[i].hp <= 0 or the[i].x > 1200 or the[i].x < -100 or the[i].y > 800 or the[i].y < -50:
                del the[i]
    fire = False
    #Render--------------------------------------------
    screen.fill((0,0,0))
    for j in range(len(the)):
        the[j].render(screen)
    pygame.draw.circle(screen,(127,0,255),swordpos,20)
    pygame.draw.circle(screen,(255,0,0),sharppos,10)

    pygame.display.flip()
    


pygame.quit()