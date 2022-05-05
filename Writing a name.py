import pygame
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

HEIGHT, WIDTH = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WrittenWord = ""


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


def quitGame():
    pygame.quit()
    quit()


def textObjects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


NameLoop()
