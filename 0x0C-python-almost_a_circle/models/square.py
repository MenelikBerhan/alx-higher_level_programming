#!/usr/bin/python3
"""Module containing `Square` class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square object by extending the `Rectangle` class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a `Square` class instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """`str`: Returns a fanciery string representation of a square"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        """`int`: Getter and setter for attribute size (width and height)\n
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not greater than 0
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates instance attribute values. Arguments passed are assumed
        to be in `id`, `size`, `x`, `y` sequence for `*args`"""
        # if more than 4 arguments don't update any argument
        # if len(args) > 4:
        #     raise AttributeError("Square object has only 4 attributes")

        # err_msg = "Square object doesn't have an attribute named "
        attributes = ["id", "size", "x", "y"]

        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                exec("self." + attributes[i] + " = " + str(arg))
        else:
            # if any attribute is unknown don't update any argument
            # for attr in kwargs:
            #     if attr not in attributes:
            #         raise AttributeError(err_msg + "'{}'".format(attr))
            for attr, arg in kwargs.items():
                exec("self." + attr + " = " + str(arg))

    def to_dictionary(self):
        """`dict`: Returns a dictionay representation of the square"""
        sqr_dict = {}
        sqr_dict.update({'id': self.id, 'size': self.size})
        sqr_dict.update({'x': self.x, 'y': self.y})

        return sqr_dict
