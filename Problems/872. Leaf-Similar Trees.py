from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def appendLeaves(self, root: TreeNode, leaves: List[int]) -> List[int]:
        if not root.left and not root.right:
            leaves.append(root.val)

        if root.left:
            self.appendLeaves(root.left, leaves)
        
        if root.right:
            self.appendLeaves(root.right, leaves)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1, l2 = [], []
        self.appendLeaves(root1, l1)
        self.appendLeaves(root2, l2)

        return l1 == l2

s = Solution()

t1 = TreeNode(1)
t2 = TreeNode(2)

assert s.leafSimilar(t1, t2) == False