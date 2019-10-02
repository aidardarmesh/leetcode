from typing import *
import collections

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_indices = {}
        n = len(nums)

        for i in range(n):
            if not nums[i] in num_indices:
                num_indices[nums[i]] = []
            
            num_indices[nums[i]].append(i)
        
        degree = max([len(indices) for indices in num_indices.values()])

        if degree == 1:
            return 1
        
        return min([indices.pop() - indices.pop(0) + 1 if len(indices) == degree else 999999 for indices in num_indices.values()])

s = Solution()

assert s.findShortestSubArray([1, 2, 2, 3, 1]) == 2
assert s.findShortestSubArray([1,2,2,3,1,4,2]) == 6