from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1.0
            
            half = fastPow(x, n // 2)

            if n % 2 == 0:
                return half * half
            
            return half * half * x
        
        if n < 0:
            x = 1.0 / x
            n = -n
        
        return fastPow(x, n)
