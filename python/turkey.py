import pygame #bring in pygame library
import random
pygame.init #initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800)) #create game screen
pygame.display.set_caption("A turkey!") #window title
turking = True
class turkey:
    def __init__(self, size, colorA, colorB, colorC, colorD):
        self.s = size
        self.color = (colorA, colorB, colorC, colorD)
        self.x = random.randint(0,800)
        self.y = -100 - size
        self.v = 0
    def rain(self):
        self.v += self.s/100
        self.y += self.v
        
        if self.y > 800 + self.s:
            self.y = -100 - self.s
            self.v = random.randint(0,10)
    def draw(self, scream):
        pygame.draw.circle(scream, self.color[3], (self.x+self.s*1.2, self.y), self.s*0.4)
        pygame.draw.circle(scream, self.color[3], (self.x-self.s*1.2, self.y), self.s*0.4)
        pygame.draw.circle(scream, self.color[2], (self.x+self.s*1.1, self.y-self.s*0.5), self.s*0.4)
        pygame.draw.circle(scream, self.color[2], (self.x-self.s*1.1, self.y-self.s*0.5), self.s*0.4)
        pygame.draw.circle(scream, self.color[3], (self.x+self.s*0.8, self.y-self.s*0.8), self.s*0.4)
        pygame.draw.circle(scream, self.color[3], (self.x-self.s*0.8, self.y-self.s*0.8), self.s*0.4)
        pygame.draw.circle(scream, self.color[2], (self.x+self.s*0.5, self.y-self.s*1.1), self.s*0.4)
        pygame.draw.circle(scream, self.color[2], (self.x-self.s*0.5, self.y-self.s*1.1), self.s*0.4)
        pygame.draw.circle(scream, self.color[3], (self.x, self.y-self.s*1.2), self.s*0.4)

        pygame.draw.circle(scream, self.color[0], (self.x, self.y), self.s)
        pygame.draw.ellipse(scream, self.color[0], (self.x-(self.s*0.4),self.y-(self.s*1.4),self.s*0.8,self.s*1.1))
        pygame.draw.ellipse(scream, (0,0,0), (self.x-(self.s*0.4),self.y-(self.s*1.4),self.s*0.8,self.s*1.1),1)
        
        pygame.draw.polygon(scream, self.color[1], ((self.x-(self.s/5), self.y-(self.s*1.2)),((self.x+(self.s/5), self.y-(self.s*1.2))),(self.x, self.y-(self.s*0.7))))
        
        pygame.draw.circle(scream, (255,255,255), (self.x-(self.s/5), self.y-(self.s*1.2)), self.s/7)
        pygame.draw.circle(scream, (255,255,255), (self.x+(self.s/5), self.y-(self.s*1.2)), self.s/7)
        pygame.draw.circle(scream, (0,0,0), (self.x-(self.s/5), self.y-(self.s*1.2)), self.s/10)
        pygame.draw.circle(scream, (0,0,0), (self.x+(self.s/5), self.y-(self.s*1.2)), self.s/10)
def randcolor() -> tuple[int]:
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

turks = []
for i in range(20):
    turks.append(turkey(random.randint(10,100),randcolor(),randcolor(),randcolor(),randcolor()))

turks = sorted(turks,key=lambda x: x.s)

while turking:
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            turking = False
    clock.tick(60)
    
    for i in range(len(turks)):
        turks[i].rain()
    
    #render

    screen.fill((0,0,0))
    
    for i in turks:
        i.draw(screen)

    pygame.display.flip() #update graphics
pygame.quit()