#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    """is_safe.

    :param board:
    :param row:
    :param col:
    :param n:
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n):
    """solve_nqueens.

    :param board:
    :param row:
    :param n:
    """
    solution = []
    if row == n:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
    else:
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_nqueens(board, row + 1, n)
                board[row][col] = 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)
