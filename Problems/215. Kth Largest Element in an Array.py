from typing import *
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        
        return heap[0]

s = Solution()

assert s.findKthLargest([3,2,1,5,6,4], 2) == 5
assert s.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4