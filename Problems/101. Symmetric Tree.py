from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = []
        queue.append(root)

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.pop(0)
                level.append(node.left)
                level.append(node.right)
            
            left_stack = level[:len(level)//2]
            right_queue = level[len(level)//2:]

            while left_stack and right_queue:
                left = left_stack.pop()
                right = right_queue.pop(0)

                if not left and not right:
                    continue

                if not left or not right:
                    return False

                if left.val != right.val:
                    return False
            
            queue = list(filter(lambda x: x, level))
        
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