from typing import *
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        stack, queue = [], []

        for ch in s:
            if ('a' <= ch and ch <= 'z') or ('0' <= ch and ch <= '9'):
                stack.append(ch)
                queue.append(ch)
        
        while stack:
            if stack.pop() != queue.pop(0):
                return False
        
        return True

s = Solution()

assert s.isPalindrome("A man, a plan, a canal: Panama") == True
assert s.isPalindrome("race a car") == False
assert s.isPalindrome("") == True
assert s.isPalindrome("0P") == False