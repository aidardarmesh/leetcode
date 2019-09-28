from typing import *
import heapq

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        squares = []
        j = 0 # positive part pointer

        while j < n and A[j] < 0:
            j += 1
        
        i = j - 1 # negative part pointer

        while i >= 0 and j < n:
            if A[i] ** 2 < A[j] ** 2:
                squares.append(A[i]**2)
                i -= 1
            else:
                squares.append(A[j]**2)
                j += 1
        
        while i >= 0:
            squares.append(A[i]**2)
            i -= 1
        
        while j < n:
            squares.append(A[j]**2)
            j += 1

        return squares

s = Solution()

assert s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert s.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]