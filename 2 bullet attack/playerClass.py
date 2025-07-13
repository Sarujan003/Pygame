import pygame
class Player(object):
    def __init__(self ,x ,y ,width ,height):
        self.playerLeft = [pygame.image.load(f'L{i}.png') for i in range(1,10)]
        self.playerRight = [pygame.image.load(f'R{i}.png') for i in range(1,10)]
        self.playerStanding = pygame.image.load('standing.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.leftCount = 0
        self.rightCount = 0
        self.right = False
        self.left = False
        self.last_position = None
        self.isJump = False
        self.peek = 10

    def draw(self ,win):
        if self.leftCount+1 >=27:
            self.leftCount = 0
        elif self.rightCount+1 >=27:
            self.rightCount = 0

        if self.isJump:
            neg = 1
            if self.peek < 0:
                neg = -1
            self.y -= (self.peek**2)*0.5*neg
            # print(self.peek)
            self.peek -= 1

            if self.peek < -10:
                self.peek = 10
                self.isJump = False
        
        if self.left:
            self.leftCount += 1
            self.x -= self.vel
            win.blit(self.playerLeft[self.leftCount//3] , (self.x,self.y))
            # print(self.leftCount , self.rightCount)

        elif self.right:
            self.rightCount += 1
            self.x += self.vel
            win.blit(self.playerRight[self.rightCount//3] , (self.x,self.y))
            # print(self.leftCount , self.rightCount)

        else:
            if self.last_position is None:
                win.blit(self.playerStanding , (self.x,self.y))
            elif self.last_position == 'left':
                win.blit(self.playerLeft[0] , (self.x,self.y))
            elif self.last_position == 'right':
                win.blit(self.playerRight[0] , (self.x,self.y))
            
            self.leftCount = 0
            self.rightCount = 0