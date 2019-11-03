from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.root = None
        self.helper(nums, 0, len(nums))
        
        return self.root
    
    def helper(self, nums, l, r):
        if l < r:
            m = (l+r) // 2
            self.insert(nums[m])
            self.helper(nums, l, m)
            self.helper(nums, m+1, r)
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
            
        node = self.root

        if node.val == val:
            pass

        while True:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right