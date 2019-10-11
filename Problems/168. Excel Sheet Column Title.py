from typing import *

class Solution:
    def convertToTitle(self, n: int) -> str:
        alph, res = {}, []

        for i in range(65, 91):
            alph.setdefault((i-64)%26, chr(i))

        while n > 0:
            rem = n % 26
            int = n // 26
            res.insert(0, alph[rem])

            if rem == 0:
                int -= 1

            n = int
        
        return "".join(res)

s = Solution()

assert s.convertToTitle(1) == 'A'
assert s.convertToTitle(26) == 'Z'
assert s.convertToTitle(27) == 'AA'
assert s.convertToTitle(28) == 'AB'
assert s.convertToTitle(701) == 'ZY'