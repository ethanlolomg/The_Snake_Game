import pygame
from SnakeBody import SnakeBody

class Snake:
    def __init__(self):
        self.x = 25
        self.y = 25
        self.tail = []
        self.size = 3
        self.speed = 100
        self.lastMove = pygame.time.get_ticks()

        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0


    def draw(self, screen):
        thisTick = pygame.time.get_ticks()
        if thisTick - self.lastMove > self.speed:
            #It's been self.speed milliseconds, move the snake
            if self.up != 0 or self.down != 0 or self.left != 0 or self.right != 0:
                self.tail = [SnakeBody(self.x,self.y)] + self.tail
                self.tail = self.tail[0:self.size]
            # [one, two, three, four]
            #  list[0] = 'one'
            # list[3] = 'four'
            # list[1] + list[2]
            # list[1:2]
            self.y -= self.up
            self.y += self.down
            self.x -= self.left
            self.x += self.right
            self.lastMove = thisTick
            if self.y < 0 or self.y >= 50:
                return 2
            if self.x < 0 or self.x >= 50:
                return 2

        pygame.draw.rect(screen, (0, 200, 0),(self.x * 10, self.y * 10, 10, 10))
        for body in self.tail:
            if self.x == body.x and self.y == body.y:
                return 2
            body.draw(screen)

        return 1



    def setUp(self):
        if self.down == 0:
            self.up = 1
            self.left = 0
            self.right = 0

    def setDown(self):
        if self.up == 0:
            self.down = 1
            self.left = 0
            self.right = 0

    def setRight(self):
        if self.left == 0:
            self.right = 1
            self.down = 0
            self.up = 0

    def setLeft(self):
        if self.right == 0:
            self.left = 1
            self.down = 0
            self.up = 0





