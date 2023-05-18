#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [0b11100000, 0b10000000, 0b10000000]
print(validUTF8(data))
