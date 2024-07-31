#!/usr/bin/python3
"""
Lockboxes Python solution by <brianoysters@gmail.com>
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of lists): A list where each index represents a
        box and each element is a list
        of keys that can open other boxes.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Set to keep track of which boxes have been opened
    opened_boxes = set()
    
    # Stack to manage the DFS approach, starting with the first box
    stack = [0]
    
    while stack:
        # Get the current box index to be processed
        box_index = stack.pop()
        
        if box_index not in opened_boxes:
            # Mark the current box as opened
            opened_boxes.add(box_index)
            
            # Add all keys found in the current box to the stack
            for key in boxes[box_index]:
                if key not in opened_boxes:
                    stack.append(key)
    
    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

