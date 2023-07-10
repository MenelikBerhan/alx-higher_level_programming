#!/usr/bin/python3
"""Module containing `is_same_class` fucntion"""


def is_same_class(obj, a_class):
    """`bool`: Returns `True` if the object is exactly an instance
    of the specified class; otherwise `False`"""
    return obj.__class__ == a_class
