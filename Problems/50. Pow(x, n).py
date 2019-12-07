from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        
        return x * self.myPow(x, n-1)
