from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        val = preorder.pop(0)
        index = inorder.index(val)
        root = TreeNode(val)

        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])

        return root

s = Solution()

root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
print(root.val)