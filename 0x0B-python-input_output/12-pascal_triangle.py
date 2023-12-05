#!/usr/bin/python3
"""Module for Pascal's triangle"""


def pascal_triangle(n):
    """
    Give a representation of a Pascal's triange of n

    Args:
        n: an int, representing the rows of Pascal's triangle

    Return: list of lists of integers representing a Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(0, n):
        row = [1] * (i + 1)

        if len(row) > 2:
            for j in range(0, len(row)):
                if j == len(row) - 1:
                    continue
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
