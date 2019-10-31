from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        node = root

        while True:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            elif node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break

        return root