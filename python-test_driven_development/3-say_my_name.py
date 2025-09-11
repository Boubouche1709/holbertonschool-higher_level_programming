#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a given number.
It validates the matrix structure and ensures all elements are numbers.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and returns a new matrix.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The number to divide each element by.

    Returns:
        list of lists: A new matrix with each element divided and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        >>> matrix_divided([[9, 12]], 3)
        [[3.0, 4.0]]
        >>> matrix_divided([[1.5, 2.5], [3.5, 4.5]], 2)
        [[0.75, 1.25], [1.75, 2.25]]
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
