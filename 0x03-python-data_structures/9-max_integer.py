#!/usr/bin/python3
def max_integer(my_list=[]):
    '''Finds the biggest integer in a list

    Args:
        my_list: a list

    Returns: the biggest integer or None if list is empty.
    '''
    if len(my_list) == 0:
        return (None)
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return (max)
