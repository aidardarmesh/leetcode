from typing import *

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        stack = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        
        return True