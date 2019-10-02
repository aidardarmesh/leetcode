from typing import *
import collections

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}

        for i, num in enumerate(nums):
            left.setdefault(num, i)
            right[num] = i
            count[num] = count.get(num, 0) + 1
        
        res = len(nums)
        degree = max(count.values())

        for num in left:
            if count[num] == degree:
                res = min(res, right[num] - left[num] + 1)
        
        return res

s = Solution()

assert s.findShortestSubArray([1, 2, 3]) == 1
assert s.findShortestSubArray([1, 2, 2, 3, 1]) == 2
assert s.findShortestSubArray([1,2,2,3,1,4,2]) == 6