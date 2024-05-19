#!/usr/bin/python3
"""
N queens,
projectis a classic problem
in
computer science and mathematics
"""


import sys


def is_safe(board, row, col, N):
    """
    Check if there is a queen in the same column
    Check upper diagonal on left side
    Check upper diagonal on right side
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board: list, row: int, N: int, solutions: list) -> bool:
    """
    take in the board the row the N and solutions and
    return
    TRUE
    or
    false
    """
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append(j + 1)
        solutions.append(solution)
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0


def solve_nqueens(N):
    """
     N queens puzzle is the challenge
     of
     placing N non-attacking queens
     on an N×N chessboard.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(' '.join(map(str, solution)))


if __name__ == "__main__":
    """
    MAIN ENTRY POINT AND CHECK FOR THE INPUT
    AND
    CORRECT USAGE OF THE PROGRAM
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
