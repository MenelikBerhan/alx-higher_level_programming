#!/usr/bin/python3
def best_score(a_dictionary):
    '''Finds a key in a dictionary with the biggest integer value

    Args:
        a_dictionary: a dictionary

    Returns: the key with the highest value or None if no dictionary
    '''
    if not a_dictionary:
        return (None)
    val_list = list(dict.values(a_dictionary))
    i = val_list.index(max(val_list))
    return (list(dict.keys(a_dictionary))[i])
