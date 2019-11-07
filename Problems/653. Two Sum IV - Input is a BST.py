from typing import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        if not root:
            return False

        stack = []
        node = root
        visited = set()
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()

                if k-node.val in visited:
                    return True
                
                visited.add(node.val)
                node = node.right
        
        return False
