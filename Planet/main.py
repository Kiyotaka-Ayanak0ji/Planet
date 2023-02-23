import pygame
import math
from pygame.locals import *

#initializing pygame
pygame.init()
WIDTH, HEIGHT = 1920, 1080
CENTER = (WIDTH//2 , HEIGHT // 2)
surface = pygame.display.set_mode((WIDTH,HEIGHT),vsync = 1)
clock = pygame.time.Clock()

#Background
bg = pygame.Surface((WIDTH,HEIGHT))
bg.fill((20,20,20))

angle = 0

x = y = math.sqrt(CENTER[0]**2 + CENTER[1]**2)//2

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    #Black fill
    surface.fill((0,0,0))


    pygame.draw.circle(surface,(225,225,60),(x+300,y),50)
    pygame.draw.circle(surface, (225, 225, 60), (x*math.cos(angle) + 950, y*math.sin(angle)+500), 30)

    angle += 0.01

    pygame.display.update()
    
    clock.tick(144)
