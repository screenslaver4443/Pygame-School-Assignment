# Pygame Tutorial 1
# main.py
# Nikolai Pesudovs
# 5th August 2022
# A basic pygametutorial

# Imports 
from ast import While
import pygame
import random


# Defining Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)

# preps image
BACKGROUND = pygame.image.load("images/backround.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, [1280, 720], )

# Window Settings
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Betwix Yall")

# preps the game
pygame.init()

# Loop to keep game running
if __name__ == "__main__":
    while True:
        for event in pygame.event.get():  # Event Loop
            if event.type == pygame.QUIT:  # Lets game be closed
                pygame.quit()

        # Game Logic

        ## Drawing ##
        screen.blit(BACKGROUND, [0, 0, 1280, 720])

        ##
        pygame.display.update()
