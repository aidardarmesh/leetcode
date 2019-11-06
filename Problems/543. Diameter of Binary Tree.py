from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0, 0

            left_depth, left_diam = helper(root.left)
            right_depth, right_diam = helper(root.right)
            diam = left_diam + right_diam

            return 1 + max(left_depth, right_depth), max(diam, left_diam, right_diam)
        
        depth, diam = helper(root)
        
        return diam
