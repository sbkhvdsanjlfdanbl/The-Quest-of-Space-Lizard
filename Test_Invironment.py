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

PlayerData = [R, G, B, player_x, player_y, player_size]

def gameLoop():
    Forwards = True
    playing = True
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            PlayerData[4] -= 30
            Up_Move(PlayerData[3],PlayerData[4])
        SCREEN.fill(WHITE)
        pygame.draw.circle(SCREEN, [PlayerData[0],PlayerData[1],PlayerData[2]], (PlayerData[3], PlayerData[4]), PlayerData[5])
        pygame.display.update()
        clock.tick(60)

def quitGame():
    pygame.quit()
    quit()

def Up_Move(playerX, playerY):
    SCREEN.fill(WHITE)
    playerY -= 30
    for i in range(0, len(PlayerData)):
        PlayerData.remove(PlayerData[0])
    PlayerData.append(R)
    PlayerData.append(G)     
    PlayerData.append(B)     
    PlayerData.append(playerX)     
    PlayerData.append(playerY)
    PlayerData.append(player_size)
    

gameLoop()
