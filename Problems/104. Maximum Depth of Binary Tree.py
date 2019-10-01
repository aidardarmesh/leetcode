from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root: TreeNode, depth: int) -> int:
        if not root.left and not root.right:
            self.depth = max(self.depth, depth)

        if root.left:
            self.maxDepth(root.left, depth + 1)

        if root.right:
            self.maxDepth(root.right, depth + 1)

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

s.maxDepth(node3, 1)
print(s.depth)