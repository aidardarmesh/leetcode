from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def max_index(self, arr):
        idx = 0

        for i in range(len(arr)):
            if arr[i] > arr[idx]:
                idx = i

        return idx
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        max_i = self.max_index(nums)
        root = TreeNode(nums[max_i])
        root.left = self.constructMaximumBinaryTree(nums[:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        
        return root