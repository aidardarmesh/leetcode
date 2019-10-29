from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p, q)
    
    def find(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return root
        
        if root == p or root == q:
            return root
        
        left_subtree = self.find(root.left, p, q)
        right_subtree = self.find(root.right, p, q)
        
        if left_subtree and right_subtree:
            return root
        
        if left_subtree:
            return left_subtree
        
        if right_subtree:
            return right_subtree
        
        return None