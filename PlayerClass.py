## Creating a player Class

import pygame
from pygame.locals import *
import Pyganim
pygame.init()

class Player:
    def __init__(self, x, y, hp, dmg, abilityUnlock):
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
        if self.abilityUnlock ==  0:
            pass
        else:
            pass

    def dmgIncrease(self, dmgModify)
        self.dmg = self.dmg + dmgModify

    def dmgTake(self, dmgDealt):
        self.hp = self.hp - dmgDealt



SpaceLizard = Player(100, 350, 100, 10)

class Snake:
    def __init__(self, x, y, hp, dmg, abilityType)
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
        self.abilityType = abilityType
        if self.abilityType = "Null":
            pass
        elif self.abilityType = "Mace":
            self.Mace = True

    def dmgTake(self, dmgDealt):
        self.hp = self.hp - dmgDealt
