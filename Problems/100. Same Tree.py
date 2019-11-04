from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # check if p and q are both None
        if not p and not q:
            return True
        
        # check if one of them None
        if not p or not q:
            return False
        
        # current line code means they're both ok
        # then check values
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)