###############################################################################
# File: board.py
# Version: 0.1 (23 Aug 23)
# Class: Board
# Remarks:  Creates the board used for the game.
###############################################################################

import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from .piece import Piece

class Board:
    # Constructor
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        # Create the board
        self.create_board()
    # Draws the board squares to the screen.
    def draw_squares(self, win):
        # FIll window screen
        win.fill(BLACK)
        #Now add the Red squares.
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    # Called from constructor. Populates the board list.            
    def create_board(self):
        for row in range(ROWS):
            #Append Column info to rows.
            self.board.append([])
            # Creates each individual piece.
            for col in range(COLS):
                # If col does not fall within parameters, append 0 or nothing.
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    # Draw Square to the screen.                
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
                    
    