from typing import *

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_ = 0
        
        for i, val in enumerate(nums):
            if i % 2 == 0:
                sum_ += val
        
        return sum_
