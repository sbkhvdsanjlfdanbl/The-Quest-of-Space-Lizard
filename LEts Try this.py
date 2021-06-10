import pygame
from pygame.locals import *
import Pyganim

pygame.init()
windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Pyganim Basic Demo')

boltAnim = Pyganim.PygAnimation([('bolt1.png', 100000000000),
                                 ('bolt2.png', 100000000000),
                                 ('bolt3.png', 100000000000),
                                 ('bolt4.png', 100000000000),
                                 ('bolt5.png', 100000000000),
                                 ('bolt6.png', 100000000000),
                                 ('bolt7.png', 100000000000),
                                 ('bolt8.png', 100000000000),
                                 ('bolt9.png', 100000000000),
                                 ('bolt10.png', 100000000000)])
boltAnim.play()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    windowSurface.fill((100, 50, 50))
    boltAnim.blit(windowSurface, (100, 50))
    pygame.display.update()
