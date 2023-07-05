#!/usr/bin/python3

class LockedClass():
    """Class that doesn't allow the user to set
    a new instance attribute except `first_name`"""

    def __setattr__(self, attribute, value):
        if attribute != "first_name":
            print("Cannot set %s" % attribute)
            raise Exception("Right!")
        else:
            self.__dict__[attribute] = value
