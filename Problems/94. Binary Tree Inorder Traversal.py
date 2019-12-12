from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                res.append(node.val)
                node = node.right

        return res

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3

s = Solution()
print(s.inorderTraversal(node1))