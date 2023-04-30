#!/usr/bin/python3
""" ALX interview 2 - Lockboxes """


def canUnlockAll(boxes):
    """ Unlocks lockboxes

    Args:
        boxes (list): List of list of containing keys
    """
    n = len(boxes)
    open_boxes = [False] * n
    open_boxes[0] = True
    keys = boxes[0]

    # Iterate through all boxes
    for i in range(n):

        # Check if current box i can be unlocked
        if not open_boxes[i]:
            continue

        # check for keys in current box
        for key in boxes[i]:
            if key < n and not open_boxes[key]:
                open_boxes[key] = True
                keys += boxes[key]

        # Check if all boxes are unlocked
        if all(open_boxes):
            return True

    return all(open_boxes)
