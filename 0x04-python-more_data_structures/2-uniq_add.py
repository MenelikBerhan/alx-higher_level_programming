#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''Finds the sum of all unique elements of a list

    Args:
        my_list: an integer list

    Returns: the sum of unique elements
    '''
    if not my_list:
        return (None)
    return (sum(set(my_list)))
