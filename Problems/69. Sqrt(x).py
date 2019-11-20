from typing import *


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, mid = 1, x, 0
        
        while left <= right:
            mid = (left+right) // 2
            mid_sqr = mid**2
            
            if mid_sqr == x:
                return mid
            elif mid_sqr < x:
                left = mid+1
            else:
                right = mid-1
        
        if mid**2 > x:
            return mid-1
        
        return mid
