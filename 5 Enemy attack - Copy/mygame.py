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
font = pygame.font.SysFont('comicsans' , 30 , True)

clock = pygame.time.Clock()

class Bullet(object):
    def __init__(self,x,y):
        self.x = x + 26
        self.y = y + 25
        self.movingDirection = player.last_position

    def drawBullet(self , win):
        bullet = pygame.Rect(self.x , self.y , 7 , 5)
        pygame.draw.rect(win ,(255,80,200), bullet)
    
    def move(self):
        if self.movingDirection == 'left':
            self.x -= 7
        elif self.movingDirection == 'right':
            self.x += 7

def reDraw():
    global score
    win.blit(bg, (0,0))
    if player.health > 0:
        player.draw(win)
    else:
        gameOver = font.render('Game Over!' , 1 , (255,85,51))
        win.blit(gameOver , (150,100))

    scoreBar = font.render('Score :' + str(score) , 1 , (0,0,0))
    win.blit(scoreBar , (50,20))

    if not enemy and player.health!=0:
        victory = font.render('Victory' , 1 , (255,85,51))
        win.blit(victory , (200,100))

    for en in enemy:
        if en.health > 0:
            en.move(win)
            if (player.x-5 < en.x < player.x + 30) and (player.y < en.y < player.y + player.height):
                player.health -= 1
                player.x = 20
        else:
            enemy.pop(enemy.index(en))

    for bullet in bulletStore:
        bullet.move()
        bullet.drawBullet(win)
    
        for en in enemy:
            if (en.x-5 < bullet.x < en.x + 30) and (en.y < bullet.y < en.y + en.height):
                bulletStore.pop(bulletStore.index(bullet))
                score += 1
                en.health -= 5
                print(score , en.y , bullet.y)

    pygame.display.update()


player = Player(50,298,64,64)     #player object
enemy = [Enemy(450,300,64,64)]      #Enemy Object
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
        if (bullet.x < 0 or bullet.x > 500):
            bulletStore.pop(bulletStore.index(bullet))

    reDraw()



pygame.quit()