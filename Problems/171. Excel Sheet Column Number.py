from typing import *

class Solution:
    def titleToNumber(self, s: str) -> int:
        # converting "number" from 26 base to 10 base
        s = s[::-1]
        res = 0

        for exp, char in enumerate(s):
            res += (ord(char) - 65 + 1) * (26 ** exp)
        
        return res

s = Solution()
assert s.titleToNumber("A") == 1
assert s.titleToNumber("AB") == 28
assert s.titleToNumber("ZY") == 701