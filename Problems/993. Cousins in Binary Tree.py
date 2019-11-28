from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        
        parent = {}
        depth = {}
        i = 0
        queue = [root]
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                depth[node.val] = i
                
                if node.left:
                    queue.append(node.left)
                    parent[node.left.val] = node.val
                
                if node.right:
                    queue.append(node.right)
                    parent[node.right.val] = node.val
            
            i += 1
        
        return depth[x] == depth[y] and parent[x] != parent[y]
