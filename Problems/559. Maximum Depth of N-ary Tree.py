from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queue = [root]
        height = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                
                for child in node.children:
                    queue.append(child)
            
            height += 1
        
        return height
