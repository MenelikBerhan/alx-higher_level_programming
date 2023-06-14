#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''Finds common elements in two sets

    Args:
        set_1: first set
        set_2: second set

    Returns: a set of common elements
    '''
    if not set_1 or not set_2:
        return (set())
    return (set.intersection(set_1, set_2))
