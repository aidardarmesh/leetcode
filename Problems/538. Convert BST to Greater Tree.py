from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        
        def convert(root):
            if root:
                convert(root.right)
                self.total += root.val
                root.val = self.total
                convert(root.left)
            
            return root
        
        convert(root)
        
        return root
