import pygame

class lander:
    def __init__(self, landerx, landery, landvex, landvey):
        self.initial = (landerx, landery, landvex, landvey)
        self.x = landerx
        self.y = landery
        self.vx = landvex
        self.vy = landvey
        self.isOnGround = False
        self.RocketOn = False
        self.crashed = False
    def thrust(self,upwards = True, direction = True):
        if upwards:
            self.RocketOn = True
            self.vy -= 0.417/60
        elif direction:
            self.vx += 1/60
        else:
            self.vx -= 1/60
    def dust(self):
        self.RocketOn = False
    def reset(self):
        self.x = self.initial[0]
        self.y = self.initial[1]
        self.vx = self.initial[2]
        self.vy = self.initial[3]
        self.crashed = False
        self.isOnGround = False
    def physics(self, ground):
        if self.y < ground:
            self.isOnGround = False
        else:
            self.isOnGround = True
        if not (self.isOnGround or self.RocketOn):
            self.vy += 1.62/60
        if self.isOnGround:
            if abs(self.vy) > .5 or abs(self.vx) > .5:
                self.crashed = True
        else:
            self.x += self.vx
            self.y += self.vy
    def render(self, surf):
        if self.crashed:
            pygame.draw.circle(surf, (255,40,0), (350,500), 30)
        else:
            pygame.draw.rect(surf, (230,220,40), (320,480,40, 40))
            