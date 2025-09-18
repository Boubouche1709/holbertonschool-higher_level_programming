#!/usr/bin/python3
"""This module defines a subclass of list a method to print sorted elements."""


class MyList(list):
    """MyList is a subclass of that adds a method to print the list sorted."""

    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        print(sorted(self))

my_list = MyList()
