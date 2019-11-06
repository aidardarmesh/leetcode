from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        if not root.left and not root.right:
            return root
        
        node = root
        prev_right = root.right
        
        if node.left:
            node.right = self.flatten(root.left)
            node.left = None
            
            while node.right:
                node = node.right
        
        node.right = self.flatten(prev_right)
        
        return root
