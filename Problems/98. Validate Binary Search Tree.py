from typing import *

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_valid(self, root, greater, less):
        if not root:
            return True
        
        for val in greater:
            if not val > root.val:
                return False
        
        for val in less:
            if not val < root.val:
                return False
        
        valid = True
        
        if root.left:
            valid &= self.is_valid(root.left, greater[:] + [root.val], less[:])
        
        if root.right:
            valid &= self.is_valid(root.right, greater[:], less[:] + [root.val])
        
        return valid
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid(root, [], [])