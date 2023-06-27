#!/usr/bin/python3
"""A `Square` class that defines a square."""


class Square():
    """A class that defines a square with size

    Attributes:
        size (int): a private attribute storing the length
            of a side of a suare
    """

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (:obj: `int`, optional): length of a side of a suare

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size
