#!/usr/bin/python3


from abc import ABC, abstractmethod
import math


# Abstract base class Shape
class Shape(ABC):

    # Abstract method to calculate area
    @abstractmethod
    def area(self):
        pass

    # Abstract method to calculate perimeter
    @abstractmethod
    def perimeter(self):
        pass


# Concrete class Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * abs(self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


# Concrete class Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Function using duck typing to print shape info
def shape_info(shape):
    # No type checking — we assume the object has area and perimeter methods
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
