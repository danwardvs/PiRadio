import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
frequency = 100.0

upButton = Rect(220,10,90,60)
downButton = Rect(220,90,90,60)
playButton = Rect(220,170,90,60)

# set up the window
windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Hello world!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

# set up the text
text = basicFont.render('Freq:' + str(frequency), True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = 110
textRect.centery = 120

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw the text's background rectangle onto the surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
pygame.draw.rect(windowSurface, BLACK, upButton)
pygame.draw.rect(windowSurface, BLACK, downButton)
pygame.draw.rect(windowSurface, BLACK, playButton)

# draw the text onto the surface
windowSurface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if upButton.collidepoint(x,y):
                ##pygame.quit()
                ##sys.exit()
                frequency = frequency + 0.1

            if downButton.collidepoint(x,y):
                ##pygame.quit()
                ##sys.exit()
                frequency = frequency - 0.1
                
    text = basicFont.render('Freq:' + str(frequency), True, WHITE, BLUE)
    
    # draw the text onto the surface
    windowSurface.blit(text, textRect)

    # draw the window onto the screen
    pygame.display.update()
    
            
            
            
