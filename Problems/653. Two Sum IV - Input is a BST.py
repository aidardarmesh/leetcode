from typing import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        def in_order(root):
            stack = []
            node = root
            res = []
            
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                elif stack:
                    node = stack.pop()
                    res.append(node.val)
                    node = node.right
            
            return res
        
        nums = in_order(root)
        l, r = 0, len(nums)-1
        
        while l < r:
            pair_sum = nums[l]+nums[r]
            if pair_sum == k:
                return True
            elif pair_sum > k:
                r -= 1
            else:
                l += 1
        
        return False
