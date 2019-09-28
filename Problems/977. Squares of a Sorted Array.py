from typing import *
import heapq

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([a**2 for a in A])

s = Solution()

assert s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert s.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]