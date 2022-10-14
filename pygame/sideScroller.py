import sys, random, pygame
from turtle import window_height, window_width
from pygame.locals import *

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RED = "#c1121f"
GREEN = (15, 155, 30)
BLUE = "#90e0ef"
GREY = "#b2967d"
SUN = "#f6bd60"
BACKGROUND="#e6beae"

window_width = 400
window_height = 300

CHARACTER = "#000000"

FPS = 60
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('WEEEEEE')

def main() :
    loop = True

    BLDGSTDX = window_width/2
    BLDGSTDY = window_height-100
    SUNSTDX = BLDGSTDX
    SUNSTDY = 20
    characterCenter = (int(window_width/2), (window_height-40))
    characterX = characterCenter[0]-25
    characterY = characterCenter[1]-35
    characterWidth = 50
    characterHeight = 70
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        
        pressed = pygame.key.get_pressed()
        if(pressed[K_RIGHT] or pressed[K_d]):
            BLDGSTDX -= 2
            SUNSTDX -= .2
        if(pressed[K_LEFT] or pressed[K_a]):
            BLDGSTDX += 2
            SUNSTDX += .2
        if(pressed[K_UP] or pressed[K_w]):
            characterY -= 1
        if(pressed[K_DOWN] or pressed[K_s]):
            characterY += 1

        if(characterY+characterHeight > window_height):
            characterY = characterY-3
        if(characterY+characterHeight < window_height-32):
            characterY = characterY+3

        if(pressed[K_LSHIFT] or pressed[K_RSHIFT]):
            characterHeight = characterHeight/2
        if(pressed[K_LCTRL] or pressed[K_RCTRL]):
            characterHeight = characterHeight*2
        
        if(characterHeight > 50):
            characterHeight = 50
        if(characterHeight < 15):
            characterHeight = 15

        #PROCESSING
        rectangle1 = pygame.Rect(BLDGSTDX-100, BLDGSTDY+20, 150, 270)
        rectangle2 = pygame.Rect(BLDGSTDX-250, BLDGSTDY-40, 50, 230)
        rectangle3 = pygame.Rect(20, 50, 50, 70)
        # floorEllipse = pygame.Rect(-35, window_height-30, 600, 40)
        character = pygame.Rect(characterX, characterY, characterWidth, characterHeight)
        
        #DISPLAY
        window.fill(BACKGROUND)
        pygame.draw.circle(window, SUN, (SUNSTDX, SUNSTDY), 100)
        pygame.draw.rect(window, (120, 40, 20), rectangle1)
        pygame.draw.rect(window, GREEN, rectangle2)
        pygame.draw.rect(window, BLUE, rectangle3)
        pygame.draw.circle(window, GREY, (window_width/2, window_height+560), 600)
        # pygame.draw.ellipse(window, GREY, floorEllipse)
        pygame.draw.rect(window, CHARACTER, character)
        pygame.display.update()
        fpsClock.tick(FPS)

main()