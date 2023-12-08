import pygame
from buttons import button
from interest import creature
from interest import move
import random

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
throwmeaway = move("Regular Attack+",11,("normal","you"))

moveRepo = (#Regular Moves
              move("Light Slap",5,("normal","normal")),
              move("Claw",15,("normal","normal")),
              move("Slap",15,("normal","normal")),
              move("Tackle",20,("normal","normal")),
              move("Bite",20,("normal","normal")),
              move("Slice",25,("normal","normal")),
              move("Wrestle",30,("normal","normal")),
              move("Triple-hit",35,("normal","normal")),
              move("Slam",40,("normal","normal")),
              move("Sneak Attack",50,("normal","normal"),[["self_stats",3,-10]]),
              move("Piledriver",60,("normal","normal")),
              move("Ram",90,("normal","normal"),[["self_stats",0,-20]]),
              move("A Swift Series of Attacks",100,("normal","normal")),
              move("Kamikaze",200,("normal","normal"),[["death"]]),
              #Rock Moves
              move("Intimidate",0,("rock","meat"),[["stats",2,-5]]),
              move("Rubble Throw",20,("rock","normal")),
              move("Rock Rage",25,("rock","normal"),[["self_stats",1,10],["self_stats",2,-5]]),
              move("Rock-hard punch",30,("rock","normal")),
              move("Flint And Iron",35,("rock","normal")),
              move("Catapult",40,("rock","normal")),
              move("Meteor Strike",70,("rock","meat")),
              #Paper Moves
              move("Reversorama",0,("paper","normal"),[["reflect","all"]]),
              move("Paper Cut",20,("paper","normal")),
              #Scissor Moves
              move("Spear Kick",20,("scissors","normal")),
              move("Axe Buster",30,("scissors","normal")),
              #Ariel Moves
              move("Demodash",0,("aerial","normal"),[["dodge"]]),
              move("Meditation",0,("aerial","normal"),[["reflect","spirit"],["self_stats",0,10]]),
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
              move("Extra Comma",0,("tech","normal"),[["effect","stun",100]]),
              move("Flashbang",10,("tech","normal"),[["effect","stun",55]]),
              move("Smart Stab",20,("tech","normal")),
              move("Minus Equals",30,("tech","normal")),
              move("Rubber Tree Slam",35,("tech","normal")),
              move("A Kai Inspired Move",120,("tech","normal"),[["death"],["effect","stun",95]]),
              #Mythical Moves
              move("Magic Missile",20,("myth","normal")),
              move("Magic Missile",20,("myth","normal")),
              #Spiritual Moves
              move("Jumpscare",20,("spirit","normal")),
              #Physics Moves
              move("Goomba-Stomp",20,("physics","normal")))

movebasket: list[move] = []

for i in range(50):
    movebasket.append(random.choice(moveRepo))


testers = [creature(0,5),creature(1,5),creature(2,5)]
battling = [creature(0,5,False,True),creature(1,5),creature(2,5)]

battling[0].name = "Player"

attackButton = button((0,200,0),(50,700,200,200),"Test",(0,0,0))

waittime=0


testers[0].printInfo(types)
#testers[1].printInfo()
#testers[2].printInfo()

testers[0].printBattleInfo(types)


testers[1].printBattleInfo(types)

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
        
        movebasket.sort(key=lambda x: x.name, reverse=True)

        doAttack = True
        #Won't do any real damage if this is switched to false
        moveDid = defaultmove
        #Makes the move you're gonna do a default move first before you decide
        cantProceed = True
        #Makes sure you type in a valid move
        while cantProceed:
            print("Available Moves:")
            previousoh = defaultmove
            m = 1
            for oh in movebasket:
                if previousoh == oh:
                    m += 1
                else:
                    print(previousoh.name, "(", previousoh.type[0], ")", end = "")
                    if m != 1:
                        print("("+str(m)+")", end = "")
                    m = 1
                    print(end = ", ")
                previousoh = oh
            else:
                print(previousoh.name, end = "")
                if m != 1:
                    print("("+str(m)+")", end = "")
                m = 1
                print(end = ", ")

            moveRequest = input("\nType the name of the move you wanna use.\n")
            for r in movebasket:
                if moveRequest == r.name:
                    moveDid = r
                    break
            if moveDid == defaultmove and moveRequest != "a":
                print("You don't have that move! If you want to use the regular default move, type in \"a\"")
            elif moveDid.type[0] == "normal" or battling[0].id in types[moveDid.type[0]]:
                cantProceed = False
            else:
                print("This creature can't use that move!")
        if len(battling) > 2:
            cantProceed = True
            target = battling[0]
            while cantProceed:
                print("Type the name of the creature you want to use this move on.")
                for h in battling:
                    print(h.name)
                whoTo = input()
                for r in battling:
                    if whoTo == r.name:
                        target = r
                        cantProceed = False
                        break
        else:
            for ip in battling:
                if not ip.player:
                    target = ip

        if moveDid != defaultmove:
            movebasket.remove(moveDid)
        
        battling.sort(key=lambda x: x.tempstats[3], reverse=True)

        reflect = ["nul","nil"]

        for m in range(len(battling)):
            print("MOVE", (m+1))
            
            t = 0
            
            if battling[m].tempstats[0] <= 0:
                print(battling[m].name+ "'s down!")
                continue
            
            if "stun" in battling[m].effects or "paralyze" in battling[m].effects:
                print(battling[m].name, "can't move!")
                battling[m].doEffect()
                continue

            if battling[m].player:
                t = battling.index(target)
                moveDoing = moveDid
            else:
                #What non-player creatures do when attacking
                cant = True
                while cant:
                    #Attacks a random creature
                    t = random.randrange(0,len(battling))
                    if battling[t] != battling[m]:
                        cant = False
                cant = True
                while cant:
                    #Uses a random move from the move basket
                    moveDoing = random.choice(movebasket)
                    if moveDoing.type[0] == "normal" or battling[m].id in types[moveDoing.type[0]]:
                        cant = False

            print("Creature attacking:", end = " ")
            battling[m].printBattleInfo(types)
            print("Targeted Creature:", end = " ")
            battling[t].printBattleInfo(types)


            print(battling[m].name, "uses", moveDoing.name)

            if moveDoing.sa == []:
                move_has_specials = True
            else:
                move_has_specials = False
            #This will be very complicated for moves with special things

            #Specials (or Special attacks, thus .sa) are stored as a list within a list. Each list in the list specifies a specific special
            #The first part of the list inside a list defined what exact special it is, and this for loop checks all the lists in the list
            #inside the for loop itself is where the special stuff happens
            
            
            
            for smove in moveDoing.sa:
                print(smove)
                if smove[0] == "death":
                    #Death only has 1 length. It simply turns the user's HP to 0
                    battling[m].tempstats[0] = 0
                elif smove[0] == "dont_attack":
                    #Don't Attack only has 1 length. It makes it so damage is done
                    doAttack = False
                elif smove[0] == "chance":
                    #Chance has a length of 2
                    #The second value determines what the chance of the attack hitting is
                    if random.randint(1,100) <= smove[2]:
                        doAttack = False
                        break
                elif smove[0] == "stats":
                    #(See Self Stats.)
                    battling[t].tempstats[smove[1]] += smove[2]
                    if smove[1] == 0:
                        if battling[t].tempstats[0] > battling[t].stats[0]:
                            battling[t].tempstats[0] = battling[t].stats[0]
                    elif battling[t].tempstats[smove[1]] <= 0:
                        battling[t].tempstats[smove[1]] = 1
                elif smove[0] == "self_stats":
                    #Self Stats has a length of 3. The second value determines what stat to effect
                    #The third determines how much to add to it (This can of course be a negative)
                    battling[m].tempstats[smove[1]] += smove[2]
                    if smove[1] == 0:
                        if battling[m].tempstats[0] > battling[m].stats[0]:
                            battling[m].tempstats[m] = battling[m].stats[0]
                    elif battling[m].tempstats[smove[1]] <= 0:
                        battling[m].tempstats[smove[1]] = 1
                elif smove[0] == "effect":
                    #Effect has a length of 3. The second value is what effect is applied
                    #The third value determines the chance of the effect going in percent
                    if random.randint(1,100) <= smove[2]:
                        if not (smove[1] in battling[t].effects):
                            battling[t].effects.append(smove[1])
                            battling[t].ecounter.append(random.randint(3,15))
                        else:
                            battling[t].ecounter[battling[t].effects.index(smove[1])] += random.randint(1,5)
                elif smove[0] == "reflect":
                    #Reflect (above) has a length of 2. The second value determines what types it can reflect
                    doAttack = False
                    #Reflect as a list has 2 values, the caster, and the type.
                    reflect = [battling[m], smove[1]]

            #this is the part where damage is actually done
            
            if moveDoing.p != 0 and doAttack:
                dam = battling[m].attack(types,battling[t],moveDoing)
                print("It deals", dam, "damage.")
                if reflect[0] == battling[t] and (reflect[1] == "all" or reflect[1] in moveDoing.type):
                    print("but the damage was reflected back to the attacker!")
                    battling[m].tempstats[0] -= dam
                battling[t].tempstats[0] -= dam
            print("Creature attacking:", end = " ")
            battling[m].printBattleInfo(types)
            print("Targeted Creature:", end = " ")
            battling[t].printBattleInfo(types)
            battling[m].doEffect()

        
    
    #Rendering is what I do!
    screen.fill((2,20,200))
    


    attackButton.render(screen)
    pygame.display.flip()
    fire = False
pygame.quit()