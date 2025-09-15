#!/usr/bin/python3
"""Module 1-square
Defines a square by size Square class.
"""


class Square:
    """Square defines a geometric square.

    This class initializes a square with a given size.
    The size is stored as a private instance attribute to ensure future control
    over its type and value, which are critical for square-related computations
    such as area, perimeter, and comparisons.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size):
        """Initializes a new Square instance with the given size.

        Args:
            size: The size of the square (no type or value verification).
        """
        self.__size = size
