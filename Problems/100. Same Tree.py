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
            # check for existence of both
            if not p and not q:
                return True
            
            # check if one of them is None
            if p == None or q == None:
                return False
            
            # check values, because both exist
            if p.val != q.val:
                return False
            
            # current place means they both exist and values are equal
            return True
        
        deq = deque()
        deq.append((p,q))

        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p and q:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True