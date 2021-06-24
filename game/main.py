#-----------------------------#
# Versions : 0.7
#-----------------------------#



#-----------------------------#
# Import section
import pygame
import random
import time
import sys
from grille import *
from board import *
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

FPS = 60
fpsClock = pygame.time.Clock()

mob1_speed = [3,2]
mob1_position = [100, 400]

player_speed = 5
player_position = [0,0] # [x,y]
direction = "stop"
#-----------------------------#
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Capture the ground')
init_board(600, 500, SCREEN)

is_running = True
grille_class = Grille()
while is_running:
    matrice= grille_class.get_grille()
    actu_board(600, 500, SCREEN,matrice, grille_class)
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

    if direction == "left" and grille_class.move_player(player_position[0] - player_speed, player_position[1]) is not None:
        player_position[0] -= player_speed
    elif direction == "right" and grille_class.move_player(player_position[0] + player_speed, player_position[1]) is not None:
        player_position[0] += player_speed
    elif direction == "up" and grille_class.move_player(player_position[0], player_position[1] - player_speed) is not None:
        player_position[1] -= player_speed
    elif direction == "down" and grille_class.move_player(player_position[0], player_position[1] + player_speed) is not None:
        player_position[1] += player_speed
    else:
        pos = grille_class.get_square(player_position[0], player_position[1])
        if direction == "left":
            if pos != "MG" and pos != "MCHG" and pos != "MCBG":
                player_position[0] -= player_speed
        elif direction == "right":
            if pos != "MD" and pos != "MCHD" and pos != "MCBD":
                player_position[0] += player_speed
        elif direction == "up":
            if pos != "MH" and pos != "MCHG" and pos != "MCHD":
                player_position[1] -= player_speed
        elif direction == "down":
            if pos != "MB" and pos != "MCBG" and pos != "MCBD":
                player_position[1] += player_speed


    if grille_class.get_square(player_position[0], player_position[1]) == 0:
        grille_class.add_log([player_position[0]//10, player_position[1]//10, direction])
    else:
        print(grille_class.log)
        render_zone(grille_class)
        grille_class.log = []


    if (mob1_position[0] <10) or (mob1_position[0] > 580):
        mob1_speed[0] *= -1
    if (mob1_position[1] < 10) or (mob1_position[1] > 480):
        mob1_speed[1] *= -1

    mob1_position[0] += mob1_speed[0]
    mob1_position[1] += mob1_speed[1]

    pygame.draw.rect(SCREEN, GREEN, (mob1_position[0], mob1_position[1], 10, 10))
    pygame.draw.rect(SCREEN, RED, (player_position[0], player_position[1], 10, 10))


    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()