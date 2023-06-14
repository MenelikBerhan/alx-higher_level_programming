#!/usr/bin/python3
def number_keys(a_dictionary):
    '''Finds the number of keys in a dictionay

    Args:
        a_dictionary: a dictionary

    Returns: the number of keys in a_dictionary
    '''
    if not a_dictionary:
        return (None)
    return (len(dict.keys(a_dictionary)))
