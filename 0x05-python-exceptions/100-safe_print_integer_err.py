#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''Prints an integer

    Args:
        value: value to be printed as integer
    Returns: True if value is integer or False otherwise
    '''
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        print("Exception: {}".format(ex.args[0]), file=sys.stderr)
        return False
