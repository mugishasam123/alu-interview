#!/usr/bin/python3
"""
0-rain module.
This module contains the function `rain`
that calculates how many square units of water
will be retained after it rains.
"""


def rain(walls):
    """
    Calculate the amount of water retained between walls.

    Args:
        walls (list): List of non-negative integers representing the heights of walls.

    Returns:
        int: Total amount of water retained after it rains.
    """
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate water trapped
    for i in range(n):
        water_trapped += max(0, min(left_max[i], right_max[i]) - walls[i])

    return water_trapped
