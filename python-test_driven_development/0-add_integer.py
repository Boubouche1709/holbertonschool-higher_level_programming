#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers after validating their types.

    Args:
        a (int | float): The first number
        b (int | float, optional): The second number, defaults to 98

    Returns:
        int: The addition of a and b, both casted to integers if they are float

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
