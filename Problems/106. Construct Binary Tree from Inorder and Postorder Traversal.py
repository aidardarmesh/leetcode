from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        val_index = {}

        for index, val in enumerate(inorder):
            val_index[val] = index
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            root = TreeNode(postorder.pop())
            root_index = val_index[root.val]
            root.right = helper(root_index+1, in_right)
            root.left = helper(in_left, root_index-1)

            return root
        
        return helper(0, len(inorder)-1)

s = Solution()

print((s.buildTree([9,3,15,20,7], [9,15,7,20,3])).val)