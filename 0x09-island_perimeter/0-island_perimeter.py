#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ returns the perimeter of the island described in a grid """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                """Add perimeter for each land cell"""
                perimeter += 4
                """ Check neighbors"""
                """up"""
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                    """down"""
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                    """left"""
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                    """right"""
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    return perimeter
