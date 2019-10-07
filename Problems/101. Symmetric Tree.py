from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = []
        queue.append(root)
        queue.append(root)

        while queue:
            t1 = queue.pop()
            t2 = queue.pop()

            if not t1 and not t2:
                continue
            
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        
        return True


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