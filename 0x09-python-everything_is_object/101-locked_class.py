#!/usr/bin/python3
"""
Module containing LockedClass
"""


class LockedClass():
    """Class that doesn't allow the user to set
    a new instance attribute except `first_name`"""

    __slots__ = ['first_name']
