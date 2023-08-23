################################################################
# File: constants.py
# Version: 0.2 (23 AUg 23)
# Remarks: Holds all the constants used in the game.
#          Added the CROWN constant as an image from png
################################################################

import pygame

# Board Specific
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# Piece Specific
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Hail to the King
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44,25))


