#!/usr/bin/python3
"""
This module defines a function (`matrix_divided`) that takes two arguments, a
matrix and a divisor, and returns the result of the division of all elements of
the matrix by the divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Args:
        matrix (list): Matrix to be divided
        div (int): Divisor
    Returns:
        The result of the division
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats or if
        div is not an integer/float
        ZeroDivisionError: If div is 0
    """
    if not (
        isinstance(matrix, list)
        and matrix
        and all(
            [
                all([isinstance(x, int) or isinstance(x, float) for x in row])
                for row in matrix
            ]
        )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all([len(matrix[0]) == len(row) for row in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
