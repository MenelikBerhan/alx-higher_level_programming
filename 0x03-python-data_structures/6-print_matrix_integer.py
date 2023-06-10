#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''Prints a matrix of integers with one row on a line

    Args:
        matrix: a matrix of integers
    '''
    for row in matrix:
        if len(row) == 0:
            print()
            continue
        for i in range(len(row)):
            print("{:d}".format(row[i]),
                  end=', ' if i != len(row) - 1 else '\n')
