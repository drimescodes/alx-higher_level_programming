#!/usr/bin/python3
"""
A function that returns a list of lists of integers representing the Pascal’s
triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        pascal = [[1], [1, 1]]
        for i in range(1, n - 1):
            row = [1]
            for j in range(0, len(pascal[i]) - 1):
                row.append(pascal[i][j] + pascal[i][j + 1])
            row.append(1)
            pascal.append(row)
        return pascal
