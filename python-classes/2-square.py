#!/usr/bin/python3
"""Module 2-square
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
    def __init__(self, size=0):
        """Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square. Must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
