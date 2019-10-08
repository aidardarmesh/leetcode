from typing import *

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        
        queue = [root]

        while queue:
            current = queue.pop()

            if current.left and current.right:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left
                
                queue.append(current.left)
                queue.append(current.right)
        
        return root