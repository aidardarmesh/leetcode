from typing import *
import collections

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, count, degree, res = {}, {}, 0, 0

        for i, num in enumerate(nums):
            first.setdefault(num, i)
            count[num] = count.get(num, 0) + 1

            if count[num] > degree:
                degree = count[num]
                res = i - first[num] + 1
            elif count[num] == degree:
                res = min(res, i - first[num] + 1)

        return res

s = Solution()

assert s.findShortestSubArray([1, 2, 2, 3, 1]) == 2
assert s.findShortestSubArray([1,2,2,3,1,4,2]) == 6