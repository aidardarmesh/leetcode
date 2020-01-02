from typing import *

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        if m > n:
            return -1
        
        a = 26
        modulus = 0x7FFFFFFF
        A = pow(a, m, modulus)
        h = h_curr = 0
        
        def to_int(s, i):
            return ord(s[i]) - ord('a')
        
        for i in range(m):
            h = (h*a + to_int(needle, i)) % modulus
            h_curr = (h_curr*a + to_int(haystack, i)) % modulus
            
        if h == h_curr:
            return 0
        
        for i in range(m, n):
            h_curr = (h_curr*a - to_int(haystack, i-m)*A + to_int(haystack, i)) % modulus
            
            if h == h_curr:
                return i-m+1
        
        return -1

s = Solution()

assert s.strStr("hello", "ll") == 2
assert s.strStr("aaaaa", "bba") == -1
assert s.strStr("qwe", "") == 0