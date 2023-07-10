#!/usr/bin/python3
"""Module containing `is_kind_of_class` fucntion"""


def is_kind_of_class(obj, a_class):
    """`bool`: Returns `True` if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified
    class; otherwise `False`"""
    return isinstance(obj, a_class)
