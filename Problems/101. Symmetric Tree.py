from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False
        
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

s = Solution()

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(2)
a.left.left = TreeNode(3)
a.left.right = TreeNode(4)
a.right.left = TreeNode(4)
a.right.right = TreeNode(3)

b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(2)
b.left.right = TreeNode(3)
b.right.right = TreeNode(3)

c = None

assert s.isSymmetric(a) == True
assert s.isSymmetric(b) == False
assert s.isSymmetric(c) == True