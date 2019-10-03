from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        
        if root:
            stack.append(root)

        while stack:
            node = stack.pop()

            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
         
        return result

s = Solution()

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3

s = Solution()
print(s.preorderTraversal(node1))