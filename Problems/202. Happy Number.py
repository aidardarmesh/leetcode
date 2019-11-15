from typing import *


class Solution:
    def isHappy(self, n: int) -> bool:
        periods = set()
        
        while True:
            if n == 1:
                return True
            
            n_copy = n
            digits_sum = 0
            
            while n_copy > 0:
                digits_sum += (n_copy % 10) ** 2
                n_copy //= 10
            
            n = digits_sum
            
            if n in periods:
                break
            else:
                periods.add(n)
        
        return False

s = Solution()

assert s.isHappy(19) == True
assert s.isHappy(7) == True
assert s.isHappy(8) == False
