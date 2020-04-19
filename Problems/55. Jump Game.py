from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[n-1] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, min(i+1+nums[i], n)):
                dp[i] |= dp[j]
        
        return dp[0]
