from typing import *

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        rows = 0

        while n >= i:
            rows += 1
            n -= i
            i += 1
        
        return rows

s = Solution()

assert s.arrangeCoins(5) == 2
assert s.arrangeCoins(6) == 3
assert s.arrangeCoins(8) == 3