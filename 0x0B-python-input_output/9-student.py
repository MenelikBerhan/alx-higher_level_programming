#!/usr/bin/python3
"""Module containing `Student` class"""


class Student:
    """Defines a student by `first_name`, `last_name` and `age`"""
    def __init__(self, first_name, last_name, age):
        """Initializes a `Student` instance or object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """`dict`: Returns a dictionay representation of a
        `Student` instance"""
        return self.__dict__
