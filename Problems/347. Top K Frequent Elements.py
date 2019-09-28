from typing import *
import heapq, collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)

s = Solution()

assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert s.topKFrequent([1], 1) == [1]