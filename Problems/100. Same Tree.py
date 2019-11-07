from typing import *
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def serialize(root):
            queue = [root]
            res = []
            
            while any(queue):
                node = queue.pop(0)
                
                if node:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append(None)
            
            return res
        
        return serialize(p) == serialize(q)