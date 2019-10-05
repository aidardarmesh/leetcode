from typing import *

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

s = Solution()

assert s.reverseWords("the sky is blue") == "blue is sky the"
assert s.reverseWords("  hello world!  ") == "world! hello"
assert s.reverseWords("a good   example") == "example good a"