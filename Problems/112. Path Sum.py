from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        
        if not root.left and not root.right:
            return sum == 0
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

s = Solution()

a = TreeNode(5)
a.left = TreeNode(4)
a.right = TreeNode(8)
a.left.left = TreeNode(11)
a.right.left = TreeNode(13)
a.right.right = TreeNode(4)
a.left.left.left = TreeNode(7)
a.left.left.right = TreeNode(2)
a.right.right.right = TreeNode(1)

assert s.hasPathSum(a, 22) == True