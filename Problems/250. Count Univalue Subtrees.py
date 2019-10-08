from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        count = 0
        left_count = self.countUnivalSubtrees(root.left)
        right_count = self.countUnivalSubtrees(root.right)

        if root.left and root.right:
            count = left_count + right_count

            if root.left.val == root.val and root.right.val == root.val:
                count += 1
        elif root.left:
            count = left_count

            if root.left.val == root.val:
                count += 1
        elif root.right:
            count = right_count

            if root.right.val == root.val:
                count += 1
        
        return count

s = Solution()

a = TreeNode(5)
a.right = TreeNode(5)
a.right.right = TreeNode(5)
a.left = TreeNode(1)
a.left.left = TreeNode(5)
a.left.right = TreeNode(5)

assert s.countUnivalSubtrees(a) == 4