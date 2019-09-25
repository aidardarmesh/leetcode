from typing import *

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        # solve it with prefix-sum
        # it already should have first element in it
        prefix_sum = []
        prefix_sum.append(nums[0])

        for i in range(0, n-1):
            prefix_sum.append(prefix_sum[i] + nums[i+1])
        
        max_sum = prefix_sum[k-1]

        for i in range(k, n):
            k_sum = prefix_sum[i] - prefix_sum[i-k]

            if k_sum > max_sum:
                max_sum = k_sum
        
        return max_sum / k

s = Solution()

assert s.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75