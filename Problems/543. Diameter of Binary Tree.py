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

            left_h, left_d = helper(root.left)
            right_h, right_d = helper(root.right)
            d = left_h + right_h

            return 1 + max(left_h, right_h), max(d, left_d, right_d)
        
        h, d = helper(root)
        
        return d
