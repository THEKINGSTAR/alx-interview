#!/usr/bin/python3
"""
N queens,
projectis a classic problem
in
computer science and mathematics
"""


import sys


def is_safe(board, row, col, n):
    """
    Check if there is a queen in the same column
    Check upper diagonal on left side
    Check upper diagonal on right side
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


def solve_nqueens_util(board, col, n, solutions):
    """
    take in the board the row the N and solutions and
    return
    TRUE
    or
    false
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0

    return res


def solve_nqueens(n):
    """
     N queens puzzle is the challenge
     of
     placing N non-attacking queens
     on an N×N chessboard.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


def main():
    """
    MAIN ENTRY POINT AND CHECK FOR THE INPUT
    AND
    CORRECT USAGE OF THE PROGRAM
    """
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

    solve_nqueens(n)


if __name__ == "__main__":
    main()
