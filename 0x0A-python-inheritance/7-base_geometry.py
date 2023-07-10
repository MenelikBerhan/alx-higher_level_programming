#!/usr/bin/python3
"""Module containing `BaseGeometry` class"""


class BaseGeometry:
    """Class BaseGeometry that defines a basic gemoetric shape"""

    def area(self):
        """Raises an `Exception`"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates `value` by checking if it is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
