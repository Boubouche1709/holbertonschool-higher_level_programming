#!/usr/bin/python3
"""
This module provides a function to append a text file (UTF8)
and returns the number of characters written.
"""


def append_write(filename="", text=""):
    """Append a text and returns the number of characters written."""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
