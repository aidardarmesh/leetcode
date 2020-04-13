from typing import *

class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s)-1
        
        while left <= right and s[left] == ' ':
            left += 1
        
        while left <= right and s[right] == ' ':
            right -= 1
        
        from collections import deque
        d, word = deque(), []
        
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            
            left += 1
        
        d.appendleft(''.join(word))
        
        return ' '.join(d)

s = Solution()

assert s.reverseWords("the sky is blue") == "blue is sky the"
assert s.reverseWords("  hello world!  ") == "world! hello"
assert s.reverseWords("a good   example") == "example good a"