import pygame
from interest import creature
from interest import move

pygame.init()  
pygame.display.set_caption("Animals Fighting")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0,0,0))
clock = pygame.time.Clock()


tackle = move(40)
testers = [creature(0,5),creature(1,5),creature(2,5)]


testers[0].printInfo()
#testers[1].printInfo()
#testers[2].printInfo()

testers[0].printBattleInfo()
testers[0].tempstats[0] -= testers[1].attack(testers[0],tackle)


testers[0].printBattleInfo()

surviving = True
while surviving:
    #The input you have
    for event in pygame.event.get(): #Event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            surviving = False
    clock.tick(60)
    
    
    #Rendering is what I do!
    screen.fill((2,20,200))
    



    pygame.draw.polygon(screen, (0,200,0),((600,900), (400,900), (400,700), (600,700)))
    pygame.display.flip()
pygame.quit()