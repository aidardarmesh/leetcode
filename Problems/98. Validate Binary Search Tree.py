from typing import *

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, lower, upper):
            if root is None:
                return True
            
            if root.val <= lower:
                return False
            
            if root.val >= upper:
                return False
            
            left = helper(root.left, lower, root.val)
            right = helper(root.right, root.val, upper)

            return left and right
        
        return helper(root, float('-inf'), float('inf'))
