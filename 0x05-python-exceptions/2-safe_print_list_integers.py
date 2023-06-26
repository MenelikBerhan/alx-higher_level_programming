#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''Prints x elements of a list if element is an integer

    Args:
        my_list: a list
        x: no. of elements to access in my_list list
    Returns: the actually printed number of integer elements
    '''
    if not my_list or x == 0:
        print("")
        return 0
    i, j = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="\n" if i == x - 1 else "")
            i += 1
        except (ValueError, TypeError):
            if i == x - 1:
                print("")
            j += 1
            i += 1
    return i - j
