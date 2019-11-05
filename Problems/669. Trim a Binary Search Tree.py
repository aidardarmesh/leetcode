from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        while root and not (L <= root.val <= R):
            if root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left
        
        if not root:
            return root
        
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        
        return root
