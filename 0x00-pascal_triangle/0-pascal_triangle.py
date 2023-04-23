#!/usr/bin/python3
""" ALX interview 1 - Pascal Triangle """


def pascal_triangle(n):
    """_summary_

    Args:
        n (int): number of rows in Pascal Triangle

    Returns:
        list: a list containing Pascal Triangle of int row n
    """

    if n <= 0:
        return []

    P_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(P_triangle[i-1][j-1] + P_triangle[i-1][j])
        row.append(1)
        P_triangle.append(row)
    return P_triangle
