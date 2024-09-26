#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a 2D grid
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by 1s in a grid.
    
    Args:
        grid
    
    Returns:
        integer
    """

    perim_ = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perim_ += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perim_ -= 1

                if i < rows - 1 and grid[i + 1][j] == 1:
                    perim_ -= 1

                if j > 0 and grid[i][j - 1] == 1:
                    perim_ -= 1

                if j < cols - 1 and grid[i][j + 1] == 1:
                    perim_ -= 1

    return perim_

