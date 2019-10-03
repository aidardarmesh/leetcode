from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]

s = Solution()

assert s.addBinary("11", "1") == "100"
assert s.addBinary("1010", "1011") == "10101"