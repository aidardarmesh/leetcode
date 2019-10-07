from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getLeaves(self, root: TreeNode) -> List[int]:
        leaves = []
        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                
                if not node.left and not node.right:
                    leaves.append(node.val)
                
                node = node.right
        
        return leaves

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)

s = Solution()

t1 = TreeNode(1)
t2 = TreeNode(2)

assert s.leafSimilar(t1, t2) == False