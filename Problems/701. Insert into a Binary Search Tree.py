from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
            elif node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
        
        return root