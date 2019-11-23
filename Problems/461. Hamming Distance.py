from typing import *

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x^y
        ones = 0
        
        while diff:
            ones += diff & 1
            diff = diff >> 1
        
        return ones
