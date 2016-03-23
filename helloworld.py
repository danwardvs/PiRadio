import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
frequency = 100.0

upButton = Rect(10,215,50,25)
downButton = Rect(70,215,50,25)
playButton = Rect(130,215,50,25)

# set up the window
windowSurface = pygame.display.set_mode((320, 240), pygame.FULLSCREEN, 32)
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
label = basicFont.render('+     -     >', True, BLACK)
labelRect = label.get_rect()
labelRect.centerx = 95
labelRect.centery = 225

text = basicFont.render('Freq:' + str(frequency), True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = 110
textRect.centery = 120

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw the text's background rectangle onto the surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 2, textRect.top - 2, textRect.width + 4, textRect.height + 4))
pygame.draw.rect(windowSurface, BLUE, upButton)
pygame.draw.rect(windowSurface, BLUE, downButton)
pygame.draw.rect(windowSurface, RED, playButton)

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

            if playButton.collidepoint(x,y):
                pygame.quit()
                sys.exit()

                
    text = basicFont.render('Freq:' + str(frequency), True, WHITE, BLUE)
    
    # draw the text onto the surface
    windowSurface.blit(text, textRect)
    windowSurface.blit(label, labelRect)

    # draw the window onto the screen
    pygame.display.update()
    
            
            
            
