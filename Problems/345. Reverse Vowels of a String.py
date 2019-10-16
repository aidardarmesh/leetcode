from typing import *

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        stack_vowels, res = [], []

        for c in s:
            if c in vowels:
                stack_vowels.append(c)
        
        for c in s:
            if c in vowels:
                res.append(stack_vowels.pop())
            else:
                res.append(c)
        
        return "".join(res)

s = Solution()

assert s.reverseVowels("hello") == "holle"
assert s.reverseVowels("leetcode") == "leotcede"