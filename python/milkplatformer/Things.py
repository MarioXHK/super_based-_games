from Collision import thing
import pygame
import random




#Entity!
class entity:
    def __init__(self, startx, starty, name = "nul"):
        self.type = name
        self.x = startx
        #Entity's X position
        self.y = starty
        #Entity's Y position
        self.vx = 0
        #Entity's Horizontal Velocity
        self.vy = 0
        #Entity's Vertical Velocity
        self.xsize = 40
        #Entity's Horizontal Size
        self.ysize = 40
        #Entity's Vertical Size
        self.held = False
        #If the entity is being held
        self.flang = False
        #If the enemy is flinged
        self.vulnerable = True
        #If the enemy can be flung at all
        self.slip = 0.5
        #How slippery the ground is
        self.defslip = self.slip
        #The default value for self.slip, cannot be changed
        self.MID = [[[]]]
        self.onGround = True
        self.wheeled = True
        self.steps = 5
        #How many loops to preform collision checks
        self.platform = False #Determines if it should act as a platform
        self.pdirections = [False,False,False,False]
        self.name = name
        if name == "cheese":
            self.xsize = 60
            self.ysize = 40
            self.vx = 3
        elif name == "slime":
            self.xsize = 50
            self.ysize = 60
            self.vx = 4
        elif name == "cherry":
            self.vx = 6
        elif name == "flyingplatform":
            self.platform = True
            self.pdirections = [True,False,False,False]
            self.vulnerable = False
            self.xsize = 120
            self.ysize = 40
            self.vy = 0
            self.fly = False
        elif name == "bluewall":
            self.platform = True
            self.pdirections = [True,True,True,True]
            self.vulnerable = False
            self.xsize = 80
            self.ysize = 80
        elif name == "fakeblock":
            self.platform = True
            self.vulnerable = False
            self.pdirections = [True,True,True,True]
            self.xsize = 120
            self.ysize = 120
    def getmap(self,idk):
        self.MID = idk
    def getinf(self):
        return (self.x,self.y,self.xsize,self.ysize)
    def fling(self,hard,direct):
        if self.vulnerable:
            self.flang = True
            r = random.randint(-10,10)
            f = abs(hard+r)
            if f == 0:
                f = 1
            self.vx = random.randint(1,f)
            self.vy = 0-(f-self.vx)
            if not direct:
                self.vx *= -1
    def beaplatform(self,playervars) -> list[bool]:
        override = [False,False,False,False]
        if thing.objcollision(playervars,[self.x-50,self.y-50,self.xsize+100,self.ysize+100],0):
            if self.pdirections[0] and playervars[0]>(self.x-playervars[2]) and playervars[0]<(self.x+self.xsize) and playervars[1]+playervars[3] >self.y and playervars[1]+playervars[3] <(self.y+self.ysize):
                override[0]=True
        return override
                
    def move(self):
        if self.held or self.flang:
            if self.flang:
                self.vy += 0.3
                self.x += self.vx
                self.y += self.vy
            return
        self.onGround = False
        #Gravity stuff
        if self.name == "flyingplatform":
            if self.fly:
                self.vy += 1
                if self.vy < 5:
                    self.fly = False
            else:
                self.vy -= 1
                if self.vy > -5:
                    self.fly = True
            self.y += self.vy
        elif self.name != "fakeblock":
            if not thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,0):
                self.vy += 1
            for i in range(self.steps):#Does physics steps times to be sure to not phase through anything.
                if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,0):#THE FLOOR
                    self.onGround = True
                    self.vy = 0
                    self.y = (int((self.y+self.ysize)/40))*40-self.ysize
                    if self.type == "cherry":
                        if (thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,2) or thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,3)):
                            self.vy -= 7
                if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,1):#Ceiling collision
                    self.vy = 0
                    self.y = (int((self.y)/40))*40+40
                    
                if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,2):#Wall left
                    self.x = (int((self.x+40)/40))*40
                    self.vx = 0-self.vx
                if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,3):#Wall right
                    self.x = (int((self.x+self.xsize)/40))*40-self.xsize
                    self.vx = 0-self.vx
                if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,5) == 1:#On surface edge
                    if self.type == "cheese":
                        self.vx = 0-self.vx
                    elif self.type == "cherry":
                        self.vy -= 7
                self.fasterDown = False
                self.x += self.vx/self.steps
                self.y += self.vy/self.steps
                #Makes the movement less controllable while in air
                if self.onGround:
                    self.slip = self.defslip
                else:
                    self.slip = self.defslip/3
    def draw(self, Screen, off, zoom = 1):
        color = (100, 100, 100)
        if self.type == "cheese":
            color = (200, 200, 100)
        elif self.type == "slime":
            color = (50, 200, 100)
        elif self.type == "cherry":
            color = (200, 75, 75)
        pygame.draw.rect(Screen, color, (self.x*zoom-off[0], self.y*zoom-off[1], self.xsize*zoom, self.ysize*zoom))