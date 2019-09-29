import pygame

class Apple:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.color=(200,20,20)

    def draw (self, screen):
        pygame.draw.rect(screen, self.color, (self.x * 10, self.y * 10, 10, 10))
