from typing import *
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        heap = []
        most_freq = []

        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        for i in num_freq:
            if len(heap) == k:
                heapq.heappushpop(heap, (num_freq[i], i))
            else:
                heapq.heappush(heap, (num_freq[i], i))

        for i in range(len(heap)):
            most_freq.append(heapq.heappop(heap)[1])

        return most_freq

s = Solution()

assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert s.topKFrequent([1], 1) == [1]