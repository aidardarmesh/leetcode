from typing import *

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left, right, s):
            if left <= right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1, s)
        
        helper(0, len(s)-1, s)


s = Solution()
l = list('hello')

s.reverseString(l)
assert l == ['o', 'l', 'l', 'e', 'h']

l = list('Hannah')
s.reverseString(l)
assert l == ['h', 'a', 'n', 'n', 'a', 'H']