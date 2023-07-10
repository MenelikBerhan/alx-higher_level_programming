#!/usr/bin/python3
"""Module containing `MyList` class"""


class MyList(list):
    """A class tha inherits the `list` class"""
    def print_sorted(self):
        """Pritns a MyList list sorted in ascending order"""
        print(sorted(self))
