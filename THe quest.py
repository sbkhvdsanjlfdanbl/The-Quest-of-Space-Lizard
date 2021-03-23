#Libraries 
import pygame, random
pygame.init()


#Colours
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
ORANGE = [255, 165, 0]


#Variables
HEIGHT, WIDTH = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
MenuScreen = pygame.image.load("TitleScreen.png")
MenuScreen = pygame.transform.scale(MenuScreen, (WIDTH, HEIGHT))
SpaceLizard = pygame.image.load("normal.png")


#Functions
def PlayerInfo():
    global PlayerLoc
    PlayerLoc = []
    player_x = 100
    player_y = 350
    PlayerLoc.append(playerx, playery)

def menuLoop():
    menuShowing = True
    while menuShowing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        SCREEN.blit(MenuScreen,(0,0))
        button("Play"           ,10,125,255,60,ORANGE, gameLoop)     
        button("Instructions"   ,10,200,255,60,ORANGE)#,instructionsLoop)
        button("Exit"           ,10,275,255,60,ORANGE, quitGame)
        pygame.display.update()
        clock.tick(60)

def gameLoop():
    playing = True
    while playing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        SCREEN.fill(WHITE)
        SCREEN.blit(SpaceLizard, (10, 300))
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


menuLoop()      
