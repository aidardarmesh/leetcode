from typing import *

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # in_order traversal of BST gives all elem-s of BST in ASC order
        # Therefore, during traversal, if next elem is smaller than current
        # then tree is not BST

        stack = []
        node = root
        prev = float('-inf')

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()

                if prev > node.val:
                    return False
                else:
                    prev = node.val
                
                node = node.right
        
        return True