import pygame
from playerClass import Player
from EenmyClass import Enemy
pygame.init()

win = pygame.display.set_mode((498,400))
pygame.display.set_caption('My game')
bg = pygame.image.load('bg.png')
bg2 = bg
bgX = 0
bgX2 = bg.get_width()
bgX3 = -1*bg.get_width()
print(bgX2)
clock = pygame.time.Clock()

class Bullet(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.movingDirection = player.last_position

    def drawBullet(self , win):
        bullet = pygame.Rect(self.x+26 , self.y+25 , 7 , 5)
        pygame.draw.rect(win ,(0,0,0), bullet)
    
    def move(self):
        if self.movingDirection == 'left':
            self.x -= 7
        elif self.movingDirection == 'right':
            self.x += 7

def reDraw():
    global score
    win.blit(bg, (bgX,0))
    win.blit(bg, (bgX2,0))
    win.blit(bg, (bgX3,0))
    player.draw(win)
    enemy.move(win)

    for bullet in bulletStore:
        bullet.move()
        bullet.drawBullet(win)

        if enemy.x-5 < bullet.x < enemy.x + 30:
            bulletStore.pop(bulletStore.index(bullet))
            score += 1
            print(score)

    pygame.display.update()


player = Player(50,298,64,64)     #player object
enemy = Enemy(450,300,64,64)      #Enemy Object
bulletStore = []
score = 0

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
    elif keys[pygame.K_UP]:
        if not player.isJump:
            player.isJump = True
    elif keys[pygame.K_SPACE]:
        if len(bulletStore) < 1 and player.last_position:
            bulletStore.append(Bullet(player.x , player.y))

    else:
        player.left = False
        player.right = False

    for bullet in bulletStore:
        if bullet.x < 0 or bullet.x > 500:
            bulletStore.pop(bulletStore.index(bullet))

    if player.x >= 200 and player.right:
            bgX -= 5
            bgX2 -= 5
            enemy.x -= 5
            player.x -= 5 

            if bgX < bg.get_width() * -1:
                bgX = bg.get_width()
            if bgX2 < bg.get_width() * -1:
                bgX2 = bg.get_width()
    if player.x < 200 and player.left:
            bgX += 5
            bgX2 += 5
            enemy.x += 5
            player.x += 5 

            if bgX > bg.get_width() :
                bgX = -1 * bg.get_width()
            if bgX2 > bg.get_width() :
                bgX2 = -1 * bg.get_width()

    reDraw()



pygame.quit()