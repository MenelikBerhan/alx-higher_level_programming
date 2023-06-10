#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints elements of a list in reverse order

    Args:
        my_list: a list
    '''
    if not my_list:
        return
    for i in sorted(my_list, reverse=True):
        print("{:d}".format(i))
