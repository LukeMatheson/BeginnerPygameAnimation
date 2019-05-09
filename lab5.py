from Drawable import *
import pygame
import random

pygame.init()
surface = pygame.display.set_mode((300, 300))
green = (0, 255, 0)
blue = (0, 0, 255)
rectangle = Rectangle(0, 300, 300, -100, green)
rectangle2 = Rectangle(0, 0, 300, 200, blue)
snowflake = Snowflake(0, 0)
drawables = [rectangle, rectangle2, snowflake]
counter = 0
fpsClock = pygame.time.Clock()
pause = True
while counter == 0:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            counter += 1
            exit()
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE:
            if pause:
                pause = False
            else:
                pause = True
    if pause:
        for drawable in drawables:
            if isinstance(drawable, Snowflake):
                drawable.setY(30)
            drawable.draw(surface)
        snowflake2 = Snowflake(random.randint(0, 300), 0)
        drawables.append(snowflake2)
    pygame.display.update()
    fpsClock.tick(30)
