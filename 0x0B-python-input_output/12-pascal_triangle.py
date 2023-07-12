#!/usr/bin/python3
"""Module containing `pascal_triangle` function"""


def pascal_triangle(n):
    """Returns a `list` of `lists` of `int` representing
    the `Pascal's triangle` of `n`"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    pascal = [[1], [1, 1]]
    i = 0
    while i < n - 2:
        row = []
        last = pascal[len(pascal) - 1]
        j = 0
        while j <= i:
            row.append(last[j] + last[j + 1])
            j += 1

        row = [1] + row + [1]
        pascal.append(row)
        i += 1

    return pascal
