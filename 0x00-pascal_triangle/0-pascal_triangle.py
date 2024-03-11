#!/usr/bin/python3
"""
function pascal_triangle
that
returns a list of lists of integers representing the Pascal’s triangl of n.
"""


def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    pascal = []
    if (n <= 0):
        return (pascal)
    else:
        if n == 1:
            pascal = [1]
            return pascal
        else:
            for row in range(n):
                rw_lst = [1] * (row + 1)
                for c in range(1, row):
                    rw_lst[c] = pascal[row - 1][c - 1] + pascal[row - 1][c]
                pascal.append(rw_lst)

    return (pascal)
