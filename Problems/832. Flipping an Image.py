from typing import *

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for a in A:
            n = len(a)
            l = 0
            r = n-1

            while l <= r:
                a[l], a[r] = a[r]^1, a[l]^1
                l += 1
                r -= 1
        
        return A

s = Solution()

assert s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]
assert s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]