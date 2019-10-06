from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n, counter = len(nums), 0
        prefix = {0: 0, 1: nums[0]}

        for i in range(1, n):
            prefix[i+1] = nums[i] + prefix[i]
        
        n += 1 # prefix length is longer to 1
        
        for i in range(n):
            for j in range(i+1, n):
                if prefix[j] - prefix[i] == k:
                    counter += 1
        
        return counter

s = Solution()

assert s.subarraySum([1,1,1], 2) == 2
# assert s.subarraySum([1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2], 6) == 5