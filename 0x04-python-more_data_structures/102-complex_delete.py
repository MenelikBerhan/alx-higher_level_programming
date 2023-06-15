#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''Deletes all keys with value from a_dictionary

    Args:
        a_dictionary: a dictionary
        value: value of keys to remove from dictionary

    Returns: the modified dictionary
    '''
    if not a_dictionary:
        return (a_dictionary)
    dict_copy = dict.copy(a_dictionary)
    for k, v in dict.items(dict_copy):
        if v == value:
            del a_dictionary[k]

    return (a_dictionary)
