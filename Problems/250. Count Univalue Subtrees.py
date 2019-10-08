from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.is_uni(root)

        return self.count
    
    def is_uni(self, root: TreeNode):
        if not root:
            return False

        if not root.left and not root.right:
            self.count += 1
        
            return True
        
        is_uni = True

        if root.left:
            is_uni = self.is_uni(root.left) and root.left.val == root.val
        
        if root.right:
            is_uni = self.is_uni(root.right) and root.right.val == root.val and is_uni
        
        self.count += is_uni

        return is_uni

s = Solution()

a = TreeNode(5)
a.right = TreeNode(5)
a.right.right = TreeNode(5)
a.left = TreeNode(1)
a.left.left = TreeNode(5)
a.left.right = TreeNode(5)

assert s.countUnivalSubtrees(a) == 4