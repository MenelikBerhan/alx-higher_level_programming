#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''Executes a function safely

    Args:
        fct: a pointer to a function to be executed
        *args: list of arguments for function pointed by fct
    Returns: The return from fct if no exception is raised or None
    '''
    try:
        return fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex.args[0]), file=sys.stderr)
        return None
