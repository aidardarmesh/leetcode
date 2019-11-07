from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        
        def dfs(root):
            if not root:
                return 0
            
            L = dfs(root.left)
            R = dfs(root.right)
            self.moves += abs(L) + abs(R)
            
            return root.val + L + R - 1
        
        dfs(root)
        
        return self.moves