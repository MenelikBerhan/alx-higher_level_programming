#!/usr/bin/python3
"""A `Square` class that defines a square."""


class Square():
    """A class that defines a square with size

    Attributes:
        size (int): a private attribute storing the length
            of a side of a suare
    """
    def __init__(self, size):
        """Initializes a square

        Args:
            size (int): length of a side of a suare
        """
        self.__size = size
