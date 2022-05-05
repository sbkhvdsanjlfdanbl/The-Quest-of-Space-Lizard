import pygame, time, random
pygame.init()
    
BLACK = [0   , 0   , 0  ]
WHITE = [255 , 255 , 255]
GREEN = [0   , 255 , 0  ]
RED =   [255 , 0   , 0  ]
GOLD =  [204 , 102 , 0  ]

clock = pygame.time.Clock()

giftsCollected = 0

infoObject = pygame.display.Info()
displayWidth, displayHeight = infoObject.current_w, infoObject.current_h
SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

sleighImg = pygame.image.load('Santa Sleigh.png')
gameBackground = pygame.image.load('Snow Scene.jpg')
gameBackground = pygame.transform.scale(gameBackground, (displayWidth, displayHeight))
giftImg = pygame.image.load('Gift.png')
cometImg = pygame.image.load('Comet.png')

xmasSong = pygame.mixer.Sound("Jingle Bells.wav")

userText = "Enter Name.."

def quitGame():
    pygame.quit()
    quit()

def snowBallLocations():
    global allSnowLocations
    allSnowLocations = []
    for i in range(5000):
        snowBallX = random.randrange(0, displayWidth + 500)
        snowBallY = random.randrange(0, displayHeight)
        allSnowLocations.append([snowBallX, snowBallY])

def pause():
    xmasSong.stop()
    bigPauseFont = pygame.font.SysFont("impact", 200)
    pauseTextLine1 = bigPauseFont.render("P A U S E D", True, BLACK)
    smallPauseFont = pygame.font.SysFont("comicsansms", 50)
    pauseTextLine2 = smallPauseFont.render("Press U to unpause the game ....", True, BLACK)
    gamePaused = True
    while gamePaused == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_u]:
                gameLoop()
        SCREEN.fill(WHITE)
        SCREEN.blit(pauseTextLine1, (200,150))
        SCREEN.blit(pauseTextLine2, (240,400))
        pygame.display.update()
        clock.tick(5)
            
def scoreData():
    GameFont = pygame.font.SysFont("cooperblack", 40)
    GameText = GameFont.render("Gifts Collected : " + str(giftsCollected), True, GOLD)
    SCREEN.blit(GameText, (20, 20))

def cometCollisionCheck(x,y,w,h,x2,y2,w2,h2):
    if (x < (x2 + w2) and (x + w) > x2 and y < (y2 + h2) and (h + y) > y2):                  
        gameEnd()

def giftCollisionCheck(x,y,w,h,x2,y2,w2,h2):
    global giftsCollected, giftX, giftY
    if (x < (x2 + w2) and (x + w) > x2 and y < (y2 + h2) and (h + y) > y2):                  
        giftsCollected += 1
        giftX += 1000
        giftY = random.randint(0, 700)

def gameEnd():
    global userText
    xmasSong.stop()
    gameEnded = True
    while gameEnded == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    userText = userText[:-1]
                elif event.key == pygame.K_RETURN:
                    print("Thank you for playing", userText[11:])
                    pygame.quit()
                else:
                    userText += event.unicode

        nameEntryFont = pygame.font.SysFont("comicsansms", 40)
        nameEntryBox = nameEntryFont.render(userText, True, GREEN)
        SCREEN.fill(WHITE)
        SCREEN.blit(nameEntryBox, (0,0))
        pygame.display.update()
        clock.tick(30)

def gameLoop():
    xmasSong.play()
    global giftX, giftY    
    SleighX, SleighY, CometX, CometY, giftX, giftY = 200, 200, 1300, 500, 1000, 350
    gamePlaying = True
    while gamePlaying == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            SleighX -= 20
        if keys[pygame.K_RIGHT]:
            SleighX += 20
        if keys[pygame.K_UP]:
            SleighY -= 20
        if keys[pygame.K_DOWN]:
            SleighY += 20
        if keys[pygame.K_p]:
            pause()


        pygame.mouse.set_visible(False)
        mouseLoc = pygame.mouse.get_pos()
        SCREEN.blit(gameBackground,(0,0))
        SCREEN.blit(sleighImg, (mouseLoc[0] - 111, mouseLoc[1] - 54))
        SCREEN.blit(cometImg, (CometX,CometY))
        SCREEN.blit(giftImg, (giftX, giftY))

        for i in range(len(allSnowLocations)):
            pygame.draw.circle(SCREEN, WHITE, (allSnowLocations[i][0], allSnowLocations[i][1]), 5)
            allSnowLocations[i][1] += 2
            if allSnowLocations[i][1] > 700:
                allSnowLocations[i][1] = 0

        CometX -= 10 + (2 * giftsCollected)
        if CometX < -120:
            CometX = 1300
            CometY = random.randint(0, 700)

        giftX -= 20
        if giftX < -120:
            giftY = random.randint(0, 700)
            giftX = 1300
        
        print (giftY)
        scoreData() 
        cometCollisionCheck(CometX,CometY,105,54,mouseLoc[0]-111,mouseLoc[1]-54,223,108)
        giftCollisionCheck(giftX,giftY,65,64,mouseLoc[0]-111,mouseLoc[1]-54,223,108)
        pygame.display.update()
        clock.tick(30)

snowBallLocations()
gameLoop()
