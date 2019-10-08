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
        queue.append(root)

        while queue:
            level, size = [], len(queue)

            for _ in range(size):
                node = queue.pop(0)
                level.append(node)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            current = level.pop(0)

            for node in level:
                current.next = node
                current = node
        
        return root