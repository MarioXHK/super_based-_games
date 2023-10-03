import pygame
import random
from spiders import enemy
import math




#Required pygame things------------------------
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Invaders")
doExit=False
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#mouse variables--------------------------------
mousePos = (0,0)
fire = False
tap = True
coins = 0

#sword variables-----------------------------------
sharpness = 1
swordpos = [512,256]
sharppos = [0,0]
angle = 0
am = 1 #Angular momentum

text1 = font.render('Coins:', False, (200,200,0))
text2 = font.render(str(coins), 1, (200,200,0))
#enemy variables--------------------------------------
the = [enemy(0),enemy(0),enemy(0)]
mlvl = 1 #The level enemies should spawn at
sr = 200 #Spawn Rate. How many ticks until spawning another monster
timer = sr

#shop variables---------------------------------------
costs = [3,3,5,5]


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
    
    
    if mousePos[0] >= 0 and mousePos[0] <= 256 and mousePos[1] >= 512 and fire and costs[0] <= coins:
        sharpness += 0.1
        coins -= int(costs[0])
        costs[0] *= 1.5
    elif mousePos[0] >= 256 and mousePos[0] <= 512 and mousePos[1] >= 512 and fire and costs[1] <= coins:
        am += 1
        coins -= int(costs[1])
        costs[1] *= 1.5
    elif mousePos[0] >= 512 and mousePos[0] <= 768 and mousePos[1] >= 512 and fire and costs[2] <= coins:
        sharpness += 2
        coins -= int(costs[2])
        costs[2] *= 3.5
    elif mousePos[0] >= 768 and mousePos[0] <= 1024 and mousePos[1] >= 512 and fire and costs[3] <= coins:
        mlvl += 1
        coins -= int(costs[3])
        costs[3] *= 2.5
    
    
    
    
    #Timer stuff---------------------------------------
    if timer <= 0:
        the.append(enemy(random.randint(1,mlvl)))
        if sr > 30:
            sr -= 1
        timer = sr+random.randint(0,60)
    else:
        timer -= 1
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
                coins += the[i].hp//2+1000//the[i].speed
                del the[i]
    fire = False
    text2 = font.render(str(coins), 1, (200,200,0))
    #Render--------------------------------------------
    screen.fill((255,255,255))
    for j in range(len(the)):
        the[j].render(screen)
    pygame.draw.circle(screen,(127,0,255),swordpos,20)
    pygame.draw.circle(screen,(255,0,0),sharppos,10)
    pygame.draw.rect(screen,(200,0,0),(0,512,256,256))
    pygame.draw.rect(screen,(200,200,0),(256,512,256,256))
    pygame.draw.rect(screen,(0,200,0),(512,512,256,256))
    pygame.draw.rect(screen,(100,0,200),(768,512,256,256))
    screen.blit(text1,(10,10))
    screen.blit(text2,(250,10))
    pygame.display.flip()
pygame.quit()