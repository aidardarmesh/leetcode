from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        MAX_INT = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        ans = 0
        
        for i in range(32):
            bit_sum = 0
            
            for num in nums:
                bit_sum += (num & (1 << i)) != 0
            
            ans = ans ^ ((bit_sum % 3 == 1) << i)
        
        return ans if ans <= MAX_INT else ~(ans ^ mask)
