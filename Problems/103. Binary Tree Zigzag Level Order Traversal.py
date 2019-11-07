from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # even - put values in level left-right, 
        # odd - put values in level right-left
        def even(num):
            return num % 2 == 0
        
        if not root:
            return []
        
        level_cnt = 0
        queue = [root]
        res = []
        
        while queue:
            size = len(queue)
            level = []
            
            for _ in range(size):
                node = queue.pop(0)
                
                if even(level_cnt):
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            level_cnt += 1
            res.append(level)
        
        return res
