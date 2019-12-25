from typing import *

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        MAX = 0xFFFFFFFF
        ans = MAX
        sum_ = 0
        
        for i, num in enumerate(nums):
            sum_ += num
            
            while sum_ >= s:
                ans = min(ans, i+1-left)
                sum_ -= nums[left]
                left += 1
            
        return ans if ans != MAX else 0
