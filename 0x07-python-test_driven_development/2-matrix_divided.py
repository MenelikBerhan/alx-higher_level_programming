#!/usr/bin/python3
"""
'2-matrix_divided' module.

This module contains `matrix_divide` function which divides
each element of a matrix by a float or an integer number.
"""


def matrix_divided(matrix, div):
    """Divides each element of `matrix` by `div`. Each row of `matrix`
    must be of equal size and `div` must be a non-zero `int` or `float`.

    Args:
        matrix (`list` of `lists` of `int` or `float`): the matrix
        div (`int` or `float`): the divisor number

    Returns (`list` of `lists` of `int` or `float`): a new matrix

    Raises:
        TypeError: if `matrix` is not a list of lists of integers or floats,
            if each row of the `matrix` are not of the same size or
            if `div` is not either an `int` or `float.
        ZeroDivisionError: if `div` is equal to zero.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    if len(matrix) == 0:  # ??for empty list or list of empty lists
        # return []
        raise TypeError(error_msg)
    row_size = len(matrix[0])
    unequal_size = 0
    not_number = 0
    for row in matrix:
        if type(row) != list or\
                not all([(type(x) == int or type(x) == float) for x in row]):
            raise TypeError(error_msg)
        if not unequal_size and len(row) != row_size:
            unequal_size = 1

    if row_size == 0:  # ??for empty list of lists
        # return matrix[:]
        raise TypeError(error_msg)
    if unequal_size:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x/div, 2) for x in row] for row in matrix]
