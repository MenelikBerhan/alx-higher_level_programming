#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints elements of a list in reverse order

    Args:
        my_list: a list
    '''
    if len(my_list) == 0:
        print()
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
