#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''If key already exists in a_dictionary updates its value
    and if it doesn't exist adds a new key:value

    Args:
        a_dictionary: a dictionary
        key: key
        value: value

    Returns: the updated dictionary
    '''
    if not a_dictionary or not key:
        return
    a_dictionary[key] = value
    return (a_dictionary)
