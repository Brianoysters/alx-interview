#!/usr/bin/python3
"""
0. Pascal's Triangle
This module contains a function that generates Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth level.

    Args:
        n (int): The number of levels in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    tri = []
    for i in range(1, n + 1):
        row = []
        C = 1
        for j in range(1, i + 1):
            row.append(C)
            C = C * (i - j) // j
        tri.append(row)

    return tri

