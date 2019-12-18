from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(a, b):
            while b:
                a, b = a ^ b, (a & b) << 1
            
            return a
        
        sum_ = add(int(a, 2), int(b, 2))
        
        return bin(sum_)[2:]

s = Solution()

assert s.addBinary("11", "1") == "100"
assert s.addBinary("1010", "1011") == "10101"