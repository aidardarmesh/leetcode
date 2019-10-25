from typing import *

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1

        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

s = Solution()
l = list('hello')

s.reverseString(l)
assert l == ['o', 'l', 'l', 'e', 'h']

l = list('Hannah')
s.reverseString(l)
assert l == ['h', 'a', 'n', 'n', 'a', 'H']