#!/usr/bin/python3
"""
This module provides a function to print a square of a given size using the '#' character.
It validates the input to ensure it is a non-negative integer.
"""

def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The length of the sides of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
