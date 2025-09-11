#!/usr/bin/python3
"""
This module provides a function that formats a text by adding two new lines
after each '.', '?' or ':' character. It also removes leading and trailing
spaces from each printed line.
"""

def text_indentation(text):
    """
    Prints a formatted version of the input text with two new lines after
    '.', '?' and ':' characters. Leading and trailing spaces are removed
    from each printed line.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    buffer = ""
    for char in text:
        buffer += char
        if char in special_chars:
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip())
