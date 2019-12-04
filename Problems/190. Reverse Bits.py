from typing import *

class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0x00000001
        ans = 0
        
        for _ in range(32):
            ans = ans << 1
            bit = n & mask
            ans ^= bit
            n = n >> 1
        
        return ans
