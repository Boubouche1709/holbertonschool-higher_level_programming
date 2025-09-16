#!/usr/bin/python3
"""Module 0-rectangle
Defines an empty Rectangle class.
"""


class Rectangle:
    """Rectangle is an empty class that defines a rectangle structure.
    This class currently does not implement any attributes or methods.
    It serves as a placeholder or base for future rectangle-related logic.
    """

    number_of_instance = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def area(self)
    return self.__width * self.__height

    def perimeter(self)
    if self.__width == 0 or self.__height == 0:
        return 0
    return (2 * (self.__height + self.__width))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol_str = str(self.print_symbol)
        rows = [symbol_str * self.__width for i in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.perimeter() >= rect_2.perimeter():
            return rect_1
        else:
            return rect_2
