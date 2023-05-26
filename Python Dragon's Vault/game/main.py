# Imports and Functions
import pygame
import sys
import os
import math
from pygame import mixer
from pygame.locals import *
from buttonObject import ButtonObject

pygame.init()
pygame.font.init()
pygame.mixer.init()
mainClock = pygame.time.Clock()

# ---------------------------------------------------------------------------------------------------- #

# Window Variables
WIDTH = 1052
HEIGHT = 1024
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('Consolas', 20)
color = (74, 74, 74)
clock = pygame.time.Clock()

# Images
start_image = pygame.image.load('./game/pictures/Start.jpg')
exit_image = pygame.image.load('./game/pictures/Exit.jpg')
start_button = pygame.transform.scale(start_image, (181, 100))
exit_button = pygame.transform.scale(exit_image, (181, 100))

BG_Image = pygame.image.load('./game/pictures/Official_Dragon_Lair.JPG')
BG_Image = pygame.transform.scale(BG_Image, (WIDTH, HEIGHT))

BG_Image_Menu = pygame.image.load('./game/pictures/Main_Menu.jpg')
BG_Image_Menu = pygame.transform.scale(BG_Image_Menu, (WIDTH, HEIGHT))

BG_Win = pygame.image.load('./game/pictures/Success.jpg')
BG_Win = pygame.transform.scale(BG_Win, (WIDTH, HEIGHT))

BG_Lose = pygame.image.load('./game/pictures/Lost.jpg')
BG_Lose = pygame.transform.scale(BG_Lose, (WIDTH, HEIGHT))

Check = pygame.image.load('./game/pictures/x.png')
Check = pygame.transform.scale(Check, (50, 25))

# Extra Variables
mixer.music.load('./game/sound/all.ogg')
mixer.music.play(-1)

# Main Menu Functions
def draw_text(text, font, color, surface, x, y):
    TEXT_Object = font.render(text, 1, color)
    TEXT_Rect = TEXT_Object.get_rect()
    TEXT_Rect.topleft = (x, y)
    surface.blit(TEXT_Object, TEXT_Rect)

CLICK = False

# ---------------------------------------------------------------------------------------------------- #

# Game Screen
def game():
    running = True
    WINDOW.blit(BG_Image, (0, 0))
    draw_text('Game', font, (255, 255, 255), WINDOW, 20, 20)
    timer_sec = -0
    timer_view = 45
    buttons = 12
    
    pygame.display.update()
    
    # Item Locations/Transparent Buttons
    gear_button = ButtonObject((224, 625, 42, 32), (75, 120))
    helmet_button = ButtonObject((832, 692, 55, 68), (75, 170))
    crown_button = ButtonObject((670, 640, 57, 50), (75, 219))
    platter_button = ButtonObject((574, 785, 50, 45), (75, 267))
    chest_button = ButtonObject((494, 325, 100, 45), (75, 317))
    cuff_button = ButtonObject((801, 835, 36, 36), (75, 392))
    artifact_button = ButtonObject((544, 376, 42, 42), (75, 442))
    tail_button = ButtonObject((288, 826, 200, 60), (75, 515))
    jewlery_button = ButtonObject((335, 490, 39, 85), (75, 589))
    liberty_button = ButtonObject((231, 570, 70, 58), (75, 663))
    thorn_button = ButtonObject((489, 77, 54, 140), (75, 740))
    star_button = ButtonObject((607, 300, 60, 68), (75, 788))

    # All Item Location Buttons Together
    all_buttons = [gear_button, helmet_button, crown_button, platter_button, chest_button, cuff_button, artifact_button, tail_button, jewlery_button, liberty_button, thorn_button, star_button]
    
    # Timer 
    while running:
        WINDOW.blit(BG_Image, (0, 0))
        draw_text('Game', font, (255, 255, 255), WINDOW, 20, 20)
        timer_sec += 1
        timer_view = 60 - math.floor(timer_sec / 60)
        draw_text(str(timer_view), font, (255, 255, 255), WINDOW, 1000, 20)
        mouse_position = pygame.mouse.get_pos()
        mx, my = pygame.mouse.get_pos()
        
        # Game Lost if Time Hits 0
        if timer_view <= 0:
            losing_screen()

        # Exit Game to Main Menu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

            # Button Check Offs & Timer Shortage
            if event.type == MOUSEBUTTONDOWN:
                clicked = False
                for button in all_buttons:
                    if button.checkPress((mx, my)) == True:
                        clicked = True
                        buttons -= 1
                        
                if clicked == False:
                    timer_sec += 600

            # Deploy Winning Screen            
            if buttons <= 0:
                winning_screen()

        for button in all_buttons:
            button.update(WINDOW)
            
        pygame.display.update()  
        mainClock.tick(60)                                        
 
# ---------------------------------------------------------------------------------------------------- #

# Winning Screen
def winning_screen():
    while True:
        WINDOW.blit(BG_Win, (0, 0))
        draw_text('Game Won', font, (255, 255, 255), WINDOW, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)

# ---------------------------------------------------------------------------------------------------- #

# Losing Screen
def losing_screen():
    while True:
        WINDOW.blit(BG_Lose, (0, 0))
        draw_text('Game Lost', font, (255, 255, 255), WINDOW, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)

# ---------------------------------------------------------------------------------------------------- #

# Main Menu
def main_menu():
    CLICK = False

    while True:
        WINDOW.blit(BG_Image_Menu, (0, 0))
        draw_text('Main Menu', font, (255, 255, 255), WINDOW, 20, 20)
        mx, my = pygame.mouse.get_pos()

        # Main Menu Buttons
        button_1 = pygame.Rect(WINDOW.blit(start_button, (439.52, 460)))
        button_2 = pygame.Rect(WINDOW.blit(exit_button, (439.52, 600)))
        
        # Play Game
        if button_1.collidepoint((mx, my)):
            if CLICK:
                game()
                
        # Close Game
        if button_2.collidepoint((mx, my)):
            if CLICK:
                exit()

        # Main Menu Running
        CLICK = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    CLICK = True

        pygame.display.update()
        mainClock.tick(60)

print('Running')
main_menu()

# ---------------------------------------------------------------------------------------------------- #

