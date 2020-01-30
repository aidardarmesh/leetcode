from typing import *

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0

        for right in range(len(A)):
            K -= 1 - A[right]
            
            if K < 0:
                K += 1 - A[left]
                left += 1
        
        return right - left + 1
