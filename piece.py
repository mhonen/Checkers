###############################################################################
#
# File: piece.py
# Version: 0.1 (23 Aug 23)
# Remarks: Piece class that holds all the attributes of each piece on the board
###############################################################################

import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY
class Piece:
    #Set padding and outline size of each piece
    PADDING = 10
    OUTLINE = 2
    #Constructor
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        #Determine direction IAW piece color 
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1
        
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    #Method that is called during class initialization.  Determines where on the board
    #The piece is placed.    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    # If piece makes it to the other side of the board, make it a king piece.    
    def make_king(self):
        self.king = True
    
    # Draw piece graphic on the board using pygame's circle method.    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
    # ALlows the use of string to define a piece object.    
    def __repr__(self):
        return str(self.color)