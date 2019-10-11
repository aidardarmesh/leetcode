from typing import *

class Solution:
    def morph(self, s: str) -> str:
        d, res = {}, ""

        for i in range(len(s)):
            d.setdefault(s[i], str(i))
        
        for ch in s:
            res += d[ch]
        
        return res

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.morph(s) == self.morph(t)

s = Solution()

assert s.isIsomorphic("egg", "add") == True
assert s.isIsomorphic("foo", "bar") == False
assert s.isIsomorphic("paper", "title") == True