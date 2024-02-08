#!/usr/bin/python3
"""N Queens problem"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    Args:
        board: list of lists containing the placement of queens
        row: current row
        col: current column
        n: number of queens to be placed
    Returns:
        True if it's safe, False otherwise
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """
    Solve the N Queens problem using backtracking
    Args:
        board: list of lists containing the placement of queens
        col: current column
        n: number of queens to be placed
    Returns:
        True if all queens are placed, False otherwise
    """
    if col >= n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, n) or res
            board[i][col] = 0

    return res


def print_solution(board):
    """
    Print the placement of queens in the board
    Args:
        board: list of lists containing the placement of queens
    """
    print([[i, row.index(1)] for i, row in enumerate(board)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)
