from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        
        def collect(root, sum, path, res):
            if not root:
                return
            
            if not root.left and not root.right and root.val == sum:
                path.append(root.val)
                res.append(path)
                return
            
            collect(root.left, sum-root.val, path+[root.val], res)
            collect(root.right, sum-root.val, path+[root.val], res)
        
        collect(root, sum, [], res)
        
        return res