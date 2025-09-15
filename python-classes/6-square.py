#!/usr/bin/python3
"""Module 6-square
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
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square. Must be an integer >= 0.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            int: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return

        for index in range(self.__position[1]):
            print()

        for index in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
