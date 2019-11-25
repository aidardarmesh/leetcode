from typing import *

class Solution(object):
    def hammingWeight(self, n):
        ones = 0
        
        while n > 0:
            ones += n % 2
            n //= 2
        
        return ones
