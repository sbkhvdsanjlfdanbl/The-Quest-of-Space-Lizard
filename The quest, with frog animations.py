# Libraries
import pygame, csv
# Required if you don't have the Pyganim repository installed
from pygame.locals import *
import Pyganim

# Starting Pygame
pygame.init()

# Colours
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
ORANGE = [255, 165, 0]
Purple = [51, 0, 102]

# Variables / initial set up pieces.
HEIGHT, WIDTH = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Quest of Space Lizard 21")
clock = pygame.time.Clock()

# Loading Images for Sprites and Backgrounds
MenuScreen = pygame.image.load("TitleScreen.png")
MenuScreen = pygame.transform.scale(MenuScreen, (WIDTH, HEIGHT))
initialScreen = pygame.image.load("land.png")
initialScreen = pygame.transform.scale(initialScreen, (WIDTH, HEIGHT))
SecondScreen = pygame.image.load("land2.png")
SecondScreen = pygame.transform.scale(SecondScreen, (WIDTH, HEIGHT))

# Boolean Variables
SCREEN2 = False
NewGameVar = False

# Creating reversed image sprites
image1 = pygame.image.load("Walking6.png")
image2 = pygame.image.load("Walking5.png")
image3 = pygame.image.load("Walking4.png")
image4 = pygame.image.load("Walking3.png")
image5 = pygame.image.load("Walking2.png")
image6 = pygame.image.load("Walking1.png")
SpaceLizard1 = pygame.image.load("normal.png")

Sword = pygame.image.load("Sword.png")  # 52*68
Sword = pygame.transform.scale(Sword, (50, 50))
SwordBack = pygame.transform.flip(Sword, True, False)

# Setting up the frog.
# Frog Location
frendSpriteX = 600
frendSpriteY = 350

# Frog Sprites and Animation
FrogIdle = Pyganim.PygAnimation([("frog idle.png", 1)])
FrogAppear = Pyganim.PygAnimation([("frog appearance1.png", 2),
                                   ("frog appearance2.png", 2),
                                   ("frog appearance3.png", 2),
                                   ("frog appearance4.png", 2)], loop=False)

# Variables
Displacement = 0
SaveVal = 0
SaveSlot = 0
WrittenWord = ""

# Space Lizard animations
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

# Reversing sprite images
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

# This List contains all the data from the csv file
allScores = []

# Set up for the functions for the animations
SpaceLizardConstant.play()
SpaceLizardAnim.play()
SpaceLizardBack.play()
SpaceLizardLeftIdle.play()
SwordConstant.play()
SwordBackConstant.play()
FrogIdle.play()


# Functions
def PlayerInfo():
    global PlayerLoc
    PlayerLoc = []
    player_x = 100
    player_y = 360
    PlayerLoc.append(player_x)
    PlayerLoc.append(player_y)
    gameLoop()


# This runs the menu code and allow the player to exit the game or play the game.
def menuLoop():
    menuShowing = True
    while menuShowing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        SCREEN.blit(MenuScreen,(0,0))
        button("Play"           ,300,125,255,60,ORANGE, SaveSystem)
        button("Exit"           ,300,200,255,60,ORANGE, quitGame)
        pygame.display.update()


# This runs the main gameplay loop, and is where the players inputs are checked and responded to
def gameLoop():
    global SCREEN2
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
        # Swapping the Background for the player, backwards and forwards
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
        # Walking
        if keys[pygame.K_ESCAPE]:
            SaveSaves()
        elif keys[pygame.K_RIGHT]:
            Forwards = True
            F_Walk(PlayerLoc[0],PlayerLoc[1])
        elif keys[pygame.K_LEFT]:
            Forwards = False
            B_Walk(PlayerLoc[0],PlayerLoc[1])
        # Jumping
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
        # Falling
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
        if SCREEN2:
            if not FrogAppear.isFinished():
                FrogAppear.play()
                FrogAppear.blit(SCREEN, (frendSpriteX, frendSpriteY))
            else:
                FrogIdle.blit(SCREEN, (frendSpriteX, frendSpriteY))
                convoFont = pygame.font.SysFont("arial", 20)
                convoPT1 = convoFont.render("Hello there, do you need help on your quest?", True, BLACK)
                convoPT2 = convoFont.render("Hey Cool looking Frog bro, I'm missing some eggs, "
                                            "you know where they might be?", True, Purple)
                convoPT3 = convoFont.render("Absolutely, go just past me!", True, BLACK)
                SCREEN.blit(convoPT1, (200, 200))
                SCREEN.blit(convoPT2, (200, 250))
                SCREEN.blit(convoPT3, (200, 300))
                # More if statements would need to be added throughout this segment in the future when more content
                # is added
        pygame.display.update()
        clock.tick(60)


# This is the original button code, it runs the function included as a parameter, when the button it creates is pressed.
def button(msg, x, y, w, h, c, action=None):
    global screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(SCREEN, c, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    smallText = pygame.font.SysFont("arial", 40)
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    SCREEN.blit(textSurf, textRect)


# This code allows me to display text on the screen
def textObjects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# Allows for exiting the game
def quitGame():
    pygame.quit()
    quit()


# Walking Functions
# Walking forwards
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


# Walking backwards
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


# Gravity Function
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


# Deciding on the loaded background
def LoadedScreen():
    global SCREEN2
    if SCREEN2 == False:
        SCREEN.blit(initialScreen, (0,0))
    elif SCREEN2 == True:
        SCREEN.blit(SecondScreen, (0,0))
    # extra  nested if statements would be required to add more screens to the game


# SaveSystem
# This opens the CSV file, and reads all the data from within, before saving all the information to allScores
def SaveSystem():
    with open('PlayerSaves.csv') as dataFile:
        fileReader = csv.DictReader(dataFile)
        for row in fileReader:
            allScores.append([row['playerName'], row['SaveCode'], row['SlotNum']])
    displaySaves()


# This plays after pressing play, the player is able to choose an already existing save, or create a new game
def displaySaves():
    difficultyShowing = True
    while difficultyShowing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        SCREEN.blit(MenuScreen, (0, 0))
        pygame.draw.rect(SCREEN, Purple, pygame.Rect(585, 125, 200, 275))
        if NewGameVar == False:
            for x in range(len(allScores)):
                word = str(allScores[int(allScores[x][2])][0])
                ButtonSaves(word, 585, (125 + (75 * x)), 180, 60, ORANGE, x, LoadSave)
            button("New Game", 595, 350, 180, 60, ORANGE, NewGame)
        if NewGameVar == True:
            font = pygame.font.SysFont("arial", 20)
            OverwriteSlot = font.render("Which Slot do you want to overwrite?", True, BLACK)
            SCREEN.blit(OverwriteSlot, (550, 100))
            for x in range(len(allScores)):
                word = str(allScores[int(allScores[x][2])][0])
                ButtonSaves(word, 585, (125 + (75 * x)), 180, 60, ORANGE, x, overwriteFunc)
        pygame.display.update()
        clock.tick(60)


# This button code allows me to pass a parameter to the function at the end, of the parameters,
# without the function running immediately
def ButtonSaves(msg, x, y, w, h, c, z, action=None):
    global screen, SaveSlot
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    SaveSlot = z
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(SCREEN, c, (x, y, w, h))
        if click[0] == 1 and action != None:
            action(z)

    smallText = pygame.font.SysFont("arial", 40)
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    SCREEN.blit(textSurf, textRect)


# This function loads the data in a selected slot, assuming that selection is not 'New Game'
def LoadSave(SaveSlot):
    global FrogConvo1, SCREEN2, WrittenWord
    SaveLocation = int(allScores[SaveSlot][1])
    WrittenWord = allScores[SaveSlot][0]

    if SaveLocation == 0:
        PlayerInfo()
    elif SaveLocation == 1:
        SCREEN2 = True
        PlayerInfo()
    # This will be updated in the future to include more statements when I add more to the gameplay


# This code saves the players' location in the game, using an incremental variable which is passed to the csv file later
def SaveSaves():
    global SaveVal
    if SCREEN2 == False:
        SaveGame(WrittenWord)
    elif SCREEN2 == True:
        SaveVal += 1
        SaveGame(WrittenWord)
    # As the game progresses, more if statements would be needed to account for more segments of the game


# This code allows the player to input and save their name when creating a new game
# There may be an easier way of scanning the input and saving to a variable, but this works.
def NameLoop():
    global WrittenWord
    playing = True
    SCREEN.fill(WHITE)
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        font = pygame.font.SysFont("arial", 20)
        keys = pygame.key.get_pressed()
        # a
        if keys[pygame.K_a]:
            WrittenWord += "a"
        # b
        elif keys[pygame.K_b]:
            WrittenWord += "b"
        # c
        elif keys[pygame.K_c]:
            WrittenWord += "c"
        # d
        elif keys[pygame.K_d]:
            WrittenWord += "d"
        # e
        elif keys[pygame.K_e]:
            WrittenWord += "e"
        # f
        elif keys[pygame.K_f]:
            WrittenWord += "f"
        # g
        elif keys[pygame.K_g]:
            WrittenWord += "g"
        # h
        elif keys[pygame.K_h]:
            WrittenWord += "h"
        # i
        elif keys[pygame.K_i]:
            WrittenWord += "i"
        # j
        elif keys[pygame.K_j]:
            WrittenWord += "j"
        # k
        elif keys[pygame.K_k]:
            WrittenWord += "k"
        # l
        elif keys[pygame.K_l]:
            WrittenWord += "l"
        # m
        elif keys[pygame.K_m]:
            WrittenWord += "m"
        # n
        elif keys[pygame.K_n]:
            WrittenWord += "n"
        # o
        elif keys[pygame.K_o]:
            WrittenWord += "o"
        # p
        elif keys[pygame.K_p]:
            WrittenWord += "p"
        # q
        elif keys[pygame.K_q]:
            WrittenWord += "q"
        # r
        elif keys[pygame.K_r]:
            WrittenWord += "r"
        # s
        elif keys[pygame.K_s]:
            WrittenWord += "s"
        # t
        elif keys[pygame.K_t]:
            WrittenWord += "t"
        # u
        elif keys[pygame.K_u]:
            WrittenWord += "u"
        # v
        elif keys[pygame.K_v]:
            WrittenWord += "v"
        # w
        elif keys[pygame.K_w]:
            WrittenWord += "w"
        # x
        elif keys[pygame.K_x]:
            WrittenWord += "x"
        # y
        elif keys[pygame.K_y]:
            WrittenWord += "y"
        # z
        elif keys[pygame.K_z]:
            WrittenWord += "z"
        # Delete letter
        elif keys[pygame.K_BACKSPACE]:
            WrittenWord = WrittenWord[:-1]
        # Confirm Word
        elif keys[pygame.K_RETURN]:
            playing = False
        # No key is pressed
        NameWrite = font.render("Please write your name here:", True, BLACK)
        Specifications = font.render("You may use letters, and backspace if you make a mistake", True, BLACK)
        Finish = font.render("Press enter once you are finished", True, BLACK)
        DisplayWord = font.render(WrittenWord, True, BLACK)
        SCREEN.fill(WHITE)
        SCREEN.blit(DisplayWord, (200, 250))
        SCREEN.blit(NameWrite, (200, 100))
        SCREEN.blit(Specifications, (200, 150))
        SCREEN.blit(Finish, (200, 200))
        pygame.display.update()
        clock.tick(10)


# This code saves the players' information into the CSV file and saves into the slot they either picked, or overwrote.
def SaveGame(playername):
    SaveInfo = playername, SaveVal, SaveSlot
    with open('PlayerSaves.csv', 'w') as dataFile:
        if SaveSlot == 0:
            allScores[0] = SaveInfo
            writer = csv.writer(dataFile)
            writer.writerow(["playerName", "SaveCode", "SlotNum"])
            writer.writerows(allScores)
            dataFile.close()
            quitGame()
        elif SaveSlot == 1:
            allScores[1] = SaveInfo
            writer = csv.writer(dataFile)
            writer.writerow(["playerName", "SaveCode", "SlotNum"])
            writer.writerows(allScores)
            dataFile.close()
            quitGame()
        elif SaveSlot == 2:
            allScores[2] = SaveInfo
            writer = csv.writer(dataFile)
            writer.writerow(['playerName', 'SaveCode', 'SlotNum'])
            writer.writerows(allScores)
            dataFile.close()
            quitGame()


# This code runs if the player selects new game. This runs the NameLoop function, and changes the statement
# within displaySaves to allow the player to overwrite a current save.
def NewGame():
    global NewGameVar
    NameLoop()
    NewGameVar = True


# This function saves the location to overwrite when a new game is run later in the code.
def overwriteFunc(SaveLoc):
    global SaveSlot
    SaveSlot = SaveLoc
    PlayerInfo()


# Starting the program
menuLoop()

# To do:
# Enemies/Integrate classes.
# New screens.
# Add attack animation
