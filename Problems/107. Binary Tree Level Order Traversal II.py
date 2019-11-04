from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []

        if not root:
            return res

        while queue:
            res.insert(0, [node.val for node in queue])
            new_queue = []

            for node in queue:
                for child in (node.left, node.right):
                    if child:
                        new_queue.append(child)
            
            queue = new_queue
        
        return res