from typing import *

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum_val = 0

        for i in range(0, k):
            sum_val += nums[i]

        max_val = sum_val
        
        for i in range(0, n-k):
            sum_val = sum_val - nums[i] + nums[i+k]

            if sum_val > max_val:
                max_val = sum_val

        return max_val / k

s = Solution()

assert s.findMaxAverage([1,12,-5,-6,50,3,7,8], 3) == 20.0
assert s.findMaxAverage([8], 1) == 8.0