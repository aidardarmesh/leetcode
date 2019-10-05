from typing import *
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = set()

        for i in range(2, n):
            is_prime = True

            for divisor in primes:
                if i % divisor == 0:
                    is_prime = False
                    break
            
            if is_prime:
                primes.add(i)
        
        return len(primes)

s = Solution()

assert s.countPrimes(10) == 4
assert s.countPrimes(14) == 6