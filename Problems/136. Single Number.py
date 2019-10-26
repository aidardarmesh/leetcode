from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for num in nums:
            res ^= num
        
        return res

s = Solution()

assert s.singleNumber([2,2,1]) == 1
assert s.singleNumber([4,1,2,1,2]) == 4