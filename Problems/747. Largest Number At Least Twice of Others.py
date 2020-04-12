from typing import *

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_idx = -1
        max_val = float('-inf')
        
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_idx = i
                max_val = nums[i]
        
        for i in range(len(nums)):
            if i != max_idx and (nums[i] << 1) > max_val:
                return -1
        
        return max_idx
