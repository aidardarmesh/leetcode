from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def level_order(self, root):
        queue = [root]
        res = []
        
        while any(queue):
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                
                if not node:
                    res.append(node)
                    continue
                
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        return res
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.level_order(p) == self.level_order(q)