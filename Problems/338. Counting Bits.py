from typing import *

class Solution:
    def countBits(self, num: int) -> List[int]:
        num += 1
        ans = [0 for _ in range(num)]
        
        for i in range(32):
            for n in range(num):
                ans[n] += ((n & (1 << i)) != 0)
        
        return ans
