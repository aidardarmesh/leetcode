from typing import *
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        last_smallest = 0
        
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, matrix[i][j])
        
        while k > 0:
            last_smallest = heapq.heappop(heap)
            k -= 1
        
        return last_smallest

s = Solution()

assert s.kthSmallest([
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], 8) == 13

assert s.kthSmallest([
    [1],
], 1) == 1