##### TO DO LIST #####
# Buttons working
# High scores file
# Display high scores in shell
# Display high scores in a pygame screen
# Game to end and ask for name
# Difficulty levels
# Instructions screen

import pygame, time, random, math, csv
pygame.init()

HEIGHT, WIDTH = 700, 1100
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
score = 0

menuScreen = pygame.image.load("Title Screen.png")
menuScreen = pygame.transform.scale(menuScreen, (WIDTH, HEIGHT))

EasyDifgameSong = pygame.mixer.Sound("Laser Groove.ogg")
MedDifgameSong = pygame.mixer.Sound("Getting it Done.ogg")
HardDifgameSong = pygame.mixer.Sound("Mighty Like Us.ogg")

def clickLocation(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def collisionCheck(x,y, balloonNumber):
    global score
    bx = bData[balloonNumber][3]
    by = bData[balloonNumber][4]
    bSize = bData[balloonNumber][6]
    if clickLocation(x,y,bx,by) < bSize:
        del bData[balloonNumber]
        score += 1

# Hec code R  G  B
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
ORANGE = (255,165, 0)
AQUA = (0, 255, 165, 255)
R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)

def quitGame():
    pygame.quit()
    quit()

def fetchScores():
    allScores = []
    with open('High Scores.csv') as dataFile:
        fileReader = csv.DictReader(dataFile)
        for row in fileReader:
            allScores.append([row['PLAYER'] ,row['SCORE']])        
    allScores = sorted(allScores, key = lambda x: int(x[1]), reverse=True)
    for i in range(len(allScores)):
        print(allScores[i])


def button(msg,x,y,w,h,c,action=None):
    global screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:        
        pygame.draw.rect(SCREEN, c, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    smallText = pygame.font.SysFont("comicsansms", 40)
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    SCREEN.blit(textSurf, textRect)

def textObjects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def dataForBallons(amount):
    global bData
    bData = []
    for i in range(amount):
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        xLoc = random.randint(0,1000)
        yLoc = random.randint(500,1800)
        size = random.randint(30,80)
        bData.append([R, G, B, xLoc, yLoc, size, i])

def displayScore():
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render("Popped: " + str(score),True, AQUA)
    SCREEN.blit(text, (0,0))

def menuLoop():
    menuShowing = True
    while menuShowing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        SCREEN.blit(menuScreen,(0,0))
        button("Play"           ,230,125,255,60,ORANGE,difficultyChoiceScreen)     
       #button("Instructions"   ,230,200,255,60,ORANGE,instructionsLoop)
        button("Highscores"     ,230,275,255,60,ORANGE,fetchScores)
        button("Exit"           ,230,350,255,60,ORANGE,quitGame)
        pygame.display.update()
        clock.tick(60)

def difficultyChoiceScreen():
    difficultyShowing = True
    while difficultyShowing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        SCREEN.blit(menuScreen,(0,0))
        pygame.draw.rect(SCREEN, AQUA, pygame.Rect(525, 100, 200, 275))
        button("Easy"      ,535,125,180,60,ORANGE,easyMode)
        button("Medium"    ,535,200,180,60,ORANGE,mediumMode)
        button("Hard"      ,535,275,180,60,ORANGE,hardMode)
        pygame.display.update()
        clock.tick(60)

#def instructionsLoop():
 #   instructionShowing = True
  #  while instructionShowing == True:
   #     for event in pygame.get():
    #        if event.type == pygame.QUIT:
     #           quitgame()
#
 #       SCREEN.blit(instructionsImage, (0,0))
  #      button("Go Back

def easyMode():
    global chosenSong, balloonSpeed
    chosenSong = EasyDifgameSong
    balloonSpeed = 2
    dataForBallons(20)
    gameLoop()

def mediumMode():
    global chosenSong, balloonSpeed
    chosenSong = MedDifgameSong
    balloonSpeed = 4
    dataForBallons(40)
    gameLoop()

def hardMode():
    global chosenSong, balloonSpeed
    chosenSong = HardDifgameSong
    balloonSpeed = 6
    dataForBallons(60)
    gameLoop()

def gameLoop():
    playing = True
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(bData)):
                    collisionCheck(mouseX, mouseY, len(bData)-1-i)
        SCREEN.fill(WHITE)
        for i in range(len(bData)):
            pygame.draw.circle(SCREEN, [bData[i][0],bData[i][1],bData[i][2]], (bData[i][3], bData[i][4]),bData[i][5])
            bData[i][4] -= balloonSpeed

        # These 5 lines of code stop the game when enough balloons have flaoted off the screen
        aboveScreenNumber = 0
        for i in range(len(bData)):
            aboveScreenNumber += bData[i][4]
        if aboveScreenNumber < -60000:
            playing = False
            pygame.quit()
            name = input("Well done. Please enter your name: ")
            playerData = name + "," + str(score) + "\n"
            file = open("High Scores.csv" , "a")
            file.write(playerData)
            file.close()
            quit()
             
        displayScore()
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        pygame.display.update()
        clock.tick(60)

menuLoop()

