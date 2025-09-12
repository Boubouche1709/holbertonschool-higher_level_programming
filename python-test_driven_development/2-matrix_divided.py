#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number, rounded to 2 decimals.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int | float): The divisor.

    Returns:
        list of lists of float: A new matrix with divided values.

    Raises:
        TypeError: If matrix is not a list of lists of int/float.
        TypeError: If each row of the matrix is not the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix structure
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(
         "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Validate rows size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix
    return [[round(num / div, 2) for num in row] for row in matrix]
