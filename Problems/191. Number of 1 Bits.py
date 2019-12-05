from typing import *

class Solution(object):
    def hammingWeight(self, n):
        ones = 0
        
        while n > 0:
            ones += 1
            n &= (n-1)
        
        return ones
