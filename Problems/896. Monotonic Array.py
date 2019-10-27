from typing import *

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        prev_delta = 0

        for i in range(len(A)-1):
            if A[i] != A[i+1]:
                delta = A[i+1] - A[i]

                if prev_delta != 0:
                    if prev_delta > 0 and delta < 0 or prev_delta < 0 and delta > 0:
                        return False
                
                prev_delta = delta
        
        return True

s = Solution()

assert s.isMonotonic([1,2,2,3]) == True
assert s.isMonotonic([6,5,4,4]) == True
assert s.isMonotonic([1,3,2]) == False
assert s.isMonotonic([1,1,1]) == True
assert s.isMonotonic([1,2,4,5]) == True
assert s.isMonotonic([1]) == True
assert s.isMonotonic([1,2]) == True
assert s.isMonotonic([3,2]) == True