from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n, counter = len(nums), 0
        prefix = {0: nums[0]}

        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i-1]
        
        prefix[n] = 0
        
        for i in range(-1, n-1):
            for j in range(i+1, n):
                if prefix[j%(n+1)] - prefix[i%(n+1)] == k:
                    counter += 1
        
        return counter

s = Solution()

assert s.subarraySum([1,1,1], 2) == 2
assert s.subarraySum([1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2], 6) == 5