#!/usr/bin/python3
"""Define a matrix multiplication function"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of m_a and m_b

    Args:
        m_a (lists of int or float): matrix 1
        m_b (lists of int or float): matrix 2
    """

    return (np.matmul(m_a, m_b))
