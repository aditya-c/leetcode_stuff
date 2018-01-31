import numpy as np

size = 4
board = np.zeros((size, size))

# backtrack


def iter(board, column):
    for row in range(board.shape[0]):
        if is_stable(board, row, column):
            board[row][column] = 1
            iter(board, column + 1)
            board[row][column] = 0
    print(board)


def is_stable(board, row, column):
    for r in range(row):
        if board[r][column] == 1:
            return False
    r = row
    c = column
    while r > -1 and c > -1:
        r -= 1
        c -= 1
    return True


iter(board, 0)
