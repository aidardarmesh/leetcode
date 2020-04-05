from typing import *

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = depth = 0
        
        for i, c in enumerate(S):
            if c == '(':
                depth += 1
            else:
                depth -= 1
                
                if S[i-1] == '(':
                    ans += 2 ** depth
        
        return ans
