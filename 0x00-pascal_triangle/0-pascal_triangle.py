#!/usr/bin/python3

def pascal_triangle(n):
    """The function returns a list of lists
    of integers representing the Pascal’s triangle of n
    values
    """
    if n <= 0:
        return []

    tri = []
    for i in range(1, n + 1):
        row = []
        init_1 = 1
        for j in range(1, i + 1):
            row.append(init_1)
            init_1 = init_1 * (i - j) // j
        tri.append(row)
    
    return tri

