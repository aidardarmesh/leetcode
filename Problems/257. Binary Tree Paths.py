from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]
        
        return list(map(lambda x: str(root.val) + "->" + x, self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)))

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