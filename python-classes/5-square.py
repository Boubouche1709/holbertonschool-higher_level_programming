#!/usr/bin/python3
"""Module 5-square
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

        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square.

        Returns:
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for index in range(self.__size):
                print("#" * self.__size)
