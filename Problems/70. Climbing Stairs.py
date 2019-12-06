from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0:1}
        
        def helper(n):
            if n in cache:
                return cache[n]

            if n < 0:
                return 0

            result = helper(n-1) + helper(n-2)
            cache[n] = result

            return result
        
        return helper(n)
