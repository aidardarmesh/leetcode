from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # imax/imin store max/min products according to current nums[i]
        # res stores subarray maximum product
        imax = imin = res = nums.pop(0)
        
        for num in nums:
            # multiplying big number by negative makes it smaller
            # small number bigger => we redefine extremums by swap
            if num < 0:
                imax, imin = imin, imax
            
            # max/min for current is prod until current or current number itself
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            
            res = max(res, imax)
        
        return res
