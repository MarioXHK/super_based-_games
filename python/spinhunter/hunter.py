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
coins: int = 0

#sword variables-----------------------------------
sharpness = 1
swordpos = [512,256]
sharppos = [0,0]
angle = 0
am = 1 #Angular momentum

#enemy variables--------------------------------------
the = [enemy(0),enemy(0),enemy(0)]
mlvl: int = 1 #The level enemies should spawn at
sr: int = 300 #Spawn Rate. How many ticks until spawning another monster
timer = sr

#shop variables---------------------------------------
costs = [3,3,5,5]

#Texts
text1 = font.render('Coins:', False, (200,200,0))
text2 = font.render(str(coins), 1, (200,200,0))
text3 = font.render('Damage:', False, (200,0,0))
text4 = font.render(str(sharpness), 1, (200,0,0))
text5 = font.render('Speed:', False, (0,0,200))
text6 = font.render(str(am), 1, (0,0,200))

sign1 = font.render('Increase damage', False, (0,0,0))
sign2 = font.render('Increase Speed', False, (0,0,0))
sign3 = font.render('Buy a new Weapon', False, (0,0,0))
sign4 = font.render('Hunt stronger', False, (0,0,0))
sign4point5 = font.render('monsters', False, (0,0,0))
sign5 = font.render('New Game', False, (255,255,255))
sign6 = font.render('Save', False, (255,255,255))
sign7 = font.render('Load Game', False, (255,255,255))

uptxt1 = font.render(str(costs[0]), 1, (0,0,0))
uptxt2 = font.render(str(costs[1]), 1, (0,0,0))
uptxt3 = font.render(str(costs[2]), 1, (0,0,0))
uptxt4 = font.render(str(costs[3]), 1, (0,0,0))

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
        costs[0] = costs[0] * 1.1 + 1
    elif mousePos[0] >= 256 and mousePos[0] <= 512 and mousePos[1] >= 512 and fire and costs[1] <= coins:
        am += 0.1
        coins -= int(costs[1])
        costs[1] = costs[1] * 1.1 + 1
    elif mousePos[0] >= 512 and mousePos[0] <= 768 and mousePos[1] >= 512 and fire and costs[2] <= coins:
        sharpness += 2
        coins -= int(costs[2])
        costs[2] *= 2
    elif mousePos[0] >= 768 and mousePos[0] <= 1024 and mousePos[1] >= 512 and fire and costs[3] <= coins:
        mlvl += 1
        if sr > 10:
            sr -= 5
        coins -= int(costs[3])
        costs[3] *= 2.5
    elif mousePos[0] >= 0 and mousePos[0] <= 160 and mousePos[1] >= 448 and fire and mousePos[0] <= 512:
        #NEW GAME!
        print("Game Erased!")
        coins = 0
        angle = 0
        am = 1
        the = [enemy(0),enemy(0),enemy(0)]
        mlvl = 1
        sr = 300
        sharpness = 1
        timer = sr
        costs = [3,3,5,5]
    elif mousePos[0] >= 256 and mousePos[0] <= 416 and mousePos[1] >= 448 and fire and mousePos[1] <= 512:
        #SAVE GAME
        print("Game Saved!")
        data = [str(coins),str(am),str(sharpness),str(mlvl),str(sr),str(costs[0]),str(costs[1]),str(costs[2]),str(costs[3])]
        writing = ' '.join(data)
        myfile = open("save.txt", "w")
        myfile.write(writing)
        myfile.close()
    elif mousePos[0] >= 768 and mousePos[0] <= 928 and mousePos[1] >= 448 and fire and mousePos[1] <= 512:
        #LOAD GAME
        print("Game Loaded!")
        myfile = open("save.txt", "r")
        reading = myfile.read().split()
        coins = int(reading[0])
        am = float(reading[1])
        sharpness = float(reading[2])
        the = [enemy(1),enemy(1),enemy(1)]
        mlvl = int(reading[3])
        sr = int(reading[4])
        costs = [float(reading[5]),float(reading[6]),float(reading[7]),float(reading[8])]
        angle = 0
        timer = sr
        myfile.close()
    #Timer stuff---------------------------------------
    if timer <= 0:
        the.append(enemy(random.randint(1,mlvl)))
        if sr > 10 and random.randint(1,6) == 6:
            sr -= 1
        timer = sr+random.randint(0,120)
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
                if the[i].hp//2+1000//the[i].speed < 1:
                    coins += 1
                else:
                    coins += int(the[i].hp//2+1000//the[i].speed)
                del the[i]
    fire = False
    text2 = font.render(str(coins), 1, (200,200,0))
    text4 = font.render(str(sharpness), 1, (200,0,0))
    text8 = font.render(str(am), 1, (0,0,200))
    uptxt1 = font.render(str(costs[0]), 1, (0,0,0))
    uptxt2 = font.render(str(costs[1]), 1, (0,0,0))
    uptxt3 = font.render(str(costs[2]), 1, (0,0,0))
    uptxt4 = font.render(str(costs[3]), 1, (0,0,0))
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

    pygame.draw.rect(screen,(0,0,200),(0,448,160,64))
    pygame.draw.rect(screen,(0,0,200),(256,448,160,64))
    pygame.draw.rect(screen,(0,0,200),(768,448,160,64))

    screen.blit(text1,(10,10))
    screen.blit(text2,(250,10))
    screen.blit(text3,(10,50))
    screen.blit(text4,(250,50))
    screen.blit(text5,(10,100))
    screen.blit(text6,(250,100))

    screen.blit(sign1,(0,512))
    screen.blit(sign2,(256,512))
    screen.blit(sign3,(512,512))
    screen.blit(sign4,(768,512))
    screen.blit(sign4point5,(768,560))
    screen.blit(sign5,(0,448))
    screen.blit(sign6,(256,448))
    screen.blit(sign7,(768,448))

    screen.blit(uptxt1,(0,640))
    screen.blit(uptxt2,(256,640))
    screen.blit(uptxt3,(512,640))
    screen.blit(uptxt4,(768,640))
    pygame.display.flip()
pygame.quit()