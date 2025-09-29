#!/usr/bin/python3
"""
This module provides a function that returns the dictionary
representation of an object's attributes.
"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple object"""
    return obj.__dict__
