from typing import *
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 0:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        i = 2

        while i*i < n:
            if not primes[i]:
                i += 1
                continue
            
            primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
            i += 1
        
        return sum(primes)

s = Solution()

assert s.countPrimes(10) == 4
assert s.countPrimes(14) == 6
assert s.countPrimes(10000) == 1229