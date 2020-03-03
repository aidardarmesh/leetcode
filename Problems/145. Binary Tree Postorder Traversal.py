from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res, stack, visited, node = [], [], set(), root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()

                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    res.append(node.val)
                    visited.add(node)
                    node = None
        
        return res

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3

s = Solution()
print(s.postorderTraversal(node1))