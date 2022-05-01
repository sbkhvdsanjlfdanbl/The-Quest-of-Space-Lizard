import csv, pygame
pygame.init()

HEIGHT, WIDTH = 700, 1100
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

Black = (0, 0, 0)
White = (255, 255, 255)
ORANGE = (255, 165, 0)

allScores = []


def quitGame():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, c, action=None):
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
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()


def SaveSystem():
    with open('PlayerSaves.csv') as dataFile:
        fileReader = csv.DictReader(dataFile)
        for row in fileReader:
            allScores.append([row['playerName'], row['SaveCode']])
        print(allScores)
    displayScore()


def menuLoop():
    menuShowing = True
    while menuShowing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        SCREEN.fill(White)
        button("Play"           ,230,125,255,60,ORANGE,"difficultyChoiceScreen")
        #button("Instructions"   ,230,200,255,60,ORANGE,instructionsLoop)
        button("Highscores"     ,230,275,255,60,ORANGE,SaveSystem)
        button("Exit"           ,230,350,255,60,ORANGE,quitGame)
        pygame.display.update()
        clock.tick(60)


def gameLoop():
        playing = True
        while playing == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitGame()
            pygame.display.update()
            clock.tick(60)


def displayScore():
    difficultyShowing = True
    while difficultyShowing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        font = pygame.font.SysFont("comicsansms", 50)
        for x in range(len(allScores)):
            word = str(allScores[len(allScores)-(len(allScores)-x)][0])
            print(word)
            button(word, 255, (200+(75*x)), 255, 60, ORANGE, LoadSave(x))
            pygame.display.update()
            clock.tick(60)
        b = 2


def LoadSave(x):
    if allScores[x][1] == 1:
        a = 1



for x in range(len(allScores)):
    word = str(allScores[len(allScores) - (len(allScores) - x)][0])
    print(word)
    button(word, 255, (200 + (75 * x)), 255, 60, ORANGE, LoadSave(x))
    pygame.display.update()
    clock.tick(60)
