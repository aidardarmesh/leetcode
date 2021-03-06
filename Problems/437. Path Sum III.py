from typing import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        self.paths = 0
        self.root_nodes = set()
        
        def path(root, path_sum, sum):
            if root:
                if root.val == path_sum:
                    self.paths += 1
                
                path(root.left, path_sum-root.val, sum)
                path(root.right, path_sum-root.val, sum)
                
                if not root.left in self.root_nodes:
                    path(root.left, sum, sum)
                    self.root_nodes.add(root.left)
                
                if not root.right in self.root_nodes:
                    path(root.right, sum, sum)
                    self.root_nodes.add(root.right)
        
        path(root, sum, sum)
        
        return self.paths
