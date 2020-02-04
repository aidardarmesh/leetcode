from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        f1, f2 = 0, 1

        for _ in range(n):
            f1, f2 = f2, f1+f2
        
        return f2
