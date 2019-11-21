from typing import *

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get_item(nums, i):
            if i < 0 or i >= len(nums):
                return float('-inf')
            
            return nums[i]
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r) // 2
            
            if get_item(nums, m) < get_item(nums, m+1):
                l = m+1
                continue
            
            if get_item(nums, m) < get_item(nums, m-1):
                r = m-1
                continue
            
            return m
        
        return -1
