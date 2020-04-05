from typing import *

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(v*2, 1)
        
        return stack.pop()
