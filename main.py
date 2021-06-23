#-----------------------------#
# Versions : 0.2
#-----------------------------#



#-----------------------------#
# Import section
import pygame
import random
import time
import sys
#-----------------------------#


#-----------------------------#
# Constantes
WIDTH = 600
HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

FPS = 60
fpsClock = pygame.time.Clock()

player_speed = 3
player_position = [0,0] # [x,y]
direction = "stop"
#-----------------------------#





pygame.init()


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Capture the ground')


is_running = True
while is_running:
    SCREEN.fill(WHITE)
    player = pygame.Rect(player_position,(10,10))
    pygame.draw.rect(SCREEN, RED, player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = "left"
    elif keys[pygame.K_RIGHT]:
        direction = "right"
    elif keys[pygame.K_UP]:
        direction = "up"
    elif keys[pygame.K_DOWN]:
        direction = "down"

    if direction == "left":
        player_position[0] -= player_speed
    elif direction == "right":
        player_position[0] += player_speed
    elif direction == "up":
        player_position[1] -= player_speed
    elif direction == "down":
        player_position[1] += player_speed


    pygame.draw.rect(SCREEN, RED, (player_position[0], player_position[1], 10, 10))



    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()