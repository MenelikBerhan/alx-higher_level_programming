#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''Removes an element at specific index in a list

    Args:
        my_list: a list
        idx: index of element to remove

    Returns: the modified list
    '''
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    del my_list[idx]
    return (my_list)
