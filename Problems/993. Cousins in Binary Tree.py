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
        queue = [root]
        
        while queue:
            size = len(queue)
            level = set()
            
            for _ in range(size):
                node = queue.pop(0)
                level.add(node.val)
                
                if node.left:
                    queue.append(node.left)
                    parent[node.left.val] = node.val
                
                if node.right:
                    queue.append(node.right)
                    parent[node.right.val] = node.val
            
            if x in level and y in level:
                if x in parent and y in parent and parent[x] != parent[y]:
                    return True
        
        return False
