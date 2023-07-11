#!/usr/bin/python3
"""Module containing `MyList` class"""


class MyList(list):
    """A class tha inherits the `list` class"""

    def __init__(self, *args):
        """Initalizes a MyList instance object"""
        super().__init__(*args)

    def print_sorted(self):
        """Prints a MyList list sorted in ascending order"""
        print(sorted(self))
