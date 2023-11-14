import pygame
pygame.init()  
pygame.display.set_caption("Tree Test")  # sets the window title
screen = pygame.display.set_mode((800, 800))
screen.fill((0,0,0))
clock = pygame.time.Clock()
def inbetweenpoints(pointA: list[float],pointB: list[float],between: float):
    pointB[0] -= pointA[0]
    pointB[1] -= pointA[1]
    pointB[0] *= between
    pointB[1] *= between
    pointC = [(pointA[0]+pointB[0]),(pointA[1]+pointB[1])]
    return pointC
troll = 0
soup = 700
growing = True
while growing:
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            growing = False
    clock.tick(60)
    #Render the monstrosity
    screen.fill((0,0,0))
    if troll < 1:
        troll += 0.01
    else:
        troll = 0
        soup -= 5

    pygame.draw.circle(screen, (255,0,0), inbetweenpoints([200,200],[500,soup],troll), 10)

    pygame.draw.line(screen, (0,200,0),(200,200),(500,soup),10)
    pygame.draw.line(screen, (0,200,0),(200,soup),(500,200),10)
    pygame.display.flip()
pygame.quit()