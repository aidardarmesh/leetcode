from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        
        if len(nums) == 1:
            return [nums]
        
        res = []
        
        for i in range(len(nums)):
            m = nums[i]
            rem = nums[:i] + nums[i+1:]
            
            for perm in self.permute(rem):
                res.append([m] + perm)
        
        return res
