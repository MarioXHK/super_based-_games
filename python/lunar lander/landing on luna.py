#pygame is a bunch of pre-written python code that makes coding games easier
import pygame
import random
from Lander import lander
pygame.init()

#this sets where  the game screen will be
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)

#creates a game screen and caption
screen = pygame.display.set_mode((700, 1000))
pygame.display.set_caption("Lunar Lander Simulator")

#game variables
doExit = False #Variable to quite out of game loop
clock = pygame.time.Clock() #Sets up a game clock to regulate game speed

landers = [lander(350,0,0,5)]
groundy = 8000

#font variables: lets us write text to the game screen
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('Vertical velocity:', False, (0,200,200))
text2 = font.render(str(landers[0].vy), 1, (0,200,200))
text3 = font.render('YOU CRASHED!', False, (200, 50, 50))
text4 = font.render('Vertical velocity:', False, (200,20,20))
text5 = font.render(str(landers[0].vy), 1, (200,20,20))
text6 = font.render('Height:', False, (20,20,200))
text7 = font.render(str(landers[0].y), 1, (20,20,200))
text8 = font.render('Horizontal velocity:', False, (0,200,200))
text9 = font.render(str(landers[0].vx), 1, (0,200,200))
text0 = font.render('Horizontal velocity:', False, (200,20,20))
text10 = font.render(str(landers[0].vx), 1, (200,20,20))
stars = []
for i in range(int(groundy/4)):
    stars.append((random.randrange(-10000,10000),random.randrange(-1000,groundy+500),random.randrange(5,20)))
farstars = []
for i in range(groundy):
    farstars.append((random.randrange(-10000,10000),random.randrange(-1000,groundy+500),random.randrange(5)))
print(stars)
keys = [False, False, False]



while doExit == False:
    clock.tick(60)
    
    for event in pygame.event.get(): #Event queue
        if event.type == pygame.QUIT:
            doExit = True
        
        #Input!
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[0] = True
            if event.key == pygame.K_RIGHT:
                keys[1] = True
            if event.key == pygame.K_UP:
                keys[2] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0] = False
            if event.key == pygame.K_RIGHT:
                keys[1] = False
            if event.key == pygame.K_UP:
                keys[2] = False
    if keys[0]:
        landers[0].thrust(False, False)
    if keys[1]:
        landers[0].thrust(False, True)
    if keys[2]:
        landers[0].thrust()
    else:
        landers[0].dust()
    landers[0].physics(groundy)
    
    #updates printed velocity
    text2 = font.render(str(landers[0].vy), 1, (0,200,200))
    text5 = font.render(str(landers[0].vy), 1, (200,20,20))
    text9 = font.render(str(landers[0].vx), 1, (0,200,200))
    text10 = font.render(str(landers[0].vx), 1, (200,20,20))
    
    #update printed height
    text6 = font.render('Height:', False, (20,20,200))
    text7 = font.render(str(groundy-landers[0].y), 1, (20,20,200))
    
    
    
    #RENDER!
    screen.fill((0,0,0))
    
    #Draws the stars!
    for i in stars:
        rotox = landers[0].x/5
        rotoy = landers[0].y/5
        pygame.draw.polygon(screen, (255,255,255), ((i[0]+i[2]-rotox,i[1]-rotoy),(i[0]-rotox,i[1]+i[2]-rotoy),(i[0]-i[2]-rotox,i[1]-rotoy),(i[0]-rotox,i[1]-i[2]-rotoy)))
    for i in farstars:
        rotox = landers[0].x/10
        rotoy = landers[0].y/10
        pygame.draw.polygon(screen, (255,255,255), ((i[0]+i[2]-rotox,i[1]-rotoy),(i[0]-rotox,i[1]+i[2]-rotoy),(i[0]-i[2]-rotox,i[1]-rotoy),(i[0]-rotox,i[1]-i[2]-rotoy)))
    
    #Drawing the ground and lander!
        
    pygame.draw.rect(screen, (222,222,232), (0, groundy-landers[0].y+500,1000, 1000))
    landers[0].render(screen)
    
    #draw velocity to screen
    if abs(landers[0].vy) < .5: #draw green
        screen.blit(text1,(10,10))
        screen.blit(text2,(250,10))
    else:
        screen.blit(text4,(10,10))
        screen.blit(text5,(250,10))
    if abs(landers[0].vx) < .5:
        screen.blit(text8,(10,100))
        screen.blit(text9,(300,100))
    else:
        screen.blit(text0,(10,100))
        screen.blit(text10,(300,100))
    
    screen.blit(text6,(10,60))
    screen.blit(text7,(150,60))
    
    
    if landers[0].isOnGround:
        if landers[0].crashed:
            screen.blit(text3, (200,500))
            pygame.display.flip()
        pygame.time.wait(1000)
        landers[0].reset()
    pygame.display.flip()
pygame.quit()