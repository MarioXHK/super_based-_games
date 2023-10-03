import random
import pygame

spider = [pygame.image.load(".png"),pygame.image.load("bad_bee.png"),pygame.image.load("firespire.png"),pygame.image.load("yellow.png"),pygame.image.load("bobx.png"),pygame.image.load("shape_bros.png")]
IUEAFDHJBLSDFGAKJBL = pygame.image.load("=(.png")

class enemy:
    def __init__(self, monsternumber: int, speed: float = 500):
        det = random.randint(0,3) #0 = North, 1 = East. Never Eat Soggy Waffles
        if det == 0 or det == 2:
            self.x = float(random.randint(0,1024))
            if det == 0:
                self.y = 0
            else:
                self.y = 512
        elif det == 1 or det == 3:
            self.y = float(random.randint(0,512))
            if det == 3:
                self.x = 0
            else:
                self.x = 1024
        self.mn = monsternumber
        
        self.px = self.x
        self.py = self.y
        if monsternumber == 1:
            self.hp = 5
            self.speed = 800
        elif monsternumber == 2:
            self.hp = 3
            self.speed = 300
        elif monsternumber == 3:
            self.hp = 8
            self.speed = 1000
        elif monsternumber == 4:
            self.hp = 12
            self.speed = 1200
        elif monsternumber == 5:
            self.hp = 10
            self.speed = 900
        elif monsternumber == 6:
            self.hp = 1
            self.speed = 60
        elif monsternumber == 7:
            self.hp = 7
            self.speed = 900
        elif monsternumber == 8:
            self.hp = 9
            self.speed = 900
        elif monsternumber == 9:
            self.hp = 11
            self.speed = 800
        elif monsternumber == 10:
            self.hp = 30
            self.speed = 1500
        else:
            self.hp = 1
            self.speed = 1500
    def step(self, target: list[float],sword: list[float],click: tuple[float],tap: bool, strength: float):
        ox = self.px-target[0]
        oy = self.py-target[1]
        # The higher the speed number, the slower
        self.x -= ox/self.speed
        self.y -= oy/self.speed
        if click[0] >= self.x-20 and click[0] <= self.x+20 and click[1] >= self.y-20 and click[1] <= self.y+20 and tap:
            self.hp -= strength
            print("You deal", strength, "damage!")
        if sword[0] >= self.x-20 and sword[0] <= self.x+20 and sword[1] >= self.y-20 and sword[1] <= self.y+20:
            self.hp -= strength/5
        if self.hp <= 0:
            print("Enemy defeated!")
    def render(self,projector):
        if self.mn < 0:
            projector.blit(IUEAFDHJBLSDFGAKJBL, (self.x-32,self.y-32))
        else:
            projector.blit(spider[self.mn], (self.x-32,self.y-32))