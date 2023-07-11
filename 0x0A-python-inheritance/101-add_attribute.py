#!/usr/bin/python3
"""Module containing `add_attribute` fucntion"""


def add_attribute(obj, attr_name, value):
    """Adds a new attribute named `attr_name` with value `value`
    to object `obj`.
    Raises:
        TypeError:  if the object can't have new attribute
    """
    if ('__dict__' in dir(obj)):
        # super(obj.__class__, obj).__setattr__(attr_name, value)
        obj.__dict__[attr_name] = value
    else:
        raise TypeError("can't add new attribute")
