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
        
        queue = [root]
        cnt = 0
        
        while queue:
            node = queue.pop(0)
            cnt += 1
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return cnt
