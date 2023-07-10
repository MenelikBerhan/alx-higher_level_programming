#!/usr/bin/python3
"""Module containing `inherits_from` fucntion"""


def inherits_from(obj, a_class):
    """`bool`: Returns `True` if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise `False`"""
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
