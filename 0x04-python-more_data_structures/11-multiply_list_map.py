#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    '''Creates a new list with all values of a list multiplied by number

    Args:
        my_list: a list used to create the new list
        number: integer to multiply values of my_list

    Returns: the newly created list
    '''
    if not my_list:
        return (None)
    return (list(map(lambda x: 2 * x, my_list)))
