import pygame
from playerClass import Player
from EenmyClass import Enemy
pygame.init()

win = pygame.display.set_mode((498,400))
pygame.display.set_caption('My game')
bg = pygame.image.load('bg.png')

clock = pygame.time.Clock()


def reDraw():
    win.blit(bg, (0,0))
    player.draw(win)
    enemy.move(win)

    pygame.display.update()


player = Player(50,298,64,64)     #player object
enemy = Enemy(450,300,64,64)      #Enemy Object

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x>0:
        player.left = True
        player.right = False
        player.last_position = 'left'
    elif keys[pygame.K_RIGHT] and player.x<500 - player.width:
        player.left = False
        player.right = True
        player.last_position = 'right'
    elif keys[pygame.K_SPACE]:
        if not player.isJump:
            player.isJump = True


    else:
        player.left = False
        player.right = False

    reDraw()



pygame.quit()