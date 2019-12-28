from typing import *

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums.insert(0, 0)
        
        for i in range(1, n+1):
            nums[i] += nums[i-1]
        
        for i in range(2, n+1):
            for j in range(i-1):
                sum_ = nums[i] - nums[j]
                
                if sum_ == 0 or (k != 0 and sum_ % k == 0):
                    return True
        
        return False
