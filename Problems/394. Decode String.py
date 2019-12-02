from typing import *

class Solution:
    def decodeString(self, s: str) -> str:
        prev_digits, prev_chars = [], []
        digits, chars = '', ''
        
        for c in s:
            if c.isnumeric():
                digits += c
            elif c.isalpha():
                chars += c
            elif c == '[':
                prev_digits.append(digits)
                digits = ''
                prev_chars.append(chars)
                chars = ''
            elif c == ']':
                digits = int(prev_digits.pop())
                chars = digits * chars
                chars = prev_chars.pop() + chars
                digits = ''
        
        return chars
