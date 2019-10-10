from typing import *

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        return haystack.find(needle)

s = Solution()

assert s.strStr("hello", "ll") == 2
assert s.strStr("aaaaa", "bba") == -1
assert s.strStr("qwe", "") == 0