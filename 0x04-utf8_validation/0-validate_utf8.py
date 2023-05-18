#!/usr/bin/python3

"""
validUTF8 method
"""


def validUTF8(data):
    """
     a method that determines if a given data set
     represents a valid UTF-8 encoding
    """
    # Number of bytes for the current character
    number_bytes = 0

    for i in data:
        # Check if the current byte is a continuation byte
        if number_bytes == 0:
            if (i >> 7) == 0b0:
                continue
            elif (i >> 5) == 0b110:
                number_bytes = 1
            elif (i >> 4) == 0b1110:
                number_bytes = 2
            elif (i >> 3) == 0b11110:
                number_bytes = 3
            else:
                return False
        else:
            # Check if the current byte is a valid continuation byte
            if (i >> 6) != 0b10:
                return False

        number_bytes -= 1

    return number_bytes == 0
