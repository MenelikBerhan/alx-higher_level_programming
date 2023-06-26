#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x number of elements from a list

    Args:
        my_list: a list
        x: no.of elements to print
    Returns: actually printed number of elements
    '''
    try:
        if not my_list:
            return 0
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print("")
        return i + 1
    except IndexError as ex:
        print("")
        return i
