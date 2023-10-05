#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    if not boxes or len(boxes) == 0:
        return False

    keys = set(boxes[0])  # Start with keys from the first box
    visited = [False] * len(boxes)
    visited[0] = True

    queue = [0]  # Use a queue for BFS traversal

    while queue:
        box_index = queue.pop(0)
        for key in boxes[box_index]:
            if key not in keys and 0 <= key < len(boxes):
                keys.add(key)
                queue.append(key)
                visited[key] = True

    return all(visited)
