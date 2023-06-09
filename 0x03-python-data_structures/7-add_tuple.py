#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''Adds the first and second elements of two tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns: a tuple of the sums
    '''
    a = tuple_a[:2]
    b = tuple_b[:2]
    while len(a) < 2:
        a += (0,)
    while len(b) < 2:
        b += (0,)
    return (a[0] + b[0], a[1] + b[1])
