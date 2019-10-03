from typing import *
import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor(-0.5 + math.sqrt(2 * n + 0.25));

s = Solution()

assert s.arrangeCoins(5) == 2
assert s.arrangeCoins(6) == 3
assert s.arrangeCoins(8) == 3