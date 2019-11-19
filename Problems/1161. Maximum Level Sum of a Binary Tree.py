from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        level = 0
        max_ = (level, 0)
        
        while queue:
            size = len(queue)
            sum_ = 0
            
            for _ in range(size):
                node = queue.pop(0)
                sum_ += node.val
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            level += 1
                
            if sum_ > max_[1]:
                max_ = (level, sum_)
        
        return max_[0]
