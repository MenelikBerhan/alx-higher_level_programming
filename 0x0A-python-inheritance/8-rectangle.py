#!/usr/bin/python3
"""Module containing `Rectangle` class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Extends class BaseGeometry and defines a Rectangle
    with width and height"""

    def __init__(self, width, height):
        """Initializes a `Rectangle` object with width and height"""
        super().integer_validator("width", width)
        # BaseGeometry.integer_validator(self, "width", width)
        super().integer_validator("height", height)
        # BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
