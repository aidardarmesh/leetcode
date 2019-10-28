from typing import *

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ = sum([i for i in range(n+1)])

        return sum_ - sum(nums)

s = Solution()

assert s.missingNumber([3,0,1]) == 2
assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
assert s.missingNumber([0]) == 1