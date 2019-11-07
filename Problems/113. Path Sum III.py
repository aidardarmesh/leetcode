from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        
        def helper(root, sum, path):
            if not root.left and not root.right and sum == root.val:
                self.res.append(path+[root.val])
            
            if root.left:
                helper(root.left, sum-root.val, path+[root.val])
            
            if root.right:
                helper(root.right, sum-root.val, path+[root.val])
        
        if not root:
            return self.res
        
        helper(root, sum, [])
        
        return self.res