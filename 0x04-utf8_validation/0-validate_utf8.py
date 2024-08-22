#!/usr/bin/python3
"""
Module for UTF-8 Validation.
"""

def validUTF8(data):
    """
    Validates if a dataset meets UTF-8 encoding requirements.

    Args:
        data.

    Returns:
        True else False
    """
    bytes_count = 0

    for num in data:

        _byte = num & 0xFF

        if bytes_count == 0:

            if _byte >> 5 == 0b110:
                bytes_count = 1
            elif _byte >> 4 == 0b1110:
                bytes_count = 2
            elif _byte >> 3 == 0b11110:
                bytes_count = 3
            elif _byte >> 7 != 0:
                return False
        else:

            if _byte >> 6 != 0b10:
                return False
            bytes_count -= 1

    return bytes_count == 0

