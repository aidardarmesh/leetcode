from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        def level_order(root):
            deq = deque()
            deq.append(root)
            res = []

            if not root:
                return res

            while deq:
                size = len(deq)
                level = []

                for _ in range(size):
                    node = deq.popleft()
                    level.append(node.val)

                    if node.left:
                        deq.append(node.left)
                    
                    if node.right:
                        deq.append(node.right)
                    
                res.append(level)
            
            return res
        
        return reversed(level_order(root))