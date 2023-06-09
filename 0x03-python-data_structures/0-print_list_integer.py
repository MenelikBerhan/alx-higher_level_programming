#!/usr/bin/python3
def print_list_integer(my_list=[]):
    '''My list printing function

    Args:
        my_list: a list to be printed
    '''
    for i in my_list:
        print("{:d}".format(i))
