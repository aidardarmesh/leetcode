from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        while root and not (L <= root.val <= R):
            if root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left
        
        sum = 0
        
        if not root:
            return sum
        
        sum += root.val
        sum += self.rangeSumBST(root.left, L, R)
        sum += self.rangeSumBST(root.right, L, R)
        
        return sum
