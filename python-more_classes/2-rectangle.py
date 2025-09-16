#!/usr/bin/python3
"""Module 0-rectangle
Defines an empty Rectangle class.
"""


class Rectangle:
    """Rectangle is an empty class that defines a rectangle structure.
    This class currently does not implement any attributes or methods.
    It serves as a placeholder or base for future rectangle-related logic.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self)
    return self.__width

    @property
    def height(self)
    return sel.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value)
    if not isinstance(value int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = height

    def area(self)
    return self.__width * self.__height

    def perimeter(self)
    if self.__width == 0 or self.__height == 0:
        return 0
    return (2 * (self.__height + self.__width))
