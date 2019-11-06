from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        sum = 0
        
        while stack:
            node = stack.pop()

            if not node:
                continue

            if L <= node.val <= R:
                sum += node.val
            
            if L < node.val:
                stack.append(node.left)
            
            if node.val < R:
                stack.append(node.right)
        
        return sum
