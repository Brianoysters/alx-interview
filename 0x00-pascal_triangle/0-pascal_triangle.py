#!/usr/bin/python3

def pascal_triangle(n):
    """The function returns a list of lists
    of integers representing the Pascal’s triangle of n
    values
    """
    if n <= 0:
        return []

    res = []
    for i in range(1, n + 1):
        level = []
        C = 1
        for j in range(1, i + 1):
            level.append(C)
            C = C * (i - j) // j
        res.append(level)
    
    return res

