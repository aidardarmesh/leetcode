from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        
        for i in range(32):
            ones = 0
            
            for num in nums:
                ones += (num & (1 << i)) != 0
            
            if ones > len(nums)-ones:
                if i == 31:
                    candidate = -((1<<31)-candidate)
                else:
                    candidate |= 1 << i
        
        return candidate
