#!/usr/bin/python3
"""Module containing `Student` class"""


class Student:
    """Defines a student by `first_name`, `last_name` and `age`"""
    def __init__(self, first_name, last_name, age):
        """Initializes a `Student` instance or object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """`dict`: Returns a dictionay representation of a `Student` instance.
        If `attrs` is a list of strings, only attribute names contained in
        this list will be retrieved. Otherwise, all attrs will be retrieved"""
        my_dict = {}
        if type(attrs) == list and all([type(x) == str for x in attrs]):
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
            return my_dict

        return self.__dict__
