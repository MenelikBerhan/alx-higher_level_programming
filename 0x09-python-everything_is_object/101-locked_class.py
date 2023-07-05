#!/usr/bin/python3

class LockedClass():
    """Class that doesn't allow the user to set
    a new instance attribute except `first_name`"""

    def __setattr__(self, attribute, value):
        if attribute != "first_name":
            raise AttributeError("Can't set {} attribute".format(attribute))
        else:
            self.__dict__[attribute] = value
