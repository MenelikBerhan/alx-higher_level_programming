#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''Prints x elements of a list if element is an integer

    Args:
        my_list: a list
        x: no. of elements to access in my_list list
    Returns: the actually printed number of integer elements
    '''
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="\n" if i == x - 1 else "")
        return i + 1
    except (ValueError, TypeError) as ex:
        if (i < x - 1):
            return (i + safe_print_list_integers(my_list[i + 1:], x - i - 1))
        else:
            print("")
            return i
