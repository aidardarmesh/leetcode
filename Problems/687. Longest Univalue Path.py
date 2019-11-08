from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest = 0
        
        def uni_path(root):
            if root is None:
                # node_val, path_len
                return float('inf'), 0
            
            path = 0
            left_val, left_path = uni_path(root.left)
            right_val, right_path = uni_path(root.right)
            
            if root.val == left_val:
                path += left_path
                self.longest = max(self.longest, path)
            
            if root.val == right_val:
                path += right_path
                self.longest = max(self.longest, path)
            
            return root.val, max(left_path if root.val == left_val else 0, \
                                 right_path if root.val == right_val else 0) + 1
        
        uni_path(root)
        
        return self.longest
