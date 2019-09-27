from typing import *
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]

kthLargest = KthLargest(3, [4,5,8,2])
assert kthLargest.add(3) == 4
assert kthLargest.add(5) == 5
assert kthLargest.add(10) == 5
assert kthLargest.add(9) == 8
assert kthLargest.add(4) == 8