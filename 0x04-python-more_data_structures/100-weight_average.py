#!/usr/bin/python3
def weight_average(my_list=[]):
    '''Calculates a weighted average of tuples (<score>, <weight>) in
    a list

    Args:
        my_list: a list of tuples of format (<score>, <weight>)

    Returns: the weighted average
    '''
    if not my_list or len(my_list) == 0:
        return (0)
    sum = 0
    weight = 0
    for t in my_list:
        sum += t[0] * t[1]
        weight += t[1]
    return (sum/weight)
