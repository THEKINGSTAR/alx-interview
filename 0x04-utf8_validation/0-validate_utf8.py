#!/usr/bin/python3
"""
method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding,
    else
    return False
    """
    num_bytes_to_follow = 0

    for num in data:
        if num_bytes_to_follow == 0:
            mask = 1 << 7
            while mask & num:
                num_bytes_to_follow += 1
                mask >>= 1

            if num_bytes_to_follow == 0:
                continue
            if num_bytes_to_follow == 1 or num_bytes_to_follow > 4:
                return False
        else:
            if not (num & (1 << 7) and not (num & (1 << 6))):
                return False

        num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
