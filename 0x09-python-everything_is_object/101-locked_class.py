#!/usr/bin/python3
"""
Module containing LockedClass
"""


class LockedClass():
    """Class that doesn't allow the user to set
    a new instance attribute except `first_name`"""

    def __setattr__(self, attribute, value):
        """sets attribute only for `first_name`"""
        if attribute != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(attribute))
        else:
            self.__dict__[attribute] = value
