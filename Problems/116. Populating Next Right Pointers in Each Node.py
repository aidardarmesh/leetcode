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
        
        queue = []

        if root.left:
            queue.append(root.left)
        
        if root.right:
            queue.append(root.right)

        while queue:
            current = queue.pop(0)
            size = len(queue)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            for _ in range(size):
                node = queue.pop(0)
                current.next = node
                current = node
                
                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)
        
        return root