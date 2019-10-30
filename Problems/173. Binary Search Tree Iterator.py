from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = []
        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                self.res.append(node.val)
                node = node.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.res.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.res) > 0


node = TreeNode(7)
node.left = TreeNode(3)
node.right = TreeNode(15)
node.right.left = TreeNode(9)
node.right.right = TreeNode(20)

bst_iter = BSTIterator(node)
print(bst_iter.next())
print(bst_iter.next())
print(bst_iter.hasNext())
print(bst_iter.next())
print(bst_iter.hasNext())
print(bst_iter.next())
print(bst_iter.hasNext())
print(bst_iter.next())
print(bst_iter.hasNext())