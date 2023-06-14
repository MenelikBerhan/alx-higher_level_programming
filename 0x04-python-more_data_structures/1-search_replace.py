#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''Replaces all occurance of search in my_list with replace

    Args:
        my_list: an integer list
        search: values to be replaced
        replace: new value to set

    Returns: a new list with modified values
    '''
    if not my_list:
        return (my_list)

    return ([x if x != search else replace for x in my_list])
