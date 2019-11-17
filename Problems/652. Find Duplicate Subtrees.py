from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []
        
        d = {}
        
        def serialize(root):
            if not root:
                return 'X,'
            
            return str(root.val) + ',' + serialize(root.left) + serialize(root.right)
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            serial = serialize(node)
            
            if serial in d:
                d[serial].append(node)
            else:
                d[serial] = [node]
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        res = []
        
        for lst_node in d.values():
            if len(lst_node) >= 2:
                res.append(lst_node.pop())
        
        return res
        
