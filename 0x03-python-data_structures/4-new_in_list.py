#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''Replaces value in my_list at index idx with element
    without modifying the original list

    Args:
        my_list: a list
        idx: index of value to be replaced
        element: new value

    Returns: a new list with replaced value
    '''
    if idx < 0 or idx >= len(my_list):
        return (my_list[:])
    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
