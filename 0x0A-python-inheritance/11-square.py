#!/usr/bin/python3
"""Module containing `Square` class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Extends class `Rectangle` and defines a square
    with width and height equal to size"""

    def __init__(self, size):
        """Initializes a `Square` object with size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """`str`: Returns a string representation of the square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
