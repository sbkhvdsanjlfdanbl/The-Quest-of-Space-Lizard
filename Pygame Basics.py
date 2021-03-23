import pygame, random, math
pygame.init()

HEIGHT, WIDTH = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

#Hex Code R  G  B Colour pallette
BLACK  = (  0,  0,  0)
WHITE  = (255,255,255)
ORANGE = (255, 165, 0)
AQUA   = (0, 255, 255)

clock = pygame.time.Clock()
score = 0

def clickLocation(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def collisionCheck(x, y, balloonNumber):
    global score
    bx = bData[balloonNumber][3]
    by = bData[balloonNumber][4]
    bSize = bData[balloonNumber][6]
    if clickLocation(x,y,bx,by) < bSize:
        del bData[balloonNumber]
        score += 1

def quitGame():
    pygame.quit()
    quit()

def dataForBalloons():
    global bData
    bData = []
    for i in range(1000):
        R = random.randrange(0,255)
        B = random.randrange(0,255)
        G = random.randrange(0,255)    
        xLoc = random.randrange(0, 1000)
        yLoc = random.randrange(0, 800)
        Size = random.randrange(30, 80)
        bData.append([R,G,B, xLoc, yLoc, Size, i])   

def displayScore():
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render("Popped: " + str(score), True, BLACK)
    SCREEN.blit(text, (0,0))
    
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
            pygame.draw.circle(SCREEN, [bData[i][0],bData[i][1],bData[i][2]] ,(bData[i][3] ,bData[i][4]) ,bData[i][5])
            bData[i][4] -= 1
             

        displayScore()

        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        
        pygame.display.update()
        clock.tick(15)
        #                             [R, G, B]
        #   pygame.draw.circle(SCREEN, COLOUR (X, Y), SIZE)
       
dataForBalloons()
gameLoop()
        
