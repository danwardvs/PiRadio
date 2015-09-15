import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()


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
text = basicFont.render('Freq:', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = 100
textRect.centery = 20

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw the text's background rectangle onto the surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

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
