from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        
        if not root:
            return
        
        root.val = 0
        queue = [root]
        self.values = set()
        
        while queue:
            node = queue.pop(0)
            self.values.add(node.val)
            
            if node.left:
                node.left.val = node.val*2 + 1
                queue.append(node.left)
            
            if node.right:
                node.right.val = node.val*2 + 2
                queue.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.values
