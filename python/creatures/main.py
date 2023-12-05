import pygame
from buttons import button
from interest import creature
from interest import move

pygame.init()  
pygame.display.set_caption("Animals Fighting")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0,0,0))
clock = pygame.time.Clock()


types = {
"rock" : [0,3,11],
"paper" : [1,4,8,9],
"scissors" : [2,5,7,10],
"aerial" : [1,4,5],
"meat" : [0,6,9,15],
"tech" : [14],
"myth" : [12],
"spirit" : [13],
"physics" : [15]
}


#mouse variables--------------------------------
mousePos = (0,0)
fire = False
tap = True
defaultmove = move("Regular Attack",10,("normal","you"))

movebasket = [#Regular Moves
              move("Light Slap",5,("normal","normal")),
              move("Claw",15,("normal","normal")),
              move("Slap",15,("normal","normal")),
              move("Tackle",20,("normal","normal")),
              move("Bite",20,("normal","normal")),
              move("Slice",25,("normal","normal")),
              move("Wrestle",30,("normal","normal")),
              move("Triple-hit",35,("normal","normal")),
              move("Slam",40,("normal","normal")),
              move("Sneak Attack",50,("normal","normal"),["self_stats",False,3,-10]),
              move("Piledriver",60,("normal","normal")),
              move("Ram",90,("normal","normal"),["self_stats",False,0,-20]),
              move("A Swift Series of Attacks",100,("normal","normal")),
              move("Kamikaze",200,("normal","normal"),["death"]),
              #Rock Moves
              move("Rubble Throw",20,("rock","normal")),
              #Paper Moves
              move("Reversorama",0,("paper","normal"),["reflect","all"]),
              move("Paper Cut",20,("paper","normal")),
              #Scissor Moves
              move("Spear Kick",20,("scissors","normal")),
              #Ariel Moves
              move("Demodash",0,("aerial","normal"),["dodge"]),
              move("Breeze",10,("aerial","normal")),
              move("Giant Fan",15,("aerial","normal")),
              move("Dash",20,("aerial","normal")),
              move("Dunk",30,("aerial","normal")),
              move("Wavedash",40,("aerial","normal")),
              #Meat Moves
              move("Full Arm Slap",20,("meat","normal")),
              move("Belly Flop",40,("meat","normal")),
              move("Body Slam",80,("meat","normal")),
              #Technical Moves
              move("Extra Comma",0,("tech","normal"),["effect","stun",1]),
              move("Smart Stab",20,("tech","normal")),
              move("Minus Equals",30,("tech","normal")),
              move("Minus Equals",30,("tech","normal")),
              move("A Kai Inspired Move",120,("tech","normal"),["death","effect","stun",1]),
              #Mythical Moves
              move("Magic Missile",20,("myth","normal")),
              #Spiritual Moves
              move("Jumpscare",20,("spirit","normal")),
              #Physics Moves
              move("Goomba-Stomp",20,("physics","normal"))]

testers = [creature(0,5),creature(1,5),creature(2,5)]

attackButton = button((0,200,0),(50,700,200,200),"Test",(0,0,0))

waittime=0


testers[0].printInfo(types)
#testers[1].printInfo()
#testers[2].printInfo()

testers[0].printBattleInfo()


testers[1].printBattleInfo()

surviving = True
while surviving:
    #The input you have
    for event in pygame.event.get(): #Event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            surviving = False
        if event.type == pygame.MOUSEBUTTONDOWN and tap:
            fire = True
            tap = False
        if event.type == pygame.MOUSEBUTTONUP:
            tap = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    clock.tick(60)
    
    #Attack function *wink*
    if attackButton.tick(fire,mousePos):
        doAttack = True
        #Won't do any real damage if this is switched to false
        moveDid = defaultmove
        #Makes the move you're gonna do a default move first before you decide
        cantProceed = True
        #Makes sure you type in a valid move
        while cantProceed:
            moveRequest = input("Type the name of the move you wanna use.\n")
            for r in movebasket:
                if moveRequest == r.name:
                    moveDid = r
                    break
            if moveDid == defaultmove and moveRequest != "a":
                print("You don't have that move! If you want to use the regular default move, type in \"a\"")
            elif moveDid.type[0] == "normal" or testers[0].id in types[moveDid.type[0]]:
                cantProceed = False
            else:
                print("This creature can't use that move!")
        movebasket.remove(moveDid)
        
        if moveDid.sa == []:
            move_has_specials = True
        else:
            move_has_specials = False
        #This will be very complicated for moves with special things
        jn = 0
        en = 0
        #Jank number stands for jank number, Expected Number stands for Expected Number
        while move_has_specials:
            
            if moveDid.sa[jn] == "death":
                en += 1
                testers[0].tempstats[0] = 0
            if en <= len(moveDid.sa):
                move_has_specials = False
            elif moveDid.sa[jn] == "self_stats":
                en += 4
                testers[0].tempstats[moveDid.sa[jn+2]] += moveDid.sa[jn+3]
                if moveDid.sa[jn+1]:
                    doAttack = False
                jn += 4
            else:
                jn += 1



        if moveDid.p != 0 and doAttack:
            testers[1].tempstats[0] -= testers[0].attack(types,testers[1],moveDid)


        
        
        testers[1].printBattleInfo()
    
    #Rendering is what I do!
    screen.fill((2,20,200))
    


    attackButton.render(screen)
    pygame.display.flip()
    fire = False
pygame.quit()