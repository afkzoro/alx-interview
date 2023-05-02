#!/usr/bin/python3
""" ALX interview 3 - 2Keys Keyboard """


def minOperations(n):
    """

    Args:
        n (int): number of H characters

    Returns:
        int: Total count
    """
    count = 0
    factor = 2
    while n > 1:
        if n % factor == 0:
            count += factor
            n //= factor
        else:
            factor += 1
    return count
