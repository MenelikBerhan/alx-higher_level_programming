#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Computes the square of all integers in a matrix and
    create a new matrix with the result

    Args:
        matix: an integer matrix

    Returns: a new matrix with squared values
    '''
    if not matrix:
        return (matrix)
    return ([[x**2 for x in row] for row in matrix])
