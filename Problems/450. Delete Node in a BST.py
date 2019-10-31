from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def successor(self, root):
        cur = root.right

        while cur and cur.left:
            cur = cur.left

        return cur

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root
        
        if root.val == key:
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left
            
            p = self.successor(root)
            root.val = p.val
            root.right = self.deleteNode(root.right, key)

            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        
        return root