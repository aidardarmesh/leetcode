from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        
        res, deq = [], deque()
        deq.append(root)

        while deq:
            size, level = len(deq), []

            for _ in range(size):
                node = deq.popleft()
                level.append(node.val)

                if node.left:
                    deq.append(node.left)
                
                if node.right:
                    deq.append(node.right)
            
            res.append(level)
        
        return res

s = Solution()

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

print(s.levelOrder(node3))