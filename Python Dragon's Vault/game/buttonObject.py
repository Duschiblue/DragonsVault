# Imports and Functions
import pygame
from pygame.locals import *
from os import path
CurrentPath = path.dirname(__file__)
game_folder = CurrentPath
img_folder = path.join(game_folder, 'pictures')

# ----------------------------------------------------------------------------------------------------#

# Variables
Check = pygame.image.load(path.join(img_folder,"x.png"))
Check = pygame.transform.scale(Check, (50, 25))

# ----------------------------------------------------------------------------------------------------#

# Object Functions for Game
class ButtonObject:
    def __init__(self, buttonPos, checkPos) -> None:
        self.rect = pygame.Rect(buttonPos)
        self.checkPos = checkPos
        self.pressed = False

    def checkPress(self, mousePos):
        if self.rect.collidepoint(mousePos):
            self.pressed = True  
            return True 
        else: 
            return False

    def update(self, WINDOW):
        if (self.pressed):
            pygame.Rect(WINDOW.blit(Check, self.checkPos))

# ----------------------------------------------------------------------------------------------------#
