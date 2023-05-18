#!/usr/bin/python3

"""
validUTF8 method
"""


def validUTF8(data):
    """ a method that determines if a given data set
     represents a valid UTF-8 encoding
     """
    num_continuation_bytes = 0

    for byte in data:
        if (byte >> 6) == 0b10:
            if num_continuation_bytes == 0:
                return False
            num_continuation_bytes -= 1
        else:
            if num_continuation_bytes > 0:
                return False
            if (byte >> 7) == 0b0:
                num_continuation_bytes = 0
            elif (byte >> 5) == 0b110:
                num_continuation_bytes = 1
                if byte >> 4 == 0b1100:
                    return False
            elif (byte >> 4) == 0b1110:
                num_continuation_bytes = 2
                if byte >> 3 == 0b11100:
                    return False
            elif (byte >> 3) == 0b11110:
                num_continuation_bytes = 3
                if byte >> 2 == 0b111100:
                    return False
            else:
                return False

    if num_continuation_bytes > 0:
        return False

    return True
