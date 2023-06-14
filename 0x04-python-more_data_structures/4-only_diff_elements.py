#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''Finds elements present in only one of the two sets

    Args:
        set_1: first set
        set_2: second set

    Returns: a symmetric difference of the two sets
    '''
    if not set_1:
        set_1 = set()
    if not set_2:
        set_2 = set()
    return (set.symmetric_difference(set_1, set_2))
