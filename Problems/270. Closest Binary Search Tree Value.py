from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return 9999999999999
        
        if root.val > target:
            closest = self.closestValue(root.left, target)
            
            if abs(closest-target) < abs(root.val-target):
                return closest
        elif root.val < target:
            closest = self.closestValue(root.right, target)
            
            if abs(closest-target) < abs(root.val-target):
                return closest
        
        return root.val