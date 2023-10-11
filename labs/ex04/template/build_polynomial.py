# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree.

    Args:
        x: numpy array of shape (N,), N is the number of samples.
        degree: integer.

    Returns:
        poly: numpy array of shape (N,d+1)
    """
    N, D = x.shape[0], degree + 1
    exponents = np.arange(D)
    phi = np.zeros((N, D))
    for i in range(N):
        base = np.repeat(x[i], D)
        phi[i] = np.power(base, exponents)
    
    return phi
