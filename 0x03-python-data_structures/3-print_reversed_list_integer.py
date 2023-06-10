#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints elements of a list in reverse order

    Args:
        my_list: a list
    '''
    a = (list(my_list))[:]
    a.sort(reverse=True)
    for i in a:
        print("{:d}".format(i), end='\n')
