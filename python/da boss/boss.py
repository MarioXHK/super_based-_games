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
        self.turntime = random.randint(120,600)
    def step(self, speed = 1):
        self.turntime -= 1
        
        #This will make Patra randomly turn every moment or so
        
        if self.turntime < 1:
            self.direction = random.randint(1,8)
            self.turntime = random.randint(120,600)
        if self.direction == 8 or self.direction == 1 or self.direction == 2:
            self.x += speed/60
        if self.direction == 2 or self.direction == 3 or self.direction == 4:
            self.y += speed/60
        if self.direction == 4 or self.direction == 5 or self.direction == 6:
            self.x -= speed/60
        if self.direction == 6 or self.direction == 7 or self.direction == 8:
            self.y -= speed/60
    def draw(self, scren):
        scren.blit(tea, (self.x, self.y))
class fireball:
    def __init__(self, following, off = 0):
        self.x = following.x
        self.y = following.y
        self.angle = off
    def step(self, following):
        self.angle += 1
        if self.angle > 360:
            self.angle -= 360
        
        radians = self.angle*180/3.14
        
        self.x = 100*math.cos(radians)+following.x
        self.y = 100*math.sin(radians)+following.y
    def draw(self,scren):
        scren.blit(fire, (self.x, self.y))