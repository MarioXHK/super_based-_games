import pygame
import boss
pygame.init()
clock = pygame.time.Clock()#set up clock
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Boss Test")
youknowwho = boss.patra(250,250)
fire = []
balls = 16
for i in range(balls):
    j = i/balls-1/balls
    fire.append(boss.fireball(youknowwho,j))
gaming = True
thing = 0
style = 12
stylevarA = 1
stylevarB = 0





while gaming:
    thing += 1/10
    for event in pygame.event.get(): #Event queue
        if event.type == pygame.QUIT:
            gaming = False
    clock.tick(60)
    youknowwho.step(1)
    if False:
        if thing > 136:
            style = 2
        elif thing > 60:
            style = 1
        elif thing > 40:
            style = 2
        elif thing > 20:
            style = 0
    
    #styles of fire
    for i in range(len(fire)):
        if style == 0: # Style 0: do nothing, become normal
            stylevarA = 0
            stylevarB = 0
            fire[i].tx = 0
            fire[i].ty = 0
            fire[i].sx = 100
            fire[i].sy = 100
            fire[i].step(youknowwho)
        elif style == 1: # Style 1: do the cool swaying
            fire[i].tx = thing/2
            if stylevarA == 1:
                fire[i].sy -= 1
                if fire[i].sy <= -100:
                    stylevarA = 2
            elif stylevarA == 2:
                fire[i].sy += 1
                if fire[i].sy >= 100:
                    stylevarA = 0
                    stylevarB = 1
            if stylevarB == 1:
                fire[i].sx -= 1
                if fire[i].sx <= -100:
                    stylevarB = 2
            elif stylevarB == 2:
                fire[i].sx += 1
                if fire[i].sx >= 100:
                    stylevarA = 1
                    stylevarB = 0
            fire[i].step(youknowwho)
        elif style == 2: # Style 2: 3 orbiting 2
            if i % 4 == 0:
                fire[i].step(youknowwho)
                stylevarB = i
            else:
                fire[i].am = 3/(len(fire)//4)
                fire[i].sx = 50
                fire[i].sy = 50
                fire[i].what = 25 * (len(fire)//4)
                    
                fire[i].step(fire[stylevarB])
        elif style == 3: # Style 3: Mario Firebar
            if stylevarB < len(fire):
                stylevarB += 1
                fire[i].angle = 0
                fire[i].sx = 20*i+20
                fire[i].sy = 20*i+20
            fire[i].step(youknowwho)
        elif style == 4: # Style 4: The Cooler Mario Firebar
            if stylevarB < len(fire):
                stylevarB += 1
                fire[i].angle = 0
                fire[i].what = thing*i*10-20
                fire[i].sx = 20*i+20
                fire[i].sy = 20*i+20
            fire[i].step(youknowwho)
        elif style == 5: #Style 5: Wings
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fire[i].angle = 1/2
                    fire[i].am = 1
                    fire[i].what = (thing)*(i//2)*10-20
                else:
                    fire[i].angle = 0
                    fire[i].am = -1
                    fire[i].what = (0-thing)*(i//2)*10+20
                fire[i].sx = (i//2)*30+30
                fire[i].sy = (i//2)*30+30
            fire[i].step(youknowwho)
        elif style == 6: # Style 6: Cool Swirl (Accident)
            if stylevarB < len(fire):
                if stylevarB < len(fire)/2:
                    stylevarB += 1
                    fire[i].sx = len(fire)*10-(i*20)
                    fire[i].sy = i*20
                else:
                    fire[i].sx = i*20
                    fire[i].sy = len(fire)*10-(i*20)
            fire[i].step(youknowwho)
        elif style == 7: # Style 7: Some other cool swirls (Also an Accident)
            if stylevarB < len(fire):
                fire[i].am = 2
                stylevarB += 1
                if stylevarB < len(fire)/2:
                    if i % 2 == 1:
                        fire[i].sy = i*20
                    else:
                        fire[i].sy = i*-20
                else:
                    fire[i].sy = fire[len(fire)-i].sy
            fire[i].step(youknowwho)
        elif style == 8: # Style 8: Have half of the balls orbit counterclock wise
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fire[i].am = 0-fire[i].am
            fire[i].step(youknowwho)
        elif style == 9: # Style 9: Revolving Horizontally
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fire[i].sx = -100
            else:
                fire[i].tx = thing/2
                if stylevarA == 1:
                    if i % 2 == 1:
                        fire[i].sx -= 1
                    else:
                        fire[i].sx += 1
                        if fire[i].sx <= -100:
                            stylevarA = 2
                elif stylevarA == 2:
                    if i % 2 == 1:
                        fire[i].sx += 1
                        
                    else:
                        fire[i].sx -= 1
                        if fire[i].sx >= 100:
                            stylevarA = 1
            fire[i].step(youknowwho)
        elif style == 10: # Style 10: Revolving Vertically
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fire[i].sy = -100
            else:
                fire[i].tx = thing/2
                if stylevarA == 1:
                    if i % 2 == 1:
                        fire[i].sy -= 1
                        
                    else:
                        fire[i].sy += 1
                        if fire[i].sy >= 100:
                            stylevarA = 2
                elif stylevarA == 2:
                    if i % 2 == 1:
                        fire[i].sy += 1
                        
                    else:
                        fire[i].sy -= 1
                        if fire[i].sy <= -100:
                            stylevarA = 1
        elif style == 11: # Style 11: In and Out
            if fire[i].sx > 0:
                stylevarB -= 0.01
            else:
                stylevarB += 0.01
            fire[i].sx += stylevarB
            fire[i].sy += stylevarB
            if fire[i].sx > 150:
                fire[i].sx = 150
                fire[i].sy = 150
                stylevarB = 0
            elif fire[i].sx < -150:
                fire[i].sx = -150
                fire[i].sy = -150
                stylevarB = 0
            fire[i].step(youknowwho)
        elif style == 12: # Style 12: E G G
            if fire[i].y < youknowwho.y:
                fire[i].sy = 150
            else:
                fire[i].sy = 75
            fire[i].step(youknowwho)
    screen.fill((200,200,200))
    youknowwho.draw(screen)
    for i in range(len(fire)):
        fire[i].draw(screen)
    pygame.display.flip()
pygame.quit()