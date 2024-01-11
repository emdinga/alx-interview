#!/usr/bin/python3
""" check if boxes can be opened and return T/F"""


def canUnlockAll(boxes):
    """ search to unlock """
    if not boxes or not boxes[0]:
        return false

    number_boxes = len(boxes)
    visited = set()
    visited.add(0)
    keys_queue =boxes[0]

    while keys_queue:
        current_key = keys_queue.pop(0)

        if current_key < num_boxes and current_key not in visited:
            visited.add(current_key)
            keys_queue.extend(boxes[current_key])

    return len(visited) == number_boxes
