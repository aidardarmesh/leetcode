from typing import *

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        s = None
        node = root
        
        while node:
            if node.val > p.val:
                s = node
                node = node.left
            else:
                node = node.right
        
        return s