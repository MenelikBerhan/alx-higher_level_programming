#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle():
    """Defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """`int`: Setter and Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """`int`: Setter and Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """`int`: Returns area of the Rectangle"""
        return self.height * self.width

    def perimeter(self):
        """`int`: Returns circumference of the Rectangel"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """`str`: string representation of a Rectangel"""
        if self.height == 0 or self.width == 0:
            return ""
        printable = ""
        row_str = '#' * self.width
        for row in range(self.height):
            printable += row_str + ('\n' if row < self.height - 1 else "")
        return printable
