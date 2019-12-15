from typing import *

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        
        for i in range(len(nums)):
            memo[i] = [float('inf')] * 2001
        
        def dfs(i, sum_):
            if i == len(nums):
                if sum_ == S:
                    return 1
                
                return 0
            
            if memo[i][sum_] != float('inf'):
                return memo[i][sum_]
            
            add = dfs(i+1, sum_ + nums[i])
            sub = dfs(i+1, sum_ - nums[i])
            memo[i][sum_] = add + sub
            
            return memo[i][sum_]
        
        return dfs(0, 0)
