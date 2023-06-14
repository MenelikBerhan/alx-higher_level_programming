#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''Deletes key from a dictionary

    Args:
        a_dictionary: a dictionary
        key: key

    Returns: the updated dictionary
    '''
    if a_dictionary and key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
