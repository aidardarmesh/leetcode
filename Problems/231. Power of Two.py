from typing import *

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 != 0:
                return False
            
            n = n >> 1
        
        return True

s = Solution()

assert s.isPowerOfTwo(1) == True
assert s.isPowerOfTwo(16) == True
assert s.isPowerOfTwo(218) == False