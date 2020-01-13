from typing import *

class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.t = [0] * self.N
        
        for i, num in enumerate(nums):
            self._inc(i, num)
    
    def _inc(self, i, delta):
        while i < self.N:
            self.t[i] += delta
            i = i | (i+1)
    
    def _prefix(self, r):
        res = 0
        
        while r >= 0:
            res += self.t[r]
            r = (r & (r+1)) - 1
        
        return res

    def update(self, i: int, val: int) -> None:
        current = self._prefix(i) - self._prefix(i-1)
        
        self._inc(i, val-current)

    def sumRange(self, i: int, j: int) -> int:
        return self._prefix(j) - self._prefix(i-1)
    