#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates the matrix 90 degrees clockwise.
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # initial number
            tmp = matrix[i][j]
            # top for left
            matrix[i][j] = matrix[x][i]
            # left for bottom
            matrix[x][i] = matrix[y][x]
            # bottom for right
            matrix[y][x] = matrix[j][y]
            # right for top
            matrix[j][y] = tmp
