from typing import *

class Solution:
    def titleToNumber(self, s: str) -> int:
        # converting "number" from 26 base to 10 base
        a = ord("A") - 1
        alph_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alph = {}

        for char in alph_str:
            alph.setdefault(char, ord(char) - a)

        s = list(s)
        i = 0
        res = 0
        
        while len(s):
            res += alph[s.pop()] * 26 ** i
            i += 1

        return res

s = Solution()
assert s.titleToNumber("A") == 1
assert s.titleToNumber("AB") == 28
assert s.titleToNumber("ZY") == 701