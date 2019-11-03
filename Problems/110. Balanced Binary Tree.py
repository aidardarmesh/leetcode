from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root):
        if not root:
            return True, 0
        
        left_b, left_h = self.height(root.left)
        right_b, right_h = self.height(root.right)
        
        return left_b and right_b and abs(left_h-right_h) <= 1, max(left_h, right_h) + 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        root_balanced, root_height = self.height(root)
        
        return root_balanced