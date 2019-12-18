from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        
        for i, val in enumerate(nums):
            if left_sum == S - left_sum - nums[i]:
                return i
            
            left_sum += val
        
        return -1
