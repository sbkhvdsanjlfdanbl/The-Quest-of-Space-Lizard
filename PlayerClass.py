# Meant to be used to create classes for the player, enemies and player weapons. Still in progress.

import pygame
from pygame.locals import *
import Pyganim
pygame.init()


## Creating a player class

class Player:
    def __init__(self, x, y, hp, abilityUnlock):
        self.x = x
        self.y = y
        self.hp = hp
        self.abilityUnlock = abilityUnlock
        if self.abilityUnlock ==  0:
            pass
        else:
            pass

    def dmgTake(self, dmgDealt):
        self.hp = self.hp - dmgDealt


### Sword Class

class Sword:
    def __init__(self, x, y, dmg):
        self.x = x 
        self.y = y
        self.dmg = dmg
        
    def dmgIncrease(self, dmgModify):
        self.dmg = self.dmg + dmgModify
    
    def dmgDeal(self, enemyHp):
        enemyHp =- self.dmg


### Creating the snake enemy class

class Snake:
    def __init__(self, x, y, hp, dmg, abilityType):
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
        self.abilityType = abilityType
        if self.abilityType == "Null":
            pass
        elif self.abilityType == "Mace":
            self.Mace = True

    def hpAdjust(self, newHp):
        self.hp = newHp
