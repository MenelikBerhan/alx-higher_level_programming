#!/usr/bin/python3
def element_at(my_list, idx):
    '''A function that retrives an element from my_list at index idx

    Args:
        my_list: a list
        idx: integer index

    Returns:
        An element of my_list at index idx, or
        None if idx is negative or is out of bounds
    '''
    if idx < 0 or idx >= len(my_list):
        return (None)
    return (my_list[idx])
