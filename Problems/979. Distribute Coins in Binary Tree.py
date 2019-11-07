from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def coin(self, root):
        if not root:
            return 0
        
        val = root.val
        left = self.coin(root.left)
        self.moves += abs(left)
        val += left
        right = self.coin(root.right)
        self.moves += abs(right)
        val += right
        
        return val - self.avg
    
    def count(self, root):
        stack = [root]
        sum = 0
        cnt = 0

        while stack:
            node = stack.pop()
            sum += node.val
            cnt += 1

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return sum, cnt
    
    def distributeCoins(self, root: TreeNode) -> int:
        sum, cnt = self.count(root)
        self.avg = sum // cnt
        self.moves = 0
        self.coin(root)
        
        return self.moves