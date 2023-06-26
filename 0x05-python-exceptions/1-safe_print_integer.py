#!/usr/bin/python3
def safe_print_integer(value):
    '''Prints integer with "{:d}".format() method

    Args:
        value: an integer to print
    Returns: True if value is correctly printed or False otherwise
    '''
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
