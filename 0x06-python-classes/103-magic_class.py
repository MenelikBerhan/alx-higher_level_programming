#!/usr/bin/python3
"""A `MagicClass` based on a byte code."""
import math


class MagicClass():
    """Defines a circle with radius\n
    Attributes:
        _MagicClass__radius (`int` or `float`): radius of the cirlce\n
    """
    def __init__(self, radius=0):
        """Initializes a `MagicClass` cirlce with radius\n
        Args:
            radius (`int` or `float`): radius of the cirlce\n
        Raises:
            TypeError: if radius is not either an integer or a float
        """
        self._MagicClass__radius = 0

        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError('radius must be a number')

        self._MagicClass__radius = radius

    def area(self):
        """`float`: area of the circle"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """`float`: circumference of a circle"""
        return 2 * math.pi * self._MagicClass__radius
