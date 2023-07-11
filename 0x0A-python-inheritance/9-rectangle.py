#!/usr/bin/python3
"""Module containing `Rectangle` class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Extends class BaseGeometry and defines a Rectangle
    with width and height"""

    def __init__(self, width, height):
        """Initializes a `Rectangle` object with width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """`int`: Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """`str`: Returns a string representation of the rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
