from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            diam = path = root.val
            left_diam = right_diam = float('-inf')
            
            if root.left:
                left_path, left_diam = helper(root.left)
                diam = max(diam, left_path + root.val)
                path = max(path, left_path + root.val)
            
            if root.right:
                right_path, right_diam = helper(root.right)
                diam = max(diam, diam + right_path)
                path = max(path, right_path + root.val)
            
            return path, max(diam, left_diam, right_diam)
        
        max_path, max_diam = helper(root)
        
        return max_diam
