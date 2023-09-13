import pygame
import random
import math

tea = pygame.image.load('boss_img.png')
fire = pygame.image.load('fire.png')
class patra:
    def __init__(self,sx,sy):
        self.x = sx
        self.y = sy
        self.direction = random.randint(1,8)
        self.turntime = random.randint(30,300)
    def step(self, speed = 1):
        self.turntime -= 1
        
        #This will make Patra randomly turn every moment or so
        
        if self.turntime < 1:
            self.direction = random.randint(1,8)
            self.turntime = random.randint(30,300)
        if self.direction == 8 or self.direction == 1 or self.direction == 2:
            self.x += speed/2
        if self.direction == 2 or self.direction == 3 or self.direction == 4:
            self.y += speed/2
        if self.direction == 4 or self.direction == 5 or self.direction == 6:
            self.x -= speed/2
        if self.direction == 6 or self.direction == 7 or self.direction == 8:
            self.y -= speed/2
    def draw(self, scren):
        scren.blit(tea, (self.x, self.y))

#FIREBALL CLASS! THE SPINNY THING!

class fireball:
    def __init__(self, following, off = 0):
        self.x = following.x
        self.y = following.y
        self.angle = off
    def step(self, following, what):
        self.angle += 1/1080
        
        radians = self.angle*what/3.14
        
        self.x = 100*math.cos(radians)+following.x
        self.y = 100*math.sin(radians)+following.y
    def draw(self,scren):
        scren.blit(fire, (self.x, self.y))