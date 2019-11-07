from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def rev_in_order_nodes(root):
            stack = []
            node = root
            res = []
            
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.right
                elif stack:
                    node = stack.pop()
                    res.append(node)
                    node = node.left
            
            return res
        
        nodes = rev_in_order_nodes(root)
        diff = 0
        
        for node in nodes:
            node.val += diff
            diff = node.val
        
        return root
