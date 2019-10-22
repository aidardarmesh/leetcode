from typing import *

Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        queue = [root]
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                
                if node.val != val:
                    return False
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return True