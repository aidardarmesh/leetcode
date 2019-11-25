from typing import *

class Solution:
    def findComplement(self, num: int) -> int:
        def bits_num(num):
            i = 0
            
            while num:
                i += 1
                num = num >> 1
            
            return i
        
        bits = bits_num(num)
        max_ = (1 << bits) - 1
        
        return num ^ max_
