from typing import *

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_valid(self, root):
        if not root:
            return True, 10**10, -10**10
        
        left_bst, left_min, left_max = self.is_valid(root.left)
        right_bst, right_min, right_max = self.is_valid(root.right)
        
        root_min = min(left_min, root.val)
        root_max = max(root.val, right_max)
        
        root_bst = left_max < root.val < right_min
        root_bst &= left_bst and right_bst
        
        return root_bst, root_min, root_max
        
    def isValidBST(self, root: TreeNode) -> bool:
        bst, _, _ = self.is_valid(root)
        
        return bst