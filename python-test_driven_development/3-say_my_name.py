#!/usr/bin/python3
"""
This module provides a function to print a formatted name using first and last name.
It ensures that both inputs are strings and raises appropriate errors otherwise.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the user's full name.

    Args:
        first_name (str): The first name of the user.
        last_name (str, optional): The last name of the user. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
