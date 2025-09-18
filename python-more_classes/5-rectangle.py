#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Rectangle is an empty class that defines a rectangle structure.
    This class currently does not implement any attributes or methods.
    It serves as a placeholder or base for future rectangle-related logic.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.width))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.height)

    def __del__(self):
        print("Bye rectangle...")
