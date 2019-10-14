from typing import *

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        return max(nums[0]*nums[1]*nums[n-1], nums[n-3]*nums[n-2]*nums[n-1])

s = Solution()

assert s.maximumProduct([1,2,3]) == 6
assert s.maximumProduct([1,2,3,4]) == 24
assert s.maximumProduct([-4,-3,-2,-1,60]) == 720