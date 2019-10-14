from typing import *

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max, n = nums[0]*nums[1]*nums[2], len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    prod = nums[i] * nums[j] * nums[k]
        
                    if max < prod:
                        max = prod
        
        return max

s = Solution()

assert s.maximumProduct([1,2,3]) == 6
assert s.maximumProduct([1,2,3,4]) == 24
assert s.maximumProduct([-4,-3,-2,-1,60]) == 720