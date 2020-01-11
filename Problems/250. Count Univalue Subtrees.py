from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.cnt = 0
        
        def uni(root):
            is_uni = True
            
            if root.left:
                is_uni = uni(root.left) and is_uni  and root.val == root.left.val
            
            if root.right:
                is_uni = uni(root.right) and is_uni and root.val == root.right.val
            
            self.cnt += is_uni
            
            return is_uni
        
        uni(root)
        
        return self.cnt
