# Makes the map swap once, when left is pressed.

import pygame, random
from pygame.locals import *
import Pyganim
pygame.init()

#Colours
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
ORANGE = [255, 165, 0]

### MapScreenSwapping
initialScreen = pygame.image.load("land.png")
SecondScreen = pygame.image.load("land2.png")
SCREEN1 = False
SCREEN2 = False


HEIGHT, WIDTH = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Quest of Space Lizard 21")
clock = pygame.time.Clock()

def gameLoop():
    global SCREEN1, SCREEN2
    playing = True
    SCREEN.blit(initialScreen, (0,0))
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            LoadedScreen()
        elif keys[pygame.K_LEFT]:
            SCREEN2 = True
        pygame.display.update()
        clock.tick(60)

def quitGame():
    pygame.quit()
    quit()

def LoadedScreen():
    global SCREEN2
    if SCREEN2 == False:
        SCREEN.blit(initialScreen, (0,0))
    elif SCREEN2 == True:
        SCREEN.blit(SecondScreen, (0,0))

gameLoop()
