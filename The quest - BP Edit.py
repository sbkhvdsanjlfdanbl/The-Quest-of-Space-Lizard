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

#Loading Images for Sprites and Backgrounds and Variable Initialisation
MenuScreen = pygame.image.load("TitleScreen.png")
MenuScreen = pygame.transform.scale(MenuScreen, (WIDTH, HEIGHT))
initialScreen = pygame.image.load("land.png")
initialScreen = pygame.transform.scale(initialScreen, (WIDTH, HEIGHT))
SecondScreen = pygame.image.load("land2.png")
SecondScreen = pygame.transform.scale(SecondScreen, (WIDTH, HEIGHT))
SCREEN2 = False

FrogConvo1 = False
FrogConvo2 = False
frendSpriteX = 600
frendSpriteY = 350

image1 = pygame.image.load("Walking6.png")
image2 = pygame.image.load("Walking5.png")
image3 = pygame.image.load("Walking4.png")
image4 = pygame.image.load("Walking3.png")
image5 = pygame.image.load("Walking2.png")
image6 = pygame.image.load("Walking1.png")
SpaceLizard1 = pygame.image.load("normal.png")

Sword = pygame.image.load("Sword.png") ##52*68
Sword = pygame.transform.scale(Sword, (50, 50))
SwordBack = pygame.transform.flip(Sword, True, False)

FrogIdle = Pyganim.PygAnimation([("frog idle.png", 1)])
FrogAppear = Pyganim.PygAnimation([("frog appearance1.png", 1),
                                   ("frog appearance2.png", 1),
                                   ("frog appearance3.png", 1),
                                   ("frog appearance4.png", 1)], loop=False)

Displacement = 0
zero = 0

SpaceLizardConstant = Pyganim.PygAnimation([("normal.png", 1)])
SwordConstant = Pyganim.PygAnimation([(Sword, 1)])
SwordBackConstant = Pyganim.PygAnimation([(SwordBack, 1)])

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


#Set up for the functions for the animations
SpaceLizardConstant.play()
SpaceLizardAnim.play()
SpaceLizardBack.play()
SpaceLizardLeftIdle.play()
SwordConstant.play()
SwordBackConstant.play()
FrogIdle.play()


#Functions
def PlayerInfo():
    global PlayerLoc
    PlayerLoc = []
    player_x = 100
    player_y = 360
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
        button("Play"           ,300,125,255,60,ORANGE, PlayerInfo)     
        button("Instructions"   ,300,200,255,60,ORANGE)#,instructionsLoop)
        button("Exit"           ,300,275,255,60,ORANGE, quitGame)
        pygame.display.update()

def gameLoop():
    global SCREEN2, FrogConvo1
    Forwards = True
    playing = True
    SCREEN.fill(WHITE)
    LoadedScreen()
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        LoadedScreen()
        keys = pygame.key.get_pressed()
        #Swapping the Background for the player, backwards and forwards
        if PlayerLoc[0] <= 13:
            if SCREEN2 == False:
                PlayerLoc[0] = 13
            else:
                LoadedScreen()
                PlayerLoc[0] = 980
                SCREEN2 = False
        elif PlayerLoc[0] >= 987:
            if SCREEN2 == True:
                PlayerLoc[0] = 987
            else:
                LoadedScreen()
                PlayerLoc[0] = 100
                SCREEN2 = True
        #Walking
        if keys[pygame.K_RIGHT]:
            Forwards = True
            F_Walk(PlayerLoc[0],PlayerLoc[1])
        elif keys[pygame.K_LEFT]:
            Forwards = False
            B_Walk(PlayerLoc[0],PlayerLoc[1])
        #Jumping
        elif keys[pygame.K_UP]:
            if Displacement < 29:
                Up_Move(PlayerLoc[1], Forwards)
            else:
                if Forwards == True:
                    SpaceLizardConstant.blit(SCREEN, (PlayerLoc[0],PlayerLoc[1]))
                    SwordConstant.blit(SCREEN, ((PlayerLoc[0]+13), PlayerLoc[1]))
                else:
                    SpaceLizardLeftIdle.blit(SCREEN, (PlayerLoc[0],PlayerLoc[1]))
                    SwordBackConstant.blit(SCREEN, ((PlayerLoc[0]-13), PlayerLoc[1]))
        #Falling
        elif pygame.KEYUP:
            if Forwards == True:
                SpaceLizardConstant.blit(SCREEN, (PlayerLoc[0],PlayerLoc[1]))
                SwordConstant.blit(SCREEN, ((PlayerLoc[0]+13), PlayerLoc[1]))
                if PlayerLoc[1] < 360:
                    GravityEffect(PlayerLoc[1], Forwards)
            elif Forwards == False:
                SpaceLizardLeftIdle.blit(SCREEN, (PlayerLoc[0],PlayerLoc[1]))
                SwordBackConstant.blit(SCREEN, ((PlayerLoc[0]-13), PlayerLoc[1]))
                if PlayerLoc[1] < 360:
                    GravityEffect(PlayerLoc[1], Forwards)

        if SCREEN2 == True:
            CollisionCheck(PlayerLoc[0],PlayerLoc[1],52,68,(frendSpriteX-300), frendSpriteY,81,103)

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


#                      width of image, height of image
def CollisionCheck(x,y,w,h,x2,y2,w2,h2):
    global FrogConvo1
    if x < (x2 + w2) and (x + w) > x2 and y < (y2 + h2) and (h + y) > y2:
        FrogConvo1 = True
        ConversationScreen()


# Walking Functions
def F_Walk(playerX, playerY):
    xVal = int(playerX)
    yVal = int(playerY)
    for y in range(0,2):
        PlayerLoc.remove(PlayerLoc[0])
    LoadedScreen()
    xVal += 5
    SpaceLizardAnim.blit(SCREEN, (xVal, yVal))
    SwordConstant.blit(SCREEN, ((xVal+13), yVal))
    PlayerLoc.append(xVal)
    PlayerLoc.append(yVal)


def B_Walk(playerX, playerY):
    xVal = int(playerX)
    yVal = int(playerY)
    for x in range(0,2):
        PlayerLoc.remove(PlayerLoc[0])
    LoadedScreen()
    xVal -= 5
    SpaceLizardBack.blit(SCREEN, (xVal, yVal))
    SwordBackConstant.blit(SCREEN, ((xVal-13), yVal))
    PlayerLoc.append(xVal)
    PlayerLoc.append(yVal)

# Jumping Function
def Up_Move(playerY, Forwards):
    global Displacement
    for x in range (0,5):
        LoadedScreen()
        playerY -= 5
        PlayerLoc[1] = playerY
        Displacement = Displacement + 1
        if Forwards == True:
            SpaceLizardConstant.blit(SCREEN, (PlayerLoc[0], playerY))
            SwordConstant.blit(SCREEN, ((PlayerLoc[0]+13), playerY))
        else:
            SpaceLizardBack.blit(SCREEN, (PlayerLoc[0], playerY))
            SwordBackConstant.blit(SCREEN, ((PlayerLoc[0]-13), playerY))    


#Gravity Function
def GravityEffect(playerY, Forwards):
    global Displacement
    for x in range(0,5):
        LoadedScreen()
        playerY += 5
        PlayerLoc[1] = playerY
        Displacement = Displacement - 1
        if Forwards == True:
            SpaceLizardConstant.blit(SCREEN, (PlayerLoc[0], playerY))
            SwordConstant.blit(SCREEN, ((PlayerLoc[0]+13), playerY))
        else:
            SpaceLizardBack.blit(SCREEN, (PlayerLoc[0], playerY))
            SwordBackConstant.blit(SCREEN, ((PlayerLoc[0]-13), playerY))  

#Deciding on the loaded background
def LoadedScreen():
    global SCREEN2
    if SCREEN2 == False:
        SCREEN.blit(initialScreen, (0,0))
    elif SCREEN2 == True:
        SCREEN.blit(SecondScreen, (0,0))


def ConversationScreen():
    global convoFont, convoText, FrogConvo1
    FrogAppearFunc()
    convoFont = pygame.font.SysFont("arial", 20)
    convoText = convoFont.render("Hello there, do you need help on your quest?", True, BLACK)
    SCREEN.blit(convoText, (200,200))


def FrogAppearFunc():
    global FrogConvo1, zero
    FrogAppear.play()
    FrogAppear.blit(SCREEN, (frendSpriteX, frendSpriteY))
    if FrogAppear.isFinished() == True:
        FrogIdle.blit(SCREEN, (frendSpriteX, frendSpriteY))
        FrogAppear.stop()


# If Space Lizard has Started Screen 2, play animation, if reaches frenSpritex-300, play constant?
# Do it procedurally, then attempt to put in the text, maybe boot up a white screen version to try and put the frog in
# with button presses if it doesn't work. Def need to clean up this file.
# Try combine this with saveattempt.py, in a main quest file. Need to upload main ver. from school to github.


# Starting the program
menuLoop()

# if player presses left, if player is on screen 2, and frogConvo1 != True Frog appear, else, frog constant
