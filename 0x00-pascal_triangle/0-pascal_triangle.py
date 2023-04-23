#!/usr/bin/python3
""" ALX interview 1 - Pascal Triangle """


def pascal_triangle(n):
    """_summary_

    Args:
        n (int): integer to convert to Pascal Triangle

    Returns:
        list: a list containing Pascal Triangle of int n
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
    return [''.join(str(num) for num in row) for row in P_triangle]
