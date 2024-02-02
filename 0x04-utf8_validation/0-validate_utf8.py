#!/usr/bin/python3

import sys


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
    try:
        encoding = 'utf-8'
        data_in = str("".join(map(chr, data)))
        print(data_in)

    except Exception:
        return False

    return True
