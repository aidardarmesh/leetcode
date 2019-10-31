from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.in_order_left(root)
    
    def in_order_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.in_order_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


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