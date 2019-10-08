from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.paths(root, "")

        return self.res
    
    def paths(self, root: TreeNode, current: str):
        if not root:
            return

        if not root.left and not root.right:
            self.res.append(current + str(root.val))

        if root.left:
            self.paths(root.left, current + str(root.val) + "->")

        if root.right:
            self.paths(root.right, current + str(root.val) + "->")

s = Solution()

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(5)

b = TreeNode(3)

c = None

assert s.binaryTreePaths(a) == ["1->2->5", "1->3"]
assert s.binaryTreePaths(b) == ["3"]
assert s.binaryTreePaths(c) == []