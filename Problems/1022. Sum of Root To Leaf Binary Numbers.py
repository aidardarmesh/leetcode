from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.nums = []

    def fulfill(self, root: TreeNode, num: str):
        if not root:
            return

        num += str(root.val)
        
        if not root.left and not root.right:
            self.nums.append(num)

        self.fulfill(root.left, num)
        self.fulfill(root.right, num)
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.fulfill(root, "")

        return sum(list(map(lambda x: eval("0b" + x), self.nums)))

a = TreeNode(1)
a.left = TreeNode(0)
a.left.left = TreeNode(0)
a.left.right = TreeNode(1)
a.right = TreeNode(1)
a.right.left = TreeNode(0)
a.right.right = TreeNode(1)

s = Solution()

assert s.sumRootToLeaf(a) == 22