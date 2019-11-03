from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root, h):
        if not root:
            return h-1
        
        left_h = self.height(root.left, h+1)
        right_h = self.height(root.right, h+1)
        
        self.balanced &= abs(left_h-right_h) <= 1

        return max(left_h, right_h)
    
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True

        if not root:
            return self.balanced
        
        root_h = self.height(root, 0)

        return self.balanced