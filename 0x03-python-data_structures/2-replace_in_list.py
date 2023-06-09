#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''A function that replaces an element at idx in my_list
    with a new value of element.

    Args:
        my_list: a list
        idx: index of element to be replaced
        element: new value at idx

    Returns:
        The modified list.
    '''
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)
