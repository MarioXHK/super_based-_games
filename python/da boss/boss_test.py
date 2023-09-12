import pygame
import boss
pygame.init()
clock = pygame.time.Clock()#set up clock
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Boss Test")
youknowwho = boss.patra(250,250)
fire = boss.fireball(youknowwho)
gaming = True
while gaming:
    for event in pygame.event.get(): #Event queue
        if event.type == pygame.QUIT:
            gaming = False
    clock.tick(60)
    youknowwho.step()
    fire.step(youknowwho)
    screen.fill((200,200,200))
    youknowwho.draw(screen)
    fire.draw(screen)
    pygame.display.flip()
pygame.quit()