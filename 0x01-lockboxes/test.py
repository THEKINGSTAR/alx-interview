#!/usr/bin/python3
"""Lockboxes"""

def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    for k in boxes:
            for sk in k:
                if sk not in boxes[1:][0:]:
                    return False
    return True