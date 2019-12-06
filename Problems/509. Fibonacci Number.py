from typing import *

class Solution:
    cache = {}
    
    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        
        if N < 2:
            result = N
        else:
            result = self.fib(N-1) + self.fib(N-2)
        
        self.cache[N] = result
        
        return result

s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
print(s.fib(5))