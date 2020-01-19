from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [(root, 0)]
        ans = 0
        
        while queue:
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            size = len(queue)
            
            for _ in range(size):
                node, pos = queue.pop(0)
                
                if node.left:
                    queue.append((node.left, 2*pos+1))
                
                if node.right:
                    queue.append((node.right, 2*pos+2))
            
        return ans
