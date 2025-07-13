import pygame

class Enemy(object):
    def __init__(self ,x,y,width,height):
        self.enemyLeft = [pygame.image.load(f'L{i}E.png') for i in range(1,17)]
        self.enemyRight = [pygame.image.load(f'R{i}E.png') for i in range(1,17)]
        self.LeftRight = self.enemyLeft + self.enemyRight
        self.walkCount = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self , win):
        if self.walkCount < 48:
            self.x -= 6
        else:
            self.x += 6
        win.blit(self.LeftRight[self.walkCount//3] , (self.x,self.y))
        print(self.walkCount)
        if self.walkCount >= 95:
            self.walkCount = 0
        else:
            self.walkCount += 1