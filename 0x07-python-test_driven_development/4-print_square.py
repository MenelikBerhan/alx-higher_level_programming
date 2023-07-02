#!/usr/bin/python3
"""
'4-print_square' module.

This module contains `print_square` function that prints squares
using `#` character.
"""


def print_square(size):
    """Prints prints squares using `#` character.

    Args:
        size (`int`): the size length of the square

    Raises:
        TypeError: size is not an integer
        ValueError: if size is less than zero
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
