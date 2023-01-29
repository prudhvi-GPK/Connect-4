"""
Connect4-2p.py
Contributor: Prudhvi and Vijay.
Last Updated : 12/8/2022
"""
import sys
import math
import numpy as np
import pygame


BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board1 = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board1


def drop_piece(board1, row1, col1, piece):
    board1[row1][col1] = piece


def is_valid_location(board1, col1):
    return board1[ROW_COUNT - 1][col1] == 0


def get_next_open_row(board1, col1):
    for r_turn in range(ROW_COUNT):
        if board1[r_turn][col1] == 0:
            return r_turn


def print_board(board1):
    print(np.flip(board1, 0))


def winning_move(board1, piece):
    # Check horizontal locations for win
    for c_turn in range(COLUMN_COUNT - 3):
        for r_turn in range(ROW_COUNT):
            if board1[r_turn][c_turn] == piece and board1[r_turn][c_turn + 1] == piece and \
                    board1[r_turn][c_turn + 2] == piece and board1[r_turn][c_turn + 3] == piece:
                return True

    # Check vertical locations for win
    for c_turn in range(COLUMN_COUNT):
        for r_turn in range(ROW_COUNT - 3):
            if board1[r_turn][c_turn] == piece and board1[r_turn + 1][c_turn] == piece and \
                    board1[r_turn + 2][c_turn] == piece and \
                    board1[r_turn + 3][c_turn] == piece:
                return True

    # Check positively sloped diaganols
    for c_turn in range(COLUMN_COUNT - 3):
        for r_turn in range(ROW_COUNT - 3):
            if board1[r_turn][c_turn] == piece and board1[r_turn + 1][c_turn + 1] == piece and \
                    board1[r_turn + 2][c_turn + 2] == piece and \
                    board1[r_turn + 3][c_turn + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c_turn in range(COLUMN_COUNT - 3):
        for r_turn in range(3, ROW_COUNT):
            if board1[r_turn][c_turn] == piece and board1[r_turn - 1][c_turn + 1] == piece and \
                    board1[r_turn - 2][c_turn + 2] == piece and\
                    board1[r_turn - 3][c_turn + 3] == piece:
                return True


def draw_board(board1):
    for c_turn in range(COLUMN_COUNT):
        for r_turn in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE,
                             (c_turn * SQUARESIZE, r_turn * SQUARESIZE + SQUARESIZE,
                              SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c_turn * SQUARESIZE + SQUARESIZE / 2),
                int(r_turn * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c_turn in range(COLUMN_COUNT):
        for r_turn in range(ROW_COUNT):
            if board1[r_turn][c_turn] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c_turn * SQUARESIZE + SQUARESIZE / 2),
                    HEIGHT - int(r_turn * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board1[r_turn][c_turn] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c_turn * SQUARESIZE + SQUARESIZE / 2),
                    HEIGHT - int(r_turn * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
GAME_OVER = False
TURN = 0

pygame.init()

SQUARESIZE = 100

WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE

size = (WIDTH, HEIGHT)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not GAME_OVER:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
            posx = event.pos[0]
            if TURN == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if TURN == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", True, RED)
                        screen.blit(label, (40, 10))
                        GAME_OVER = True

            # # Ask for Player 2 Input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", True, YELLOW)
                        screen.blit(label, (40, 10))
                        GAME_OVER = True

            print_board(board)
            draw_board(board)

            TURN += 1
            TURN = TURN % 2

            if GAME_OVER:
                pygame.time.wait(3000)
