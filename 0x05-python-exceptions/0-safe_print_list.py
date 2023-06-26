#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x number of elements from a list

    Args:
        my_list: a list
        x: no.of elements to print
    Returns: actually printed number of elements
    '''
    if not my_list or x == 0:
        print("")
        return 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print("")
        return i + 1
    except IndexError as ex:
        print("")
        return i
