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


#Variables / initial set up pieces.
HEIGHT, WIDTH = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Quest of Space Lizard 21")
clock = pygame.time.Clock()
MenuScreen = pygame.image.load("TitleScreen.png")
MenuScreen = pygame.transform.scale(MenuScreen, (WIDTH, HEIGHT))
image1 = pygame.image.load("Walking6.png")
image2 = pygame.image.load("Walking5.png")
image3 = pygame.image.load("Walking4.png")
image4 = pygame.image.load("Walking3.png")
image5 = pygame.image.load("Walking2.png")
image6 = pygame.image.load("Walking1.png")
SpaceLizard1 = pygame.image.load("normal.png")
    

SpaceLizardConstant = Pyganim.PygAnimation([("normal.png", 1)])

SpaceLizardLeft = pygame.transform.flip(SpaceLizard1, True, False)
SpaceLizardLeftIdle = Pyganim.PygAnimation([(SpaceLizardLeft, 1)])

SpaceLizardAnim = Pyganim.PygAnimation([("Walking1.png", 0.1),
                                        ("Walking2.png", 0.1),
                                        ("Walking3.png", 0.1),
                                        ("Walking4.png", 0.1),
                                        ("Walking5.png", 0.1),
                                        ("Walking6.png", 0.1)])

image1 = pygame.transform.flip(image1, True, False)
image2 = pygame.transform.flip(image2, True, False)
image3 = pygame.transform.flip(image3, True, False)
image4 = pygame.transform.flip(image4, True, False)
image5 = pygame.transform.flip(image5, True, False)
image6 = pygame.transform.flip(image6, True, False)


SpaceLizardBack = Pyganim.PygAnimation([(image1, 0.1),
                                        (image2, 0.1),
                                        (image3, 0.1),
                                        (image4, 0.1),
                                        (image5, 0.1),
                                        (image6, 0.1)])

SpaceLizardConstant.play()
SpaceLizardAnim.play()
SpaceLizardBack.play()
SpaceLizardLeftIdle.play()
global Forwards
Forwards = True

#Functions
def PlayerInfo():
    global PlayerLoc
    PlayerLoc = []
    player_x = 100
    player_y = 350
    PlayerLoc.append(player_x)
    PlayerLoc.append(player_y)
    gameLoop()

def menuLoop():
    menuShowing = True
    while menuShowing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        SCREEN.blit(MenuScreen,(0,0))
        button("Play"           ,10,125,255,60,ORANGE, PlayerInfo)     
        button("Instructions"   ,10,200,255,60,ORANGE)#,instructionsLoop)
        button("Exit"           ,10,275,255,60,ORANGE, quitGame)
        pygame.display.update()

def gameLoop():
    playing = True
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        SCREEN.fill(WHITE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            F_Walk(PlayerLoc[0],PlayerLoc[1])
        elif keys[pygame.K_LEFT]:
            B_Walk(PlayerLoc[0],PlayerLoc[1])
        else:
            if Forwards == True:
                SpaceLizardConstant.blit(SCREEN, (PlayerLoc[0],PlayerLoc[1]))
            elif Forwards == False:
                SpaceLizardLeftIdle.blit(SCREEN, (PlayerLoc[0],PlayerLoc[1]))
        pygame.display.update()
        clock.tick(60)

def button(msg,x,y,w,h,c,action=None):
    global screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:        
        pygame.draw.rect(SCREEN, c, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    smallText = pygame.font.SysFont("arial", 40)
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    SCREEN.blit(textSurf, textRect)

def textObjects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def quitGame():
    pygame.quit()
    quit()

def ConversationScreen():
    Screen.fill(BLACK)

#                      width of image, height of image
def CollisionCheck(x,y,w,h,x2,y2,w2,h2):
    if (x < (x2 + w2) and (x + w) > x2 and y < (y2 + h2) and (h + y) > y2):                  
      collisionCheck = True  

def F_Walk(playerX, playerY):
    Forwards = True
    xVal = int(playerX)
    yVal = int(playerY)
    for y in range(0,2):
        PlayerLoc.remove(PlayerLoc[0])
    SCREEN.fill(WHITE)
    xVal += 5
    SpaceLizardAnim.blit(SCREEN, (xVal, yVal))
    PlayerLoc.append(xVal)
    PlayerLoc.append(yVal)
    clock.tick(30)

def B_Walk(playerX, playerY):
    Forwards = False
    xVal = int(playerX)
    yVal = int(playerY)
    for x in range(0,2):
        PlayerLoc.remove(PlayerLoc[0])
    #if CollisionCheck(playerLoc[0],playerLoc[1],0,0,1000,800,0,0)
        #PreScene = True
    #elif CollisionCheck(playerLoc[0],playerLoc[1],h,w,EnemyLoc[0],EnemyLoc[1])
    SCREEN.fill(WHITE)
    xVal -= 5
    SpaceLizardBack.blit(SCREEN, (xVal, yVal))
    PlayerLoc.append(xVal)
    PlayerLoc.append(yVal)
    clock.tick(30)




#def __init__(self, x, y):
    


menuLoop()
