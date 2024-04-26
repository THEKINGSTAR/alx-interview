#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""


def old_rotate_2d_matrix(matrix):
    """
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empt
    [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]
    ==
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    row = len(matrix[0]) - 1
    colmn = len(matrix) - 1
    n = row
    new_matrix = [[0 for _ in range(row)] for _ in range(colmn)]
    # print(f"MATRINX ROW IS: {row}, COMLUMN IS: {colmn}")
    x = 0
    y = 0
    for x in range(colmn):
        for y in range(row):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp

        # print(f"NEW MATRIX {new_matrix}")


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)
    # Rotate each layer of the matrix starting from the outermost layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
