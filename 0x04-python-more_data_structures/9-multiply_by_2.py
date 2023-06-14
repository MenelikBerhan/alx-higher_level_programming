#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''Multiplies all values of a dictionary by 2

    Args:
        a_dictionary: a dictionary

    Returns: a new and updated dictionary
    '''
    if not a_dictionary:
        return (None)
    return ({x: a_dictionary[x] * 2 for x in a_dictionary})
