#!/usr/bin/python3
def no_c(my_string):
    '''Removes all 'c' and 'C' characters from string my_string

    Args:
        my_string: a string

    Returns: a new string with all 'c' & 'C' removed
    '''
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return (new_string)
