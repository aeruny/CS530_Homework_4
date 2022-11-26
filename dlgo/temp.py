# Part 4
# game.py
from dlgo.goboard_slow import Board
from dlgo import gotypes
import time
import random

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
    None: '. ',
    gotypes.Player.black: 'x ',
    gotypes.Player.white: 'o ',
}

def print_board(board):
    for row in range(board.num_rows, 0, -1):
        bump = " " if row <= 9 else ""
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(gotypes.Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print('%s%d %s' % (bump, row, ''.join(line)))
    print('   ' + ' '.join(COLS[:board.num_cols]))

def main():
    candidates = []
    board = Board(19, 19)
    for row in range(1, board.num_rows):
        for col in range(1, board.num_cols):
            candidates.append(gotypes.Point(row, col))
    cnt = 0
    while True:
        player = gotypes.Player.black if cnt % 2 == 0 else gotypes.Player.white
        cnt += 1
        board.place_stone(player, random.choice(candidates))
        time.sleep(1.0)
        print(chr(27) + "[2J")
        print_board(board)
        print()

if __name__ == '__main__':
    main()
