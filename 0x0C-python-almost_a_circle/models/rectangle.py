#!/usr/bin/python3
"""Module containing `Rectangle` class"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle by extending `Base` class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a `Rectangle` object\n
        Raises:
            TypeError: if width, height, x or y is not an integer
            ValueError: if width or height is not greater than 0, or
                if x or y is less than 0.
        """
        super().__init__(id)
        # check if "__width" here will allow square to access __width
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """`int`: Getter and Setter for `width` attribute\n
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not greater than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """`int`: Getter and Setter for `height` attribute\n
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not greater than 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """`int`: Getter and Setter for `x` attribute\n
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """`int`: Getter and Setter for `y` attribute\n
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """`int`: Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle in `stdout` using `#`"""
        rec = "\n" * self.__y
        rec += ((' ' * self.__x) + ('#' * self.__width) + '\n') * self.__height
        print(rec, end="")

    def __str__(self):
        """`str`: Returns a fanciery string representation of a rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates instance attribute values. Arguments passed are assumed
        to be in `id`, `width`, `height`, `x`, `y` sequence for `*args`"""
        # if more than 5 arguments don't update any argument
        if len(args) > 5:
            raise AttributeError("Rectangle object has only 5 attributes")

        err_msg = "Rectangle object doesn't have an attribute named "
        attributes = ["id", "width", "height", "x", "y"]

        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                exec("self." + attributes[i] + " = " + str(arg))
        else:
            # if any attribute is unknown don't update any argument
            for attr in kwargs:
                if attr not in attributes:
                    raise AttributeError(err_msg + "'{}'".format(attr))
            for attr, arg in kwargs.items():
                exec("self." + attr + " = " + str(arg))

    def to_dictionary(self):
        """`dict`: Returns a dictionay representation of the rectangle"""
        rec_dict = {}
        rec_dict.update({'id': self.id, 'width': self.width})
        rec_dict.update({'height': self.height, 'x': self.x, 'y': self.y})

        return rec_dict
