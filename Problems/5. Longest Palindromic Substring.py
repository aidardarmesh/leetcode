from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        queue = []
        ans = ''
        n = len(s)
        
        # single-symbol palindromes
        for i in range(n):
            ans = s[i]
            queue.append((s[i], i-1, i+1))
        
        # double-symbol palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                ans = s[i]+s[i+1]
                queue.append((ans, i-1, i+2))
        
        while queue:
            palind, left, right = queue.pop(0)
            
            if left < 0 or right > n-1:
                continue
            
            if s[left] == s[right]:
                ans = s[left] + palind + s[right]
                queue.append((ans, left-1, right+1))
        
        return ans
