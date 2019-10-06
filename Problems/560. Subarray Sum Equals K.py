from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and nums[0] == k:
            return 1
        
        n, counter = len(nums), 0
        prefix = [nums[0]]

        for i in range(1, n):
            prefix.append(nums[i] + prefix[i-1])
        
        for i in range(n-1, -1, -1):
            for j in range(i-1, -1, -1):
                if prefix[i] == k:
                    counter += 1
                
                if prefix[i] - prefix[j] == k:
                    counter += 1
        
        return counter

s = Solution()

assert s.subarraySum([1,1,1], 2) == 2