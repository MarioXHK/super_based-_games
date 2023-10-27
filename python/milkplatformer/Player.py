from Collision import thing
import pygame
playeridle = pygame.image.load('player/idle.png')
playerduck = pygame.image.load('player/duck.png')
playertired = pygame.image.load('player/tired.png')
def rescale(imag):
    return pygame.transform.scale(imag, (80,80))
playerduck = rescale(playerduck)
playertired = pygame.transform.scale(playertired, (64,1216))
playeridle = pygame.transform.scale(playeridle, (64,1088))
class player:#THE PLAYER OF THE GAME
    def __init__(self, startx, starty, name = "nul"):
        self.name = name
        self.x = startx
        #Player's X position
        self.y = starty
        #Player's Y position
        self.xsize = 40
        #Player's Horizontal Size
        self.ysize = 60
        #Player's Vertical Size
        self.vx = 0
        #Player's Horizontal Velocity
        self.vy = 0
        #Player's Vertical Velocity
        self.rx = self.x
        self.ry = self.y
        #Player's Render Positions (used for offset)
        
        self.ox = 0
        self.oy = 0
        #The offset for the previous
        
        self.touchedGround = True
        #If the player has touched the ground (only turns false after the punch function)
        self.bump = 0
        #Cancel moving timer
        
        self.punchcd = 0
        #Punch timer
        
        self.controlling = False
        #If the player is being controlled
        
        self.pound = False
        #If the player is in a state to knock enemies out
        
        self.groundpound = False
        #If the player should continue to be dangerous in the air
        
        self.slip = 0.5
        #How slippery the ground is
        
        self.defslip = self.slip
        #The default value for self.slip, cannot be changed
        
        self.lastDone = False
        #The last movement done
        
        self.fasterDown = False
        #If the player lets go of jump soon
        
        self.maxrun = 4
        #How fast can the player run
        
        self.MID = [[[]]]
        #Place to hold map
        
        self.idc = 2
        #How much the player's max speed can really do
        
        self.vmod = 5
        #How fast can the player run's modifier
        
        self.wheeled = True
        #FOr when the player has his wheel
        
        self.onGround = True
        #If the player is on the ground
        
        self.crouch = False
        #If the player is crouched
        
        self.steps = 10
        #How many loops to preform collision checks
        
        self.state = "idle"
        #The state of the player (Mostly determines the sprite)
        self.savestate = self.state
        #The saved state of the player (Used to set anitimer to 0)
        self.anitimer = 0
        #animation timer doohickey
    def getmap(self,idk):
        self.MID = idk
    def getinf(self):
        return (self.x,self.y,self.xsize,self.ysize)
    def repos(self,nx,ny):
        #Makes the player this position
        self.x = nx
        self.y = ny
    def controlhorz(self,dirr,run):
        self.controlling = True
        self.lastDone = dirr
        #Moves you in both directions
        hardtoaccel = 12
        #The speed in which speeding up becomes harder than slowing down
        if self.crouch:
            self.maxrun = 2
        elif run:
            self.maxrun = 8 * self.vmod
        else:
            self.maxrun = 4
        
        if dirr:
            if self.vx <= self.maxrun:
                if self.vx < hardtoaccel:
                    self.vx += self.slip
                else:
                    self.vx += self.slip/5
            else:
                self.vx -= self.slip/self.idc
        else:
            if self.vx >= 0-self.maxrun:
                if self.vx > 0-hardtoaccel:
                    self.vx -= self.slip
                else:
                    self.vx -= self.slip/5
            else:
                self.vx += self.slip/self.idc
    def jump(self):
        if self.onGround:
            if self.groundpound:
                self.vy = -12
                self.groundpound = False
            else:
                self.vy = -10
    def duck(self, sneak):
        if self.bump > 0 or thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,4,self.crouch):
            return
        if sneak != self.crouch:
            if not self.crouch:
                self.ysize = 40
                self.y += 20
                self.oy -= 20
            else:
                self.ysize = 60
                self.y -= 20
                self.oy += 20
        self.crouch = sneak
    def speed(self):
        return abs(self.vx)+abs(self.vy)
    def getdir(self):
        return self.vx >= 0
    def punch(self,a,o,goinup,goingdown):
        prex = self.vx
        did = False
        mp = 1.2
        if self.wheeled:
            if self.punchcd == 0:
                did = True
                self.pound = True
                self.vy = 0
                self.touchedGround = False
                if abs(self.vx) > 7:
                    self.vx *= mp
                else:
                    if self.lastDone:
                        self.vx = 8
                    else:
                        self.vx = -8
            if self.punchcd < 30 and ((goinup and not self.crouch) or (goingdown and not (goinup or self.onGround))):
                did = True
                if self.punchcd != 0:
                    mp = 1.4
                    self.pound = True
                    self.touchedGround = False
                if goinup and not self.crouch:
                    self.wheeled = False
                    if abs(self.vx) < 12:
                        self.vx *= mp
                    self.vy = -7
                    if not (a or o):#If you just want to dash up
                        self.vx = prex * 1/(mp-0.1)
                        self.vy -= 3
                else:
                    self.groundpound = True
                    if abs(self.vx) < 5:
                        if self.lastDone:
                            self.vx = 6
                        else:
                            self.vx = -6
                    elif abs(self.vx) < 10:
                        self.vx *= mp
                    self.vy = 12
                    if not (a or o):#If you just ground pound
                        self.vx = prex/2
                        self.vy = 20
            if did:
                self.punchcd = 60
    def retick(self):
        #Pre-render maths and some other scripts that update the player that don't involve moving (good for when the game is pawused)
        self.rx = self.x + self.ox
        self.ry = self.y + self.oy
        if self.crouch:
            self.state = "duck"
        else:
            self.state = "idle"
    def move(self,overrides):
        if self.onGround:
            self.touchedGround = True
            if not self.crouch:
                self.groundpound = False
        self.idc = 2
        
        if self.punchcd > 0:
            self.punchcd -= 1
        if (abs(self.vx) < 0.1 and self.punchcd < 30) or self.punchcd < 30:
            self.pound = False
        if self.groundpound:
            self.idc = 100
        if self.bump > 0:
            self.bump -= 1
            return
        self.onGround = False
        #Actually makes you move
        
        
        if not self.controlling:#If you're not doing anything you'll be slown down
            if self.vx > 0:
                self.vx -= self.slip/self.idc
                if self.vx < 0.1:
                    self.vx = 0
            elif self.vx < 0:
                self.vx += self.slip/self.idc
                if self.vx > -0.1:
                    self.vx = 0
        
        if abs(self.vx) > 15:
            self.pound = True
        
        
        #Collision--------------------------------
        if not thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,0):
            self.vy += .3
            #if the player let go of the jump early
            if self.fasterDown and not self.pound:
                self.vy += 0.6
        dodabump = [False, self.vx]
        for i in range(self.steps):#Does physics 10 times to be sure to not phase through anything.
        #Gravity stuff
            if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,0) or overrides[0]:#THE FLOOR
                self.onGround = True
                if self.vy > 20:
                    self.vx = 0
                    self.bump = 30
                self.vy = 0
                self.y = (int((self.y+self.ysize)/40))*40-self.ysize
                if not self.wheeled:
                    self.wheeled = True
                    self.vx /= 2
            if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,1) or overrides[1]:#Ceiling collision
                if self.vy < -20:
                    self.vx = 0
                    self.bump = 30
                self.vy = 0
                self.y = (int((self.y)/40))*40+40
                
            if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,2) or overrides[2]:#Wall left
                self.x = (int((self.x+40)/40))*40
                if self.vx < -15:
                    dodabump[0] = True
                self.vx = 0
            if thing.mapcollision(self.MID,self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,3) or overrides[3]:#Wall right
                self.x = (int((self.x+self.xsize)/40))*40-self.xsize
                if self.vx > 15:
                    dodabump[0] = True
                self.vx = 0
                    
            #Terminal Velocity
            if self.vy > 15:
                self.vy -= self.slip*2
            self.fasterDown = False
            self.x += self.vx/self.steps
            self.y += self.vy/self.steps
            #Makes the movement less controllable while in air
            if self.onGround:
                self.slip = self.defslip
            else:
                self.slip = self.defslip/3
        if dodabump[0]:
            self.vx = 0-dodabump[1]/4
            self.vy = -5
            self.bump = 5
    def draw(self, Screen, off, zoom = 1):
        self.anitimer += 1
        if self.savestate != self.state:
            self.anitimer = 0
        self.savestate = self.state
        if self.pound:
            pygame.draw.rect(Screen, (255,0,0), ((self.x*zoom-off[0])-2, (self.y*zoom-off[1])-2, self.xsize*zoom+4, self.ysize*zoom+4))
        if zoom == 1:
            
            if self.state == "duck":
                Screen.blit(pygame.transform.flip(playerduck, not self.lastDone, False), (self.rx-off[0]-20, self.ry-(off[1]+20)))
            elif self.pound:
                if self.anitimer > 54:
                    self.anitimer = 0
                Screen.blit(pygame.transform.flip(playertired, not self.lastDone, False),(self.rx-off[0]-16, self.ry-(off[1]+4)),(0,(self.anitimer//3)*64,64,64))
            else:
                if self.anitimer > 48:
                    self.anitimer = 0
                Screen.blit(pygame.transform.flip(playeridle, not self.lastDone, False), (self.rx-off[0]-16, self.ry-(off[1]+4)),(0,(self.anitimer//3)*64,64,64))
        else:
            color = (100, 100, 100)
            if self.name == "w":
                color = (100, 200, 100)
            elif self.name == "m":
                color = (200, 100, 100)
            pygame.draw.rect(Screen, color, (self.x*zoom-off[0], self.y*zoom-off[1], self.xsize*zoom, self.ysize*zoom))
        
