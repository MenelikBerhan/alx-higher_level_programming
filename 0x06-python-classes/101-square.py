#!/usr/bin/python3
"""A `Square` class that defines a square."""


class Square():
    """A class that defines a square with size

    Attributes:
        size (`int`): a private attribute storing the length
            of a side of a suare
        position (`tuple` of two `int`s): (x, y) position of
            the square from origin. Both x and y must be >= 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square

        Args:
            size (`int`, optional): length of a side of a suare
            position (`tuple` of two `int`s): (x, y) position of the square

        Raises:
            TypeError: if size is not an integer or
                if postion is not a tuple of two non negative integers
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple or type(position[0]) != int\
                or len(position) != 2 or type(position[1]) != int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of the square\n
        Returns (`int`): area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """int: gets and sets the attribute size\n
        For setter;
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """`tuple`: Gets and sets the position attribute\n
        For Setter, Raises:
            TypeError: if value is not a tuple of two non negative integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or type(value[0]) != int or\
                type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square using `#`\n
        Example:
            Square(2).my_print()
                ##
                ##
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for row in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            print('#' * self.__size)

    def __str__(self):
        """`str`: Returns a string representation of a `Square`"""
        printable = ""
        if self.__size == 0:
            # printable += '\n'
            return printable
        for y in range(0, self.__position[1]):
            printable += '\n'
        for row in range(0, self.__size):
            for x in range(0, self.__position[0]):
                printable += " "
            printable += '#' * self.__size
            if row != self.__size - 1:
                printable += '\n'
        return printable
