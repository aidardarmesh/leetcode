from typing import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.paths = 0
        self.root_nodes = set()
        
        def path(root, node_sum, sum):
            if not root:
                return
            
            if root.val == node_sum:
                self.paths += 1
                # path(root.left, sum, sum)
                # path(root.right, sum, sum)
            
            path(root.left, node_sum-root.val, sum)
            path(root.right, node_sum-root.val, sum)
            
            if not root.left in self.root_nodes:
                path(root.left, sum, sum)
                self.root_nodes.add(root.left)
            
            if not root.right in self.root_nodes:
                path(root.right, sum, sum)
                self.root_nodes.add(root.right)
        
        path(root, sum, sum)
        
        return self.paths
