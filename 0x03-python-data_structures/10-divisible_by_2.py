#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''Checks if integer elements of a list are divisible by 2

    Args:
        my_list: a list

    Returns: a list with boolean values for divisibility by 2.
    '''
    return ([x % 2 == 0 for x in my_list])
