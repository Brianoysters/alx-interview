#!/usr/bin/python3
"""
Function to rotate a 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix by 90 degrees clockwise in place.

    Args:
        2D matrix of integers to be rotated.

    Returns:
        Matrix
    """

    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

