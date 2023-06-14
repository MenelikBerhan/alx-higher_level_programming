#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''Prints a dictionay by ordered keys

    Args:
        a_dictionary: a dictionary
    '''
    if not a_dictionary:
        return
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
