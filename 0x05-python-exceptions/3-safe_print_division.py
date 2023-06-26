#!/usr/bin/python3
def safe_print_division(a, b):
    '''Prints the result of a divided by b

    Args:
        a: first integer
        b: second integer
    Returns: a/b or None if b equals 0
    '''
    try:
        ans = a/b
    except ZeroDivisionError:
        ans = None
    finally:
        print("Inside result: {}".format(ans))
    return ans
