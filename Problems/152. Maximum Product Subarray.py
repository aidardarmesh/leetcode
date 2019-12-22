from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax = imin = res = nums.pop(0)
        
        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            
            res = max(res, imax)
        
        return res
