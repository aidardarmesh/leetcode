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
    
    def predecessor(self, root):
        cur = root.left

        while cur and cur.right:
            cur = cur.right
        
        return cur

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val < key:
            root.left = self.deleteNode(root.left, key
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)
            
        return root