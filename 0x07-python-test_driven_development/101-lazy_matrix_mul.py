#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices using the module
NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices using the module NumPy.
    Args:
        m_a (list): the first matrix
        m_b (list): the second matrix
    Returns:
        list: the product of the 2 matrices
    """
    return np.matmul(m_a, m_b)
