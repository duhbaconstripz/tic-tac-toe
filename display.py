import pygame, sys
import numpy as np

pygame.init()


#Size of the window
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

LINE_COLOR = (173,216,230) 

#Dark Green screen fill 
SCREEN_FILL = (1, 50, 32) 

#Board Rows and Columns 
BOARD_ROWS = 3
BOARD_COLS = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
screen.fill(SCREEN_FILL)
pygame.display.update()

board = np.zeros((BOARD_ROWS, BOARD_COLS))


#function to draw lines for the tic-tac-toe grid
def grid():
    #horizontal lines 
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600,200), LINE_WIDTH )
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600,400), LINE_WIDTH )

    #vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH )
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400,600), LINE_WIDTH )


def draw_board():
    grid()

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

grid()

player = 1
#while loop to keep game running (mainloop)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1

                print(board)


    pygame.display.update()