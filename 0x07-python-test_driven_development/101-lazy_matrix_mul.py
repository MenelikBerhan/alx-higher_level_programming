#!/usr/bin/python3
"""
Module to compute product of two matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies two matrices\n
    Args:
        m_a (`list` of `list` of `int`): first matrix
        m_b (`list` of `list` of `int`): second matrix\n
    Returns (`list` of `list` of `int`): the product
    """
    result = np.matmul(m_a, m_b)

    # return np.dot(m_a, m_b, out=np.array)

    return result.tolist()
