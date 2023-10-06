#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    keys = [0]  # The first box is unlocked by default
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    return len(keys) == len(boxes)
