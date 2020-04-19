from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[n-1] = True
        last_good_idx = n-1
        
        for i in range(n-1, -1, -1):
            if nums[i] >= last_good_idx-i:
                dp[i] = True
                last_good_idx = i
        
        return dp[0]
