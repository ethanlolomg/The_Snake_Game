import pygame
import random
from Snake import Snake
from Apple import Apple

pygame.init()
screen = pygame.display.set_mode((500,500))

grey = (50, 50, 50)
green = (0, 200, 0)
red = (200, 0, 0)
yellow = (255, 255, 0)

mySnake = Snake()
myApple = Apple(10,10)

mode = 1

font = pygame.sysfont.SysFont('Time New Roman', 72)

text = font.render("Game Over!", True, (0, 128, 0))

playing = True
while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                mySnake.setUp()
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                mySnake.setDown()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                mySnake.setLeft()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                mySnake.setRight()

    screen.fill(grey)

    if mode == 1:
        mode = mySnake.draw(screen)
        myApple.draw(screen)
        if mySnake.x == myApple.x and mySnake.y == myApple.y:
            x = random.randint(0,49)
            y = random.randint(0,49)
            myApple = Apple(x,y)
            mySnake.size += 3

    if mode == 2:
        screen.blit(text, (250, 250))



    pygame.display.flip()

pygame.quit()



