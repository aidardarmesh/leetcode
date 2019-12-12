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
        def check(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return True
        
        queue = [(p, q)]

        while queue:
            p, q = queue.pop(0)

            if not check(p, q):
                return False
            
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            
        return True
