from typing import *

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(idx):
            return nums[idx] - nums[0] - idx
        
        for i in range(1, len(nums)):
            if missing(i-1) < k <= missing(i):
                return nums[i-1] + k - missing(i-1)
        
        return nums[-1] + k - missing(len(nums)-1)
