#!/usr/bin/python3
"""
Module to compute product of two matrices

"""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices\n
    Args:
        m_a (`list` of `list` of `int`): first matrix
        m_b (`list` of `list` of `int`): second matrix\n
    Returns (`list` of `list` of `int`): the product
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) != list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or all([len(row) == 0 for row in m_a]):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all([len(row) == 0 for row in m_b]):
        raise ValueError("m_b can't be empty")

    m_a_width = len(m_a[0])
    m_a_unequal_size = 0
    for row in m_a:
        if not all([(type(x) == int or type(x) == float) for x in row]):
            raise TypeError("m_a should contain only integers or floats")
        if not m_a_unequal_size and len(row) != m_a_width:
            m_a_unequal_size = 1

    m_b_width = len(m_b[0])
    m_b_unequal_size = 0
    for row in m_b:
        if not all([(type(x) == int or type(x) == float) for x in row]):
            raise TypeError("m_b should contain only integers or floats")
        if not m_b_unequal_size and len(row) != m_b_width:
            m_b_unequal_size = 1

    if m_a_unequal_size:
        raise TypeError("each row of m_a must be of the same size")
    if m_b_unequal_size:
        raise TypeError("each row of m_b must be of the same size")

    if m_a_width != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    product = []
    for row in m_a:
        row_product = []
        for i in range(m_b_width):
            val_i = 0
            b_col = [m_b[x][i] for x in range(m_a_width)]
            val_i = sum([row[k] * b_col[k] for k in range(m_a_width)])
            row_product.append(val_i)
        product.append(row_product)

    return product
