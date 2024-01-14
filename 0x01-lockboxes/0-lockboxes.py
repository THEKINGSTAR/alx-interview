#!/usr/bin/python3
"""Lockboxes"""

def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    for k in boxes[0][1:]:
        if k not in boxes[1:]:
            return False  
    return True
    