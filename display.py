import pygame, sys
import numpy as np

pygame.init()

#Size of the window
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

LINE_COLOR = (173,216,230) 
CIRCLE_COLOR = (255,0,0)
X_COLOR = (255,255,0)
#Dark Green screen fill 
SCREEN_FILL = (1, 50, 32) 

#Circle dimensions 
CIRCLE_RADIUS = 60 
CIRCLE_WIDTH = 10

#Cross dimensions 
CROSS_WIDTH = 15
SPACE = 55

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


def draw_pieces():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200  + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col]==2:
                pygame.draw.line(screen, X_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


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

def check_win(player):
    #check vertical win 
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_line(col, player)
            return True

    #check for horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_line(row, player)
            return True 

    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diag(player)
        return True

    #dsc diagonal win check 
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diag(player)
        return True

    return False



def draw_vertical_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH- 15, posY), 15)

def draw_asc_diag(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH - 15, 15), 15)

def draw_desc_diag(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15,15), (WIDTH -15, HEIGHT - 15), 15)

def restart():
    screen.fill(SCREEN_FILL)
    grid()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
    

grid()

player = 1
game_over =False
#while loop to keep game running (mainloop)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                draw_pieces()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                restart()
                game_over = False
        

    pygame.display.update()