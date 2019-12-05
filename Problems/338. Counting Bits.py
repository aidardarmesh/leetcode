from typing import *

class Solution:
    def countBits(self, num: int) -> List[int]:
        def num_bits(num):
            bits = 0
            
            while num:
                bits += 1
                num &= (num-1)
            
            return bits
        
        return [num_bits(i) for i in range(num+1)]
