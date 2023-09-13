import pygame
import boss
pygame.init()
clock = pygame.time.Clock()#set up clock
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Boss Test")
youknowwho = boss.patra(250,250)
fire = [boss.fireball(youknowwho),boss.fireball(youknowwho,1/4),boss.fireball(youknowwho, 1/2),boss.fireball(youknowwho,3/4),boss.fireball(youknowwho,1/8),boss.fireball(youknowwho,3/8),boss.fireball(youknowwho, 5/8),boss.fireball(youknowwho,7/8)]
gaming = True
thing = 0
something = 1
somethingelse = 0
while gaming:
    thing += 1/10
    for event in pygame.event.get(): #Event queue
        if event.type == pygame.QUIT:
            gaming = False
    clock.tick(60)
    youknowwho.step(0)
    for i in range(len(fire)):
        fire[i].tx = thing/2
        if something == 1:
            fire[i].sy -= 1
            if fire[i].sy <= -100:
                something = 2
        elif something == 2:
            fire[i].sy += 1
            if fire[i].sy >= 100:
                something = 0
                somethingelse = 1
        if somethingelse == 1:
            fire[i].sx -= 1
            if fire[i].sx <= -100:
                somethingelse = 2
        elif somethingelse == 2:
            fire[i].sx += 1
            if fire[i].sx >= 100:
                something = 1
                somethingelse = 0
        fire[i].step(youknowwho)
    screen.fill((200,200,200))
    youknowwho.draw(screen)
    for i in range(len(fire)):
        fire[i].draw(screen)
    pygame.display.flip()
pygame.quit()