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

    i = 0
    length = len(text)
    while i < length:
        ch = text[i]
        # Normal character
        if ch not in ".?:":
            print(ch, end="")
            i += 1
            continue

        # If it's punctuation
        print(ch, end="")
        print("\n")
        i += 1

        # Skip spaces right after punctuation
        while i < length and text[i] == " ":
            i += 1
