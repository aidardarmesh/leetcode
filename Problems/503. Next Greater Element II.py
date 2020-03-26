from typing import *

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        prev = []
        res = [0]*len(nums)
        
        for i in range(2*len(nums)-1, -1, -1):
            i = i % len(nums)
            found = False
            
            while prev:
                if nums[prev[-1]] > nums[i]:
                    res[i] = nums[prev[-1]]
                    found = True
                    break
                
                prev.pop()
            
            prev.append(i)
            
            if not found:
                res[i] = -1
                continue
        
        return res
        