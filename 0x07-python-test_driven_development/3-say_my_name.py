#!/usr/bin/python3
"""
'3-say_my_name' module.

This module contains `say_my_name` function that prints first
and last name given to it as an argument.
"""


def say_my_name(first_name, last_name=""):
    """Prints name in `first last` format

    Args:
        first_name (`string`): first name
        last_name (`string`, optional): last name

    Raises:
        TypeError: if either first_name or last_name is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
