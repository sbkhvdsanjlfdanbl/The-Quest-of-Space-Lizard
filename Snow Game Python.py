import pygame, time, random
pygame.init()
    
BLACK = [0   , 0   , 0  ]
WHITE = [255 , 255 , 255]
GREEN = [0   , 255 , 0  ]

clock = pygame.time.Clock()

cometsDoged = 0
giftsCollected = 0

displayWidth = 1200
displayHeight = 700
SCREEN = pygame.display.set_mode((displayWidth, displayHeight))

sleighImg = pygame.image.load('Santa Sleigh.png')
gameBackground = pygame.image.load('Snow Scene.jpg')
giftImg = pygame.image.load('Gift.png')
cometImg = pygame.image.load('Comet.png')

def quitGame():
    pygame.quit()
    quit()


def gameLoop():
    gamePlaying = True
    while gamePlaying == True:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                quitGame()

        #SCREEN.blit(gameBackground,(0,0))
        SCREEN.blit(sleighImg,(200,200))
        pygame.display.update()
        clock.tick(30)

gameLoop()
