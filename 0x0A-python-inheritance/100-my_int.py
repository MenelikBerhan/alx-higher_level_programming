#!/usr/bin/python3
"""Module containing `MyInt` class"""


class MyInt(int):
    """My integer class that extends the `int` class"""

    def __ne__(self, other):
        """`bool`: checks if self is equal to other. It is a reverse
        of proper __ne__ that checks if self is not equal to other"""
        return super().__eq__(other)

    def __eq__(self, other):
        """`bool`: checks if self is not equal to other. It is a reverse
        of proper __eq__ that checks if self is equal to other"""
        return super().__ne__(other)
