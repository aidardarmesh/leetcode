from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest_unipath = 0
        
        def path(root, uni_val, path_len):
            if root is None:
                return 0
            
            if root.val == uni_val:
                self.longest_unipath = max(self.longest_unipath, path_len+1)
                path(root.left, uni_val, path_len+1)
                path(root.right, uni_val, path_len+1)
            else:
                path(root.left, root.val, 0)
                path(root.right, root.val, 0)
            
            return 
        
        path(root, float('inf'), 0)
        
        return self.longest_unipath
