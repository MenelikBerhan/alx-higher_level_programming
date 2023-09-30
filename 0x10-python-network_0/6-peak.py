#!/usr/bin/python3
"""Contains a function that finds a peak"""


def find_peak(list_of_integers):
    """Finds the peak element which is not less than its neighbours"""
    if not list_of_integers:
        return None
    list_len = len(list_of_integers)
    if list_len == 1 or list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[list_len - 1] >= list_of_integers[list_len - 2]:
        return list_of_integers[list_len - 1]
    low, high = 0, list_len - 1
    while low <= high:
        mid = (low + high) // 2
        if list_of_integers[mid - 1] <= list_of_integers[mid] and\
                list_of_integers[mid + 1] <= list_of_integers[mid]:
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1
