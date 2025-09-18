#!/usr/bin/python3
"""This module defines an instance of the specified class"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a_class that inherited, or False."""
    return isinstance(obj, a_class) and type(obj)is not a_class
