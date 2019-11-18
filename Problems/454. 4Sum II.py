from typing import *


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res, ab = 0, {}
        
        for a in A:
            for b in B:
                sum_ = a + b
                ab[sum_] = ab.get(sum_, 0) + 1
        
        for c in C:
            for d in D:
                sum_ = c+d
                
                if -sum_ in ab:
                    res += ab[-sum_]
        
        return res
