from typing import *

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            found = False
            j = (i + 1) % len(nums)
            
            while i != j:
                if nums[i] < nums[j]:
                    res.append(nums[j])
                    found = True
                    break
                
                j = (j + 1) % len(nums)
            
            if not found:
                res.append(-1)
        
        return res
