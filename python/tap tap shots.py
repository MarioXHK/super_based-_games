import pygame
import random
pygame.init()
pygame.display.set_caption("tap tap shots")
screen = pygame.display.set_mode((500,500))
screen.fill((0,0,0))
xpos = 250
ypos = 200
xvel = 150
yvel = 0
clock = pygame.time.Clock()
tap = True
gaming = True
hx = 400
hy = 150
score = 0
timer = 10000000
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render(str(score), False, (255,255,255))

while gaming:
    timer -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        if event.type == pygame.MOUSEBUTTONDOWN and tap and timer > 0:
            yvel = -400
            tap = False

        if event.type == pygame.MOUSEBUTTONUP:
            tap = True
    if timer <= 0:
        clock.tick(30)
    else:
        clock.tick(60)
    #physics
    if xpos > 550 and xvel > 0 :
        xpos -= 600
    if xpos < -50 and xvel < 0:
        xpos+=600
    
    isonground = False
    if ypos > 480:
        if not isonground:
            if yvel > 0:
                if abs(yvel) > 5:
                    yvel *= -0.8
                else:
                    yvel = 0
        isonground = True
        
    if not isonground:
        yvel += 10
    
    xpos += xvel/60
    ypos += yvel/60
    if xpos > hx and xpos < hx+100 and ypos > hy and ypos < hy+30 and yvel > 0:
        if hx == 400:
            hx = 0
        else:
            hx = 400
        hy = random.randint(150,400)
        xvel *= -1
        score += 1
        timer = 500

    #render------------------
    text1 = font.render(str(score), False, (255,255,255))
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (hx,hy,100,60))
    screen.blit(text1,(250,100))
    pygame.draw.circle(screen,(255,0,0),(xpos,ypos),20)
    pygame.display.flip()
    print(timer)
    if timer <= 0 and isonground:
        gaming = False
pygame.quit()
print("GAME OVER\nScore:", score)