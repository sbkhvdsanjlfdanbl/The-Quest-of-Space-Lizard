# Has a ball that can be made to jump, then comes back down.

#Libraries
import pygame, random
from pygame.locals import *
import Pyganim
pygame.init()


#Colours
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
ORANGE = [255, 165, 0]

HEIGHT, WIDTH = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)

player_x = 100
player_y = 350
player_size = 30
Displacement = 0

PlayerData = [R, G, B, player_x, player_y, player_size]

def gameLoop():
    Forwards = True
    playing = True
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        keys = pygame.key.get_pressed()
        if PlayerData[3] < 13:
            PlayerData[3] = 13
        elif PlayerData[3] > 987:
            PlayerData[3] = 987
        elif PlayerData[4] <= 30:
            PlayerData[4] = 30
        if keys[pygame.K_UP]:
            if Displacement < 29:
                Up_Move(PlayerData[3],PlayerData[4])
        elif PlayerData[4] < 350:
            GravityEffect(PlayerData[4])
        SCREEN.fill(WHITE)
        pygame.draw.circle(SCREEN, [PlayerData[0],PlayerData[1],PlayerData[2]], (PlayerData[3], PlayerData[4]), PlayerData[5])
        pygame.display.update()
        clock.tick(60)

def quitGame():
    pygame.quit()
    quit()

def Up_Move(playerX, playerY):
    global Displacement
    for x in range (0,5):
        SCREEN.fill(WHITE)
        playerY -= 5
        PlayerData[4] = playerY
        Displacement = Displacement + 1

def GravityEffect(playerY):
    global Displacement
    for x in range(0,5):
        SCREEN.fill(WHITE)
        playerY += 5
        PlayerData[4] = playerY
        Displacement = Displacement - 1


gameLoop()
