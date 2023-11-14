import pygame
pygame.init()  
pygame.display.set_caption("Trees")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0,0,0))
initSquarePos = [400,850]

def inbetweenpoints(pointA: list[float],pointB: list[float],between: float):
    pointB[0] -= pointA[0]
    pointB[1] -= pointA[1]
    pointB[0] *= between
    pointB[1] *= between
    pointC = [(pointA[0]+pointB[0]),(pointA[1]+pointB[1])]

def pythagorean(a: float,b: float) -> float:
    return (a*a+b*b)**0.5

#[0][0] [1][1]                [1][0] [1][1]
#
#
#[0][0] [0][1]                [1][0] [0][1]

def boringTree(Screen: pygame.Surface, points: list[list], iter: int, tripoint: tuple[float] = (1,1), pos = tuple[float]):
    pygame.draw.polygon(Screen, (0,200,0),((points[0][0]+pos[0],points[0][1]+pos[1]), ((points[1][0])+pos[0],points[0][1]+pos[1]), ((points[1][0])+pos[0],(points[1][1])+pos[1]), (points[1][0]+pos[0],points[0][1]+pos[1])))
    if iter > 0:
        savepoints = points


        betweens = [inbetweenpoints((points[0][0],points[1][1]),(points[0][0],points[1][1]),tripoint[1])]

        
        points[0][1] = savepoints[1][1]
        boringTree()
        points[0][0] = savepoints[1][0]
        points[0][1] = savepoints[1][1]
        boringTree()



growing = True
while growing:
    #The little input you have
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            growing = False

    #Render the monstrosity
    screen.fill((0,0,0))




    pygame.draw.polygon(screen, (0,200,0),((600,900), (400,900), (400,700), (600,700)))
    pygame.display.flip()
pygame.quit()