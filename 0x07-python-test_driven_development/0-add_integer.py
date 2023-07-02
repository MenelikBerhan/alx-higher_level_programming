#!/usr/bin/python3
"""
'0-add_integers' module.

This module contains add_integer function which sums two
numbers that are either an integer or a float.
"""


def add_integer(a, b=98):
    """Adds two numbers. Numbers can be float or integer.
    If number is float it will be cast to integer before addition

    Args:
        a (`int` or `float`): first integer
        b (`int` or `float`, optional): second integer

    Returns (`int`): an integer sum of the two numbers

    Raises:
        TypeError: if either a or b is not neither an integer or a float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
