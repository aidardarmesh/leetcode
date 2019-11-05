from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [root]
        cnt = 0
        
        while stack:
            node = stack.pop()
            cnt += 1
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return cnt
