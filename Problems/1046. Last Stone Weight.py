from typing import *
import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        while stones:
            hq.heappush(heap, -stones.pop())
        
        while len(heap) >= 2:
            y = -hq.heappop(heap)
            x = -hq.heappop(heap)

            if y != x:
                hq.heappush(heap, x-y)
        
        return -hq.heappop(heap) if len(heap) > 0 else 0

s = Solution()

# problem tests
assert s.lastStoneWeight([2,7,4,1,8,1]) == 1
assert s.lastStoneWeight([1]) == 1
assert s.lastStoneWeight([3,7,2]) == 2