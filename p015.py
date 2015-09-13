"""Problem 015
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import factorial


def comb(n):
    """Central Binominal Coefficient Solution"""
    return factorial(2 * n) // factorial(n) ** 2


def lattice(grid):
    """Recursive Solution"""
    if grid == [0, 0]:
        return 1
    paths = 0
    if grid[0] > 0:
        paths += lattice([grid[0] - 1, grid[1]])
    if grid[1] > 0:
        paths += lattice([grid[0], grid[1] - 1])
    return paths


def route(cube):
    """Dynamic Solution"""
    L = [1] * cube
    for i in range(cube):
        for j in range(i):
            L[j] = L[j] + L[j - 1]
        L[i] = 2 * L[i - 1]
    return L[cube - 1]

ans = route(20)

print(ans)
