from typing import *

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_ = 0
        left = right = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_ = max(max_, left*2)
            elif right > left:
                left = right = 0
        
        left = right = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            
            if left == right:
                max_ = max(max_, right*2)
            elif left > right:
                left = right = 0
        
        return max_
