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

    @property
    def size(self):
        """int: gets and sets the attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square using `#`

        Example:
            Square(2).my_print()
                ##
                ##
        """
        if self.__size == 0:
            print()
            return
        row = 0
        while row < self.__size:
            print('#' * self.__size)
            row += 1
