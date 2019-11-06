from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def height(root):
            if not root:
                return 0
            
            return 1 + max(height(root.left), height(root.right))
        
        d = height(root.left) + height(root.right)
        
        left_d = self.diameterOfBinaryTree(root.left)
        right_d = self.diameterOfBinaryTree(root.right)
        
        return max(d, left_d, right_d)
