from typing import *
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        if len(stones) < 2:
            return stones.pop()

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone_larger = -heapq.heappop(heap)
            stone_smaller = -heapq.heappop(heap)

            stone_reminder = stone_larger - stone_smaller

            if stone_reminder != 0:
                heapq.heappush(heap, -stone_reminder)

        if heap:
            return -heapq.heappop(heap)
        
        return 0

s = Solution()

# problem tests
assert s.lastStoneWeight([2,7,4,1,8,1]) == 1
assert s.lastStoneWeight([1]) == 1
assert s.lastStoneWeight([3,7,2]) == 2