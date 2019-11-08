from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        res = []
        
        while queue:
            size = len(queue)
            level_sum = 0
            level_cnt = 0
            
            for _ in range(size):
                node = queue.pop(0)
                level_sum += node.val
                level_cnt += 1
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            res.append(level_sum / level_cnt)
        
        return res
